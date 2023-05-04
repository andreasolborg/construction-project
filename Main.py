
from Utils import *
from MachineLearning import *
from Task import *
from Project import *

import time

def task1():
    # Encode PERT-diagram from an Excel file and save the graph as a png file
    project = Project(1.0)
    project.import_project_from_excel("Villa.xlsx")
    project.draw_pert_diagram("VillaPERTDiagram")

def task2_and_3():
    project = Project(1.0)
    project.import_project_from_excel("Villa.xlsx")
    project.find_early_dates()  # 1 indicates that we want to use the middle duration for each task. If set to None, we get a random duration for each task.
    project.find_late_dates()
    project.set_is_critical_for_all_tasks()
    project.print_project()
    project.export_detailed_project_to_excel("VillaProjectDetailed.xlsx")

    project.set_shortest_duration()
    project.set_expected_duration()
    project.set_longest_duration()

    print("Shortest duration: ", project.shortest_duration)
    print("Expected duration: ", project.expected_duration)
    print("Longest duration: ", project.longest_duration)


def task4():
    utils = Utils()
    samples = utils.make_samples(1000)
    utils.perform_statistics(samples)

def task5and6():
    start_time = time.time()
    utils = Utils()
    ml = MachineLearning()

    print("Making samples with early gate... This may take a while...")
    samples_with_early_gate = utils.make_mixed_samples_of_random_risk_factors(1000, "Early gate", "Early gate", ["C.2", "C.3"])
    print("--- %s seconds ---" % (time.time() - start_time))

    print("Making samples with center gate... This may take a while...")
    samples_with_center_gate = utils.make_mixed_samples_of_random_risk_factors(1000, "Center gate", "Center gate", ["H.2","H.3"])
    print("--- %s seconds ---" % (time.time() - start_time))

    print("Making samples with late gate... This may take a while...")
    samples_with_late_gate = utils.make_mixed_samples_of_random_risk_factors(1000, "Late gate", "Late gate", ["Q.2"])
    print("--- %s seconds ---" % (time.time() - start_time))

    print("Finished making samples.")

    utils.write_to_csv(samples_with_early_gate, "EarlyGate.csv")
    utils.write_to_csv(samples_with_center_gate, "CenterGate.csv")
    utils.write_to_csv(samples_with_late_gate, "LateGate.csv")


    ml.run_classification_methods("EarlyGate.csv")
    ml.run_classification_methods("CenterGate.csv")
    ml.run_classification_methods("LateGate.csv")

    ml.run_regression_methods("EarlyGate.csv")
    ml.run_regression_methods("CenterGate.csv")
    ml.run_regression_methods("LateGate.csv")
    









def main():
    ml = MachineLearning()
    project = Project(1.0)


    # project.import_project_from_excel("Villa.xlsx")
    # project.add_gate("Test_Gate", "Test gate", ["H.2", "H.3"])


    # project.find_early_dates(1)
    # project.find_late_dates(1)
    # project.set_is_critical_for_all_tasks()
    # project.print_project()



    # project.draw_pert_diagram("VillaPERTDiagram")
    # print(project.duration, "project duration")



    # samples = utils.make_samples(2, "Test_Gate", "Test gate", ["L.1", "M.1"])
    # utils.perform_statistics(samples)    
    # utils.write_to_csv(samples)

    ml.run_classification_methods()
    ml.run_regression_methods()


# main()
# task2_and_3()
task5and6()