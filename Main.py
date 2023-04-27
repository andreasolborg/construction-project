
from Utils import *
from MachineLearning import *
from Task import *
from Project import *


def main():
    ml = MachineLearning()
    utils = Utils()
    project = Project(1.0)
    

    project.import_project_from_excel("Warehouse.xlsx")
    
    project.save_tree("test")

    #project.find_early_dates(1)
    #project.find_late_dates(1)
    #project.set_is_critical_for_all_tasks()
    #project.print_project()

    #print(project.duration, "project duration")

    # project.set_shortest_duration()
    # project.set_expected_duration()
    # project.set_longest_duration()


    # print("Shortest duration: ", project.shortest_duration)
    # print("Expected duration: ", project.expected_duration)
    # print("Longest duration: ", project.longest_duration)

    # samples = utils.make_samples(1000)
    # perform_statistics(samples)

    # write_to_csv(samples)

    #ml.run_classification_methods()
    #ml.run_regression_methods()


main()