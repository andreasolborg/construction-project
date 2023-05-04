# Required packages and software:
- sklearn 
- numpy
- panda
- seaborn
- matplotlib
- openpyxl

# General overview:
## Classes:
### Task: 		    
This class represents a task in a project. Every task has attributes for ES, EF, LS, and LF that are initially set to None until we run the algorithms for finding early and late dates in the Project class. Every task has list attributes for predecessors and successors so every task in a project is binded togheter like a linked list. Each task has a triangularly distributed duration range that incorporates a risk factor specific to the task. The actual duration for a task is selected randomly from this distribution. A task also has som general attributes as code, type and description.
### Project: 		    
For encoding PERT diagrams, we created a Task class which serves as Node objects in the PERT-diagram. The Project class has functions for determining shortest, expected, and longest duration of a project. This is done by calling the find_early_dates function that takes in the parameter duration_index, which follows the algorithm described in the assignment description. If a duration_index is set to n, it will choose the n-th duration in duration range, so zero index will set all tasks to their shortest duration, and 2 will set all tasks to their longest duration. If no duration_index is set, it will randomly choose a duration between (min, mode, max) using the triangular distribution with the risk factor taken into account. After iterating over all tasks, the find_early_dates function will then set the projects duration to the maximum of all the tasks early completion dates. The Project class also has a loader for Excel spreadsheets for importing projects. This is done by calling the import_project_from_excel function. This function will iterate over all the rows in the Excel spreadsheet and create a Task object for each row. It will then add the predecessors and successors to each Task object, and add the Task object to the projects list of tasks. The Project class also has a printer function that prints sufficient information about each task in the project. Running this function with the Warehouse project gives output that matches the output in the assignment description. 
### Utils: 	        
The Utils class, provides utility functions that are not directly tied to any specific class but are useful for general operations in the project. The Utils class includes three methods: make_samples, write_to_csv, and perform_statistics.  

Utils is a class that has all the "utillity" function that dosent belong in the other classs. W
### MachineLearning:	
TODO
### Main: 	        
TODO


## Task 4
The Project class has a function for classifying if a project was Success, Acceptable or a Failure. This function is used in Utils.py in the make_samples(n) function, which creates n samples for each risk factor. The function returns a dictionary with risk factor as key, and a list of the projects as value. The returned dictionary can be used as input to the perform_statistics(samples_with_risk_factor) function, which will print the statistics of the samples for each risk factor.



# Machine learning