import imp
from gymModel import GymModel
from random import sample, randint

class InstanceGenerator:
    def __init__(self, gymModel):
         self.gymModel = gymModel

    def generate_exercises_instance(self, number_of_trainees: int, number_of_exercise_with_spotter: int, number_of_exercise_without_spotter: int):

        exercises_list = []
        for i in range(number_of_trainees):
            exersices = sample(self.gymModel.without_spotter_exercies, 
                number_of_exercise_without_spotter)
            exersices.extend(sample(self.gymModel.with_spotter_exercies, 
                number_of_exercise_with_spotter))
            exercises_list.append(exersices)

        return exercises_list

    def generate_instance(self, number_of_trainees: int, 
            min_exercise_with_spotter: int, max_exercise_with_spotter: int, 
            min_exercise_without_spotter: int, max_exercise_without_spotter: int):
        number_of_exercise_with_spotter = randint(min_exercise_with_spotter, 
            min(len(self.gymModel.with_spotter_exercies), max_exercise_with_spotter))
        number_of_exercise_without_spotter = randint(min_exercise_without_spotter, 
            min(len(self.gymModel.without_spotter_exercies), max_exercise_without_spotter))

        return self.generate_exercises_instance(number_of_trainees, number_of_exercise_with_spotter, 
            number_of_exercise_without_spotter)




