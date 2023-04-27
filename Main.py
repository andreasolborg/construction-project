
from Utils import *
from MachineLearning import *
from Task import *
from Project import *


def main():
    ml = MachineLearning()
    utils = Utils()
    project = Project(1.0)
    

    project.import_project_from_excel("Villa.xlsx")
    project.add_gate("Test_Gate", "Test gate", ["H.2", "H.3"])
    

    project.find_early_dates(1)
    project.find_late_dates(1)
    project.set_is_critical_for_all_tasks()
    project.print_project()



    project.draw_pert_diagram("VillaPERTDiagram")
    # print(project.duration, "project duration")

    # project.set_shortest_duration()
    # project.set_expected_duration()
    # project.set_longest_duration()


    # print("Shortest duration: ", project.shortest_duration)
    # print("Expected duration: ", project.expected_duration)
    # print("Longest duration: ", project.longest_duration)

    # samples = utils.make_samples(10)
    # perform_statistics(samples)
    samples = {0.8: [project]}
    utils.write_to_csv(samples)

    # ml.run_classification_methods()
    #ml.run_regression_methods()


main()