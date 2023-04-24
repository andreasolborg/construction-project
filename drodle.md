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