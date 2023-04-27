import os
from openpyxl import load_workbook
from Task import *


class Project:
    def __init__(self, r):
        self.tasks = None
        self.duration = 0
        self.shortest_duration = 0
        self.expected_duration = 0
        self.longest_duration = 0
        self.classification = None
        self.r = r

    def get_task_by_code(self, code):
        for task in self.tasks:
            if task.code == code:
                return task
        return None

    def set_shortest_duration(self):
        self.shortest_duration = self.find_early_dates(0)

    def set_expected_duration(self):
        self.expected_duration = self.find_early_dates(1)

    def set_longest_duration(self):
        self.longest_duration = self.find_early_dates(2)
    
    def get_tasks(self):
        return self.tasks
    
    def __repr__(self):
        return f"{self.classification}"
    
    # Find the critical tasks. A task is critical if its early and late dates are equal.
    def set_is_critical_for_all_tasks(self):
        for task in self.tasks:
            if task.early_start_date and task.early_completion_date and task.late_start_date and task.late_completion_date:
                if task.early_start_date == task.late_start_date and task.early_completion_date == task.late_completion_date:
                    task.is_critical = True
                else:
                    task.is_critical = False

    def print_task(self, task, dot_file):
        dot_file.write('{} [label="{}", style="filled", fontsize="60pt"];\n'.format(str(id(task)), str(task.code))) # write node
        for sucessor_task in task.successors:
                # if number of games inside the node is less than given threshold, we do not want to plot any children
                dot_file.write('{} [label="{}", style="filled", fontsize="60pt"];\n'.format(str(id(sucessor_task)), str(sucessor_task.code))) # write node
                dot_file.write('{} -> {} [fontsize="60pt" arrowsize="3"];\n'.format(str(id(task)), str(id(sucessor_task)))) # write edge 
                self.print_task(sucessor_task, dot_file) # recursive call to print child nodes


    def save_tree(self, filename):
        print("Saving graph to file {}".format(filename)) # print to console
        if os.path.exists("{}.dot".format(filename)): # if file already exists, delete it
            os.remove("{}.dot".format(filename))
        if os.path.exists("{}.png".format(filename)): # if file already exists, delete it
            os.remove("{}.png".format(filename))
        with open("{}.dot".format(filename), "w") as dot_file: 
            dot_file.write("digraph G {\n")
            dot_file.write('rankdir=LR;\ncenter=true;\nsize="10,7"\n')
            self.print_task(self.tasks[0], dot_file) # recursive call to print nodes
            dot_file.write("}\n")
        os.system("dot -Tpng -Gdpi=500 {}.dot -o {}.png".format(filename, filename)) # create png from dot file

    # Read the tasks from an excel file
    def import_project_from_excel(self, filename):
        wb = load_workbook(filename)
        ws = wb.active
        tasks = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            type = row[0]
            code = row[1]
            description = row[2]

            durations = eval(str(row[3]))
            durations = (0.0, 0.0, 0.0) if durations is None else durations

            predecessors = [] if row[4] is None else row[4].split(", ")
            if type == "Task" or type == "Gate":
                tasks.append(Task(type, code, description, durations, predecessors, self.r)) # takes in r from the project as a default value to be used in the task
        
        # Convert the predecessors from a list of codes to a list of tasks
        for task in tasks:
            new_predecessors = []
            for comparing_task in tasks:
                if comparing_task.code in task.predecessors:
                    new_predecessors.append(comparing_task)
                    comparing_task.add_successor(task)
            task.predecessors = new_predecessors
        self.tasks = tasks
        wb.close()

    def print_project(self):
        print(f"Tasks: {self.tasks}")
        print("Tasks:")
        for task in self.tasks:
            print(f"Task: {task}")
            print(f"Description: {task.description}")
            print(f"Predecessors: {task.predecessors}")
            print(f"Successors: {task.successors}")
            print(f"Duration: {task.duration}")
            print(f"Early start date: {task.early_start_date}")
            print(f"Early completion date: {task.early_completion_date}")
            print(f"Late start date: {task.late_start_date}")
            print(f"Late completion date: {task.late_completion_date}")
            print(f"Is critical: {task.is_critical}")
            print()

    def find_early_dates(self, duration_index=None):
        
        '''
        Early dates are thus calculated by propagating values from the source nodes to the
        sink nodes. The early start date of a task is the maximum of the early completion dates of
        its predecessors plus the task duration. The early completion date of a task is the sum of
        its early start date and its duration.

        1. Start with a list of all tasks
        2. While it remains a task in the list,
            a. Find a task with no predecessors
            b. Remove it from the list
            c. Calculate its early start date and early completion date
        The minimum of the porject is the maximum of the early completion dates of the tasks
        Early dates is thus calculated by propagating values from the source nodes to the sink nodes
        '''

        self.duration = 0
        tasks = self.tasks.copy()
        while len(tasks) > 0:
            for task in tasks:
                if task.has_predecessor_in_list(tasks):
                    continue
                if len(task.predecessors) == 0:
                    task.early_start_date = 0
    
                    if duration_index is not None:
                        task.early_completion_date = task.early_start_date + task.list_of_durations[duration_index]
                    else:
                        task.early_completion_date = task.early_start_date + task.duration
                else:
                    task.early_start_date = max([predecessor.early_completion_date for predecessor in task.predecessors])
                    if duration_index is not None:
                        task.early_completion_date = task.early_start_date + task.list_of_durations[duration_index]
                    else:
                        task.early_completion_date = task.early_start_date + task.duration
                tasks.remove(task)
        self.duration = max([task.early_completion_date for task in self.tasks])
        return self.duration
        
    def find_late_dates(self, duration_index=None):
        tasks = self.tasks.copy()
        while len(tasks) > 0:
            for task in tasks:
                if task.has_successor_in_list(tasks):
                    continue
                if len(task.successors) == 0:
                    task.late_completion_date = task.early_completion_date
                    task.late_start_date = task.early_start_date
                else:
                    task.late_completion_date = min([successor.late_start_date for successor in task.successors])
                    if duration_index is not None:
                        task.late_start_date = task.late_completion_date - task.list_of_durations[duration_index]
                    else:
                        task.late_start_date = task.late_completion_date - task.duration
                tasks.remove(task)

    def classify_project(self):
        
        '''
        Classify the project as either a success, acceptable, or failure.
        Success: The projects actual duration does not exceed the expected duration by more than 5% (with a risk factor of 1.0)
        Acceptable: The actual duration of the project stands between 105% and 115% of the expected duration (with a risk factor of 1.0)
        Failure: The actual duration of the project exceeds its expected duration by more than 15% (with a risk factor of 1.0)
        '''
        
        if self.duration <= self.expected_duration * 1.05:
            self.classification = "Success"
        elif self.duration <= self.expected_duration * 1.15:
            self.classification = "Acceptable"
        else:
            self.classification = "Failure"
        return self.classification