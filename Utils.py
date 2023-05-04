from Project import *
import random
import statistics
import pandas as pd
import time



class Utils:
    def make_samples(self, n, gate_name=None, gate_description=None, gate_predeccessors=None):
        '''
        Make at random a sample n of values of durations for each value of the risk factor.
        '''
        risk_factors = [0.8, 1.0, 1.2, 1.4]
        samples_with_risk_factor = {}
        for risk_factor in risk_factors:
            sample_with_risk_factor = []
            for i in range(n):
                project = Project(risk_factor)
                project.import_project_from_excel("Villa.xlsx")
                if gate_name != None and gate_description != None and gate_predeccessors != None:
                    project.add_gate(gate_name, gate_description, gate_predeccessors)
                project.set_expected_duration()
                project.find_early_dates()
                project.classify_project()
                sample_with_risk_factor.append(project)
            samples_with_risk_factor[risk_factor] = sample_with_risk_factor
        return samples_with_risk_factor
    
    def make_mixed_samples_of_random_risk_factors(self, n, gate_name=None, gate_description=None, gate_predeccessors=None):
        '''
        Function is used to make samples with random risk factors instead of making n samples for each risk factor like the make_samples function.
        Cuts down on the amount of samples needed to be made, and computing time.
        '''
        risk_factors = [0.8, 1.0, 1.2, 1.4]
        dict_of_mixed_samples = {}
        samples = []
        for i in range(n):
            risk_factor = random.choice(risk_factors)
            project = Project(risk_factor)
            project.import_project_from_excel("Villa.xlsx")
            if gate_name != None and gate_description != None and gate_predeccessors != None:
                project.add_gate(gate_name, gate_description, gate_predeccessors)
            project.set_expected_duration()
            project.find_early_dates()
            project.classify_project()
            samples.append(project)
        dict_of_mixed_samples["Mixed"] = samples
        return dict_of_mixed_samples

    def write_to_csv(self, samples_with_risk_factor, filename):
        '''
        Takes in a dictionary with risk factors as keys and a list of samples as values. Randomly choose a sample from each risk factor and write it to a csv file.
        '''

        try:
            os.remove(filename)
        except OSError:
            pass
        
        amount_of_samples = len(list(samples_with_risk_factor.values())[0]) #amount_of_samples = len of first value in dict 
        index = 0
        for i in range(amount_of_samples):
            #random_risk_factor = random.choice(list(samples_with_risk_factor.keys()))
            sample = samples_with_risk_factor["Mixed"][i]
            samples_to_save = []
            tasks = []
            for task in sample.tasks[1:-1]: # Exclude the first and last task
                if task.type == "Gate":
                    index = sample.tasks.index(task)  ## This should be sent into ML 
                task_early_completion_date = task.early_completion_date
                tasks.append(task_early_completion_date)
            # Set the index as the first element in the list
            tasks.insert(0, index)
            tasks.append(sample.classification)
            samples_to_save.append(tasks)
            df = pd.DataFrame(samples_to_save)
            df.to_csv(filename, mode="a", header=False, index=False)

            








        
        


            



    def perform_statistics(self, samples_with_risk_factor):
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

        