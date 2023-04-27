import random


class Task:
    def __init__(self, type, code, description, durations, predecessors, r=1):  # r is the risk factor, default is 1 (no risk). May be more dynamic in the future
        self.code = code
        self.description = description
        self.type = type

        self.durations = durations
        durations_updated = self.update_durations_with_risk_factor(r, durations)  # Update the durations with the risk factor, First in task 2.2 in the assignment
        self.duration = random.triangular(*durations_updated) # Randomly generate a duration from the given range of durations (min, mode, max)

        # print()
        # print(self.duration)
        # print(self.durations[1])
        # print()

        self.predecessors = predecessors
        # self.duration = durations[1] # Use the mode as the duration
        self.successors = []
        self.early_start_date = 0
        self.early_completion_date = 0
        self.late_start_date = 0
        self.late_completion_date = 0
        self.is_critical = False

    def update_durations_with_risk_factor(self, r, durations):
        a = durations[0] # a = min, b = max, e = mode
        e = durations[1]
        b = durations[2]
        e_new = e * r
        if e_new < a:
            e_new = a
        elif e_new > b:
            # set e_new as b
            e_new = b
        durations = (a, e_new, b)
        return durations

    #
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
