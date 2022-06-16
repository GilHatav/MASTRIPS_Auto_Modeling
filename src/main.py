from ast import Import
from gymModel import GymModel
from instance_file_reader import InstanceFileReader
from instance_generator import InstanceGenerator
from reader_generator import ReaderGenerator


def generate_automated(gym_model):
    instacne_name = input('Enter the instace name: ')
    number_of_traniees = int(input('Enter number of trainees: '))
    min_exercise_with_spotter = int(input('Enter min exersices with spotters: '))
    max_exercise_with_spotter = int(input('Enter max exersices with spotters: '))
    min_exercise_without_spotter = int(input('Enter min exersices without spotters: '))
    max_exercise_without_spotter = int(input('Enter max exersices without spotters: '))

    instance_gen = InstanceGenerator(gym_model)
    exercies = instance_gen.generate_instance(number_of_traniees, 
        min_exercise_with_spotter, max_exercise_with_spotter,
        min_exercise_without_spotter, max_exercise_without_spotter)
    
    generator = ReaderGenerator('files', gym_model)
    for trainee_index in range(number_of_traniees):
        generator.generate(f'{instacne_name}', trainee_index + 1, exercies[trainee_index], number_of_traniees)

def generate_manual(gym_model):
    reader = InstanceFileReader()
    instacne_path = input('Enter the instace path: ')
    instacne_name = input('Enter the instace name: ')
    instance = reader.readInstanceFrom(instacne_path)
    
    generator = ReaderGenerator('files', gym_model)
    for trainee_index in range(instance.size):
        generator.generate(f'{instacne_name}', trainee_index + 1, instance.exersices[trainee_index], instance.size)

def generate_fix_agent_diffrent_exercises():
    instance_gen = InstanceGenerator(gym_model)
    generator = ReaderGenerator('files', gym_model)
    for i in range(3, 10, 2):
        for j in range(3, 8):
            with_spotter = int(j / 2)
            without_spotter = int(j / 2)
            if int(j / 2) % 2 == 1:
                without_spotter = without_spotter + 1

            exercies = instance_gen.generate_instance(i, with_spotter, with_spotter, 
                without_spotter, without_spotter)
    

            for trainee_index in range(i):
                generator.generate(f'{i}a-{j}e', trainee_index + 1, exercies[trainee_index], i)

if __name__ == "__main__":
    gym_model = GymModel()
    
    
    ans = input('Automated or Manual?: (a/m): ')
    while True:
        if(ans == 'a'):
            generate_automated(gym_model)
            break
        elif(ans == 'm'):
            generate_manual(gym_model)
            break
        else:
            ans = input('Automated or Manual?: (a/m): ')
