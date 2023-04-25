Task class parameters
- code
- description
- durations[List]
- predecessors

Task attributes
- All dates
- boolean critical
- random duration determination
- duration


Class methods:
- Calculate random duration
- add and clear predecessors and successors
- self.successors.append(successor)
        if self not in successor.predecessors:
            successor.addPredecessor(self)
- Get date(s)
- Calculate dates
- IsCritical?



ConstructionProject CLASS

Attributes:
- Name
- List of tasks
- early and late project duration
  - These are determined by 


early completion date = duration

late start date 



classificiation results to aim for
0.8 = 980 success
1.0 = 800 success
1.2 = 200 success
1.4 = 20 success