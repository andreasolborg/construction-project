# Required packages and software:
- sklearn 
- numpy
- panda
- seaborn
- matplotlib
- openpyxl

## Classes:
### Task: 		    
This class represents a task in a project. Every task has attributes for ES, EF, LS, and LF that are initially set to None until we run the algorithms for finding early and late dates in the Project class. Every task has list attributes for predecessors and successors so every task in a project is binded togheter like a linked list. Each task has a triangularly distributed duration range that incorporates a risk factor specific to the task. The actual duration for a task is selected randomly from this distribution. A task also has som general attributes as code, type and description.
### Project: 		    
In order to encode PERT diagrams, we have developed a Task class, which functions as Node objects within the PERT diagram. The Project class contains methods for calculating the shortest, expected, and longest durations of a project. This is accomplished through the find_early_dates function, which accepts a duration_index parameter, as outlined in the assignment description. The duration_index value, when set to n, selects the n-th duration within the duration range, with a zero index setting tasks to their shortest duration and a value of 2 setting tasks to their longest duration. If no duration_index is specified, a duration between (min, mode, max) is randomly chosen using the triangular distribution, with the risk factor considered. Once all tasks have been iterated over, the find_early_dates function assigns the project's duration to the maximum of all task early completion dates.

The add_gate function is responsible for incorporating a new gate into the project. It accepts a code, description, and a list of predecessor tasks as input parameters. Initially, the function verifies if the gate is valid.

Additionally, the Project class is equipped with an Excel spreadsheet loader for importing projects, which is executed via the import_project_from_excel function. This function iterates over every row in the spreadsheet, creating a Task object for each row, then assigns predecessors and successors to each Task object before adding the Task object to the project's task list. An exporter is also available to export comprehensive project information after early and late dates have been computed.

The Project class includes a printer function that displays pertinent information about each task within the project. When this function is run using the Warehouse project, it produces output consistent with the assignment description.

Furthermore, we provide a function to visually represent the project as a graph, illustrating dependencies and displaying the placement of a gate.

### Utils: 	        
The Utils class offers utility functions that, while not directly associated with a specific class, are valuable for various operations within the project. This class contains four methods: make_samples, make_mixed_samples_of_random_risk_factors, write_to_csv, and perform_statistics.

The make_samples function generates a sample of n random duration values for each risk factor. This method also accepts arguments for gate placement, although it will not place a gate if the arguments are not provided. In contrast, the make_mixed_samples_of_random_risk_factors function creates samples with random risk factors, rather than generating n samples for each risk factor, as the make_samples function does. This approach reduces the number of samples needed and computation time. Like make_samples, this function also accepts arguments for gate placement.

The write_to_csv function takes a list of samples as input and records the data to a specified CSV file, which is designed for use with machine learning algorithms. The perform_statistics function calculates and displays various statistical measures for the durations and classifications of provided samples, grouped by risk factors. This method takes a dictionary as input, with keys representing different risk factors and corresponding values as lists containing the associated samples for each risk factor. The displayed statistics encompass minimum, maximum, mean, standard deviation, deciles for durations, as well as counts of successful, acceptable, and failed projects.

### MachineLearning:	
The MachineLearning class is designed to perform machine learning tasks on a given CSV file. It contains two main functions: run_classification_methods and run_regression_methods. The function run_classification_methods applies classification algorithms (Logistic Regression, Random Forest, Support Vector Machine, and Decision Tree) on the dataset. It first reads the CSV file, splits the data into features and labels, and then into training and test sets. Afterward, it trains the models, evaluates their performance, and generates confusion matrices to visualize the results. The function run_regression_methods performs regression analysis on the dataset using Linear Regression, Random Forest, Support Vector Machine, and Decision Tree algorithms. Similar to the classification function, it reads the CSV file, splits the data, and trains the models. It then evaluates the models' performance using the metrics R-squared, mean squared error and absolute squared, and calculates the accuracy score.
### Main: 	        
This script runs all the tasks in the assignment, including tasks 1 through 6. 

### CSV format
Each row in the CSV file represents a sample, which corresponds to a single random execution of a project. The first value in each row indicates the gate placement, while the last value provides the correct classification for the project. The values between these two represent the early completion dates for each task in the project.