"""
Author: Andreas Olborg and Jon Grendstad
Group: group 4
"""

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
    project.find_early_dates(None)  # 1 indicates that we want to use the middle duration for each task. If set to None, we get a random duration for each task.
    project.find_late_dates(None)
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
    '''
    This function makes csv files with samples of projects with different risk factors and gates. The csv files are used in the MachineLearning class.
    Initilazing the samples takes a long time, so comment out the code if you don't need to make new samples.
    '''
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


def miscellaneous():
    '''
    Draw the PERT-diagram with different gates. The gates are added to the project after the project has been imported from an Excel file.
    '''
    # project_with_early_gate = Project(1.0)
    # project_with_early_gate.import_project_from_excel("Villa.xlsx")
    # project_with_early_gate.add_gate("Early gate", "Early gate", ["C.2", "C.3"])
    # project_with_early_gate.draw_pert_diagram("images/VillaPERTDiagramWithEarlyGate")

    # project_with_center_gate = Project(1.0)
    # project_with_center_gate.import_project_from_excel("Villa.xlsx")
    # project_with_center_gate.add_gate("Center gate", "Center gate", ["H.2","H.3"])
    # project_with_center_gate.draw_pert_diagram("images/VillaPERTDiagramWithCenterGate")

    project_with_late_gate = Project(1.0)
    project_with_late_gate.import_project_from_excel("Villa.xlsx")
    project_with_late_gate.add_gate("Late gate", "Late gate", ["P.1", "P.2", "P.3"])
    project_with_late_gate.draw_pert_diagram("images/VillaPERTDiagramWithLateGate")

    # project_with_early_and_center_gate = Project(1.0)
    # project_with_early_and_center_gate.import_project_from_excel("Villa.xlsx")
    # project_with_early_and_center_gate.draw_pert_diagram("images/VillaPERTDiagramStandard")

    

miscellaneous()
task2_and_3()
# task5and6()