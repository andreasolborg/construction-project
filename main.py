
from Utils import *
from MachineLearning import *
from Task import *
from Project import *


def main():
    project = Project([], 1.0)
   
    project.import_project_from_excel("Warehouse.xlsx")
    
  
    #project.find_early_dates()
    #project.find_late_dates()
    #project.find_critical_tasks()
    #project.print_project()

    #print(project.duration, "project duration")

    # project.set_shortest_duration()
    # project.set_expected_duration()
    # project.set_longest_duration()


    # print("Shortest duration: ", project.shortest_duration)
    # print("Expected duration: ", project.expected_duration)
    # print("Longest duration: ", project.longest_duration)

    # samples = make_samples(1000)
    # perform_statistics(samples)

    # write_to_csv(samples)

    machine_learning2()


main()