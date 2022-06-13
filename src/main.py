from ast import Import
from gymModel import GymModel
from instance_file_reader import InstanceFileReader
from instance_generator import InstanceGenerator
from reader_generator import ReaderGenerator

if __name__ == "__main__":
    gym_model = GymModel()

    reader = InstanceFileReader()
    instance = reader.readInstanceFrom('manualInstances\\instance1.txt')

    print(instance.size)
    print(instance.exersices)
    
    #instance_gen = InstanceGenerator(gym_model)
    #print(instance_gen.generate_instance(3, 2, 2))


    #generator = ReaderGenerator('files\\', gymModel)
    #print(generator.generate(1, ['Lunges', 'PushPress', 'PushUps'], 3))