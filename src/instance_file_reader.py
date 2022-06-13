from instance import Instance

class InstanceFileReader:
    
    def readInstanceFrom(self, file: str):
        exersices_list = []
        with open(file, 'r') as file:
            for exersices in file:
                exersices_list.append(exersices.translate({ord(i): None for i in [' ', '\n']}).split(','))

        return Instance(exersices_list)