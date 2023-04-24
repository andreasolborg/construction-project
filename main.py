'''
Table 1 describes the tasks of the construction of a warehouse.
Types   | Codes | Description                   | Duration | Predecessors
--------|-------|-------------------------------|----------|--------------
Gate    | Start |                               |          | 
Task    | A     | Agreement of the owner        | 3, 4, 6 | Start
Task    | B     | Preparation of the ground     | 1, 2, 4 | Start
Task    | C     | Order of materials            | 1, 1, 3 | A
Task    | D     | Excavation                    | 1, 1, 3 | A, B
Task    | E     | Order of doors and windows    | 1, 2, 4 | A
Task    | F     | Delivery of materials         | 1, 2, 4 | C
Task    | G     | Concrete foundations          | 1, 2, 4 | D, F
Task    | H     | Delivery of doors and windows | 8, 10, 12 | E
Task    | J     | Frame, roofs, walls           | 3, 4, 6 | G
Task    | K     | Installation of doors and windows | 1, 1, 3 | H, J
Gate    | End   |                               |          | J, H



Table 2: Early and late dates for the warehouse project

Task | Start | A | B | C | D | E | F | G | H | J | K | En
-----|-------|---|---|---|---|---|---|---|---|---|---|-----
Duration | 0 | 4 | 2 | 1 | 2 | 2 | 2 | 2 | 10 | 4 | 1 | 0
Early start date | 0 | 0 | 0 | 4 | 4 | 4 | 5 | 7 | 6 | 9 | 16 | 17
Early completion date | 0 | 4 | 2 | 5 | 5 | 6 | 7 | 9 | 16 | 13 | 17 | 17
Late start date | 0 | 0 | 7 | 7 | 9 | 4 | 8 | 10 | 6 | 12 | 16 | 17
Late completion date | 0 | 4 | 9 | 8 | 10 | 6 | 10 | 12 | 16 | 16 | 17 | 17


'''
import random
from openpyxl import load_workbook

class Task:
    def __init__(self, code, description, durations, predecessors):
        self.code = code
        self.description = description
        self.durations = durations
        self.predecessors = predecessors
        self.duration = random.triangular(*durations) # Randomly generate a duration from the given range of durations (min, mode, max)
        # self.duration = durations[1] # Use the mode as the duration
        self.successors = []
        self.early_start_date = 0
        self.early_completion_date = 0
        self.late_start_date = 0
        self.late_completion_date = 0
        self.is_critical = False

    # Getters and setters for the dates
    def get_early_start_date(self):
        return self.early_start_date
    
    def get_early_completion_date(self):
        return self.early_completion_date

    def get_late_start_date(self):
        return self.late_start_date

    def get_late_completion_date(self):
        return self.late_completion_date
    
    def get_is_critical(self):
        return self.is_critical

    def add_predecessor(self, predecessor):
        self.predecessors.append(predecessor)
        predecessor.successors.append(self)

    def add_successor(self, successor):
        self.successors.append(successor)
        successor.predecessors.append(self)    
        
    def clear_predecessors(self):
        self.predecessors = []

    def clear_successors(self):
        self.successors = []

    def has_predecessor_in_list(self, tasks):
        for task in tasks:
            if task in self.predecessors:
                return True
        return False
    
    def has_successor_in_list(self, tasks):
        for task in tasks:
            if task in self.successors:
                return True
        return False


    def __str__(self):
        return f"{self.code}"
    
    def __repr__(self):
        return f"{self.code}"


class Project:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks
        self.duration = 0
        self.shortest_duration = 0
        self.expected_duration = 0
        self.longest_duration = 0

    def get_task_by_code(self, code):
        for task in self.tasks:
            if task.code == code:
                return task
        return None

    def set_shortest_duration(self):
        self.shortest_duration = 0
        self.shortest_duration = self.find_early_dates("Shortest")

    def set_expected_duration(self):
        self.expected_duration = 0
        self.expected_duration = self.find_early_dates("Expected")

    def set_longest_duration(self):
        self.longest_duration = 0
        self.longest_duration = self.find_early_dates("Longest")
    
    def get_tasks(self):
        return self.tasks
    
    # Read the tasks from an excel file
    def import_project_from_excel(self, filename):
        wb = load_workbook(filename)
        ws = wb.active
        tasks = []
        for row in ws.iter_rows(min_row=2, values_only=True):
            type = row[0]
            code = row[1]
            description = row[2]
            durations = eval(str(row[3])) # Convert string to list of integers, if it is None, then the list is (0, 0, 0)
            durations = (0, 0, 0) if durations is None else durations
            predecessors = [] if row[4] is None else row[4].split(", ")
            if type == "Task" or type == "Gate":
                tasks.append(Task(code, description, durations, predecessors))
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
        '''
        Design a printer to print projects, including the list of successors of each task, their
        early and late dates, and their criticality. Use this printer to test both the data
        structures you designed in Task 1. and your loader.
        '''    
        print(f"Project: {self.name}")
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
            print(f"Project: {self.name}")
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
        print("Finding early dates...")
        tasks = self.tasks.copy()
        while len(tasks) > 0:
            for task in tasks:
                if duration_index is not None:
                    if duration_index == "Shortest":
                        task.duration = task.durations[0]
                    elif duration_index == "Expected":
                        task.duration = task.durations[1]
                    elif duration_index == "Longest":
                        task.duration = task.durations[2]
                # if duration_index is not None:
                #     task.duration = task.durations[duration_index]  # 0: shortest, 1: expected, 2: longest, hvilken foretrekker du?
                if task.has_predecessor_in_list(tasks):
                    continue
                if len(task.predecessors) == 0:
                    task.early_start_date = 0
                    task.early_completion_date = task.early_start_date + task.duration
                else:
                    task.early_start_date = max([predecessor.early_completion_date for predecessor in task.predecessors])
                    task.early_completion_date = task.early_start_date + task.duration
                tasks.remove(task)
        self.duration = max([task.early_completion_date for task in self.tasks])
        print("Early dates found.")
        return self.duration
        
    def find_late_dates(self, duration_index=None):
        '''
        The late completion date of a task is the minimum of the late start dates of its successors, and
        the project duration if the task has no successors. The late start date of a task is its late
        completion date minus its duration.
        1. Start with a list of all tasks
        2. While it remains a task in the list,
            a. Find a task in the list whose all successors are not in the list
            b. Remove it from the list
            c. Calculate its late start date and late completion date
        '''
        print("Finding late dates...")
        tasks = self.tasks.copy()
        while len(tasks) > 0:
            for task in tasks:
                if duration_index is not None:
                    if duration_index == "Shortest":
                        task.duration = task.durations[0]
                    elif duration_index == "Expected":
                        task.duration = task.durations[1]
                    elif duration_index == "Longest":
                        task.duration = task.durations[2]
                # if duration_index is not None:
                #     task.duration = task.durations[duration_index]
                if task.has_successor_in_list(tasks):
                    continue
                if len(task.successors) == 0:
                    task.late_completion_date = task.early_completion_date
                    task.late_start_date = task.early_start_date
                else:
                    task.late_completion_date = min([successor.late_start_date for successor in task.successors])
                    task.late_start_date = task.late_completion_date - task.duration
                tasks.remove(task)
                print("Removed task: ", task)
        print("Late dates found.")

    # Find the critical tasks
    def find_critical_tasks(self):
        for task in self.tasks:
            if task.early_start_date == task.late_start_date and task.early_completion_date == task.late_completion_date:
                task.is_critical = True
            else:
                task.is_critical = False
            
    ######################
    # Machine Learning
    ######################

    risk_factors = [0.8, 1.0, 1.2, 1.4]
    expected_duration =0 


def main():
    project = Project("Villa", [])
    project.import_project_from_excel("Warehouse.xlsx")
    project.find_early_dates("Shortest")
    project.find_late_dates("Shortest")
    project.find_critical_tasks()
    project.print_project()

    project.set_shortest_duration()
    project.set_expected_duration()
    project.set_longest_duration()

    print("Shortest duration: ", project.shortest_duration)
    print("Expected duration: ", project.expected_duration)
    print("Longest duration: ", project.longest_duration)

if __name__ == "__main__":
    main()
