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
        self.duration = random.triangular(*durations)
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
        # Add the predecessor to the list of predecessors
        print("Adding predecessor", predecessor.code, "to", self.code)
        self.predecessors.append(predecessor)
        if predecessor not in self.successors:
            self.successors.append(predecessor)
        

        
    def clear_predecessors(self):
        self.predecessors = []

    def clear_successors(self):
        self.successors = []

    def __str__(self):
        return f"{self.code} {self.description} {self.durations} {self.predecessors}"
    
    def __repr__(self):
        return f"{self.code}"


class Project:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks
        self.early_completion_date = 0
        self.late_completion_date = 0 

    def get_task_by_code(self, code):
        for task in self.tasks:
            if task.code == code:
                return task
        return None
    
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
            predecessors = str(row[4]).split(", ") # Convert string to list of strings, if it is None, then the list is empty
            predecessors = [] if predecessors is None else predecessors
            task = Task(code, description, durations, predecessors)
            tasks.append(task)
        for task in tasks:
            new_predecessors = []
            for comparing_task in tasks:
                if comparing_task.code in task.predecessors:
                    new_predecessors.append(comparing_task)
                    comparing_task.successors.append(task)
            task.predecessors = new_predecessors
        self.tasks = tasks
        wb.close()

    
    def print_tasks(self):
        for task in self.tasks:
            print(task.code, task.description, task.durations, task.predecessors, task.successors)

    # Find the early start and completion dates of each task
    def find_early_dates(self):
        for task in self.tasks:
            if len(task.predecessors) == 0:
                task.early_start_date = 0
            else:
                task.early_start_date = max([self.get_task_by_code(predecessor).early_completion_date for predecessor in task.predecessors])
            task.early_completion_date = task.early_start_date + task.duration    


        

def main():
    project = Project("Warehouse", [])
    project.read_tasks_from_excel("Warehouse.xlsx")
    project.print_tasks()



if __name__ == "__main__":
    main()
