from Project import *
import random
import statistics
import pandas as pd

   
'''
Make at random a sample 1000 of values of durations for each value of the risk factor.
Calculate the duration of the project for each of the 1000 samples.
'''

class Utils:


    def make_samples(n):
        risk_factors = [0.8, 1.0, 1.2, 1.4]
        samples_with_risk_factor = {}
        for risk_factor in risk_factors:
            sample_with_risk_factor = []
            for i in range(n):
                project = Project([], risk_factor)
                project.import_project_from_excel("Villa.xlsx")
                project.set_expected_duration()
                project.find_early_dates()
                project.classify_project()
                sample_with_risk_factor.append(project)

            samples_with_risk_factor[risk_factor] = sample_with_risk_factor
        return samples_with_risk_factor

    def write_to_csv(samples_with_risk_factor):
        '''
        Takes in a dictionary with risk factors as keys and a list of samples as values. Randomly choose a sample from each risk factor and write it to a csv file.
        '''
        amount_of_samples = len(samples_with_risk_factor[0.8]) # Randomly choose a sample from each risk factor
        for i in range(amount_of_samples):
            random_risk_factor = random.choice(list(samples_with_risk_factor.keys()))
            sample = samples_with_risk_factor[random_risk_factor][i]
            samples_to_save = []
            tasks = []
            task_duration = 0
            for task in sample.tasks[1:-1]: # Exclude the first and last task
                task_duration += task.duration
                tasks.append(task_duration)
            tasks.append(sample.classification)
            samples_to_save.append(tasks)
            #Overwrite the file if it already exists
            pd.DataFrame(samples_to_save).to_csv("samples.csv", mode='a', header=False, index=False)


    def perform_statistics(samples_with_risk_factor):
        '''
        Perform statistics on these durations (minimum, maximum,
        mean, standard-deviation, deciles), as well as on the numbers of successful, acceptable
        and failed projects.
        '''
        for risk_factor in samples_with_risk_factor:
            samples = samples_with_risk_factor[risk_factor]
            durations = [sample.duration for sample in samples]
            classifications = [sample.classification for sample in samples]
            print("Risk factor: ", risk_factor)
            # print("Durations: ", durations)
            # print("Classifications: ", classifications)
            print("Minimum duration: ", min(durations))
            print("Maximum duration: ", max(durations))
            print("Mean duration: ", sum(durations)/len(durations))
            print("Standard deviation: ", statistics.stdev(durations))
            print("Deciles: ", statistics.quantiles(durations, n=10))
            print("Number of successes: ", classifications.count("Success"))
            print("Number of acceptables: ", classifications.count("Acceptable"))
            print("Number of failures: ", classifications.count("Failure"))
            print("")

        