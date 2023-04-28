import random
class Task:
    def __init__(self, type, code, description, list_of_durations, predecessors, r=1):  # r is the risk factor, default is 1 (no risk)
        self.code = code
        self.description = description
        self.type = type

        self.list_of_durations = list_of_durations 
        self.list_of_durations_with_risk_factor = self.update_durations_with_risk_factor(r, list_of_durations)  # Creates as new list of durations with the risk factor included
        self.duration = random.triangular(*self.list_of_durations_with_risk_factor) # Initilizes the list of three durations as a triangluar distribution and picks a random value from it

        self.predecessors = predecessors
        self.successors = []

        self.early_start_date = None
        self.early_completion_date = None
        self.late_start_date = None
        self.late_completion_date = None
        self.is_critical = False

    def update_durations_with_risk_factor(self, r, durations):
        a = durations[0] # a = min
        e = durations[1] # e = mode
        b = durations[2] # b = max
        e_new = e * r
        if e_new < a:
            e_new = a
        elif e_new > b:
            e_new = b
        durations = [a, b, e_new] # Order must be changed to [min, max, mode] for triangular distribution in random.triangular to work
        return durations

    def add_predecessor(self, predecessor):
        self.predecessors.append(predecessor)
        predecessor.successors.append(self)

    def add_successor(self, successor):
        self.successors.append(successor)
        successor.predecessors.append(self)    

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
    
    def set_is_critical(self):
        # A task is critical if its early start date is equal to its late start date
        if self.early_start_date == self.late_start_date:
            self.is_critical = True
        else:
            self.is_critical = False
        return self.is_critical

    def __str__(self):
        return f"{self.code}"
    
    def __repr__(self):
        return f"{self.code}"
