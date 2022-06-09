from typing import List
from typing import Callable

'''
Exercises are taken form: https://www.muscleandfitness.com/
1. Lunges 
2. Squat
3. Push Press
4. Push Ups
5. Pull Ups
6. Deadlift
7. Bench Press
8. Back: T-Bar Row
9. Back: 30-Degree Lat Pulldown
10. Arms: Seated Incline Dumbbell Curl
'''

class ReaderGenerator:
    def __init__(self, pathPrefix: str):
        self.pathPrefix = pathPrefix
        self.without_spotter_exercies: List[str] = [
            'Lunges', 'PushPress', 'PushUps', 
            'PullUps', 'Back:T-BarRow', 'Back:30-DegreeLatPulldown'
        ]

        self.with_spotter_exercies: List[str] = [
            'Squat', 'Deadlift', 'BenchPress',
            'Arms:SeatedInclineDumbbellCurl'
        ]
    
    def generate(self, want_machines: List[str], number_of_trainees: int):
        for trainee_index in range(1, number_of_trainees + 1):
            with open(f'{self.pathPrefix}trainee{trainee_index}-problem.pddl', "w") as file:
                file.write(self.generate_problem(trainee_index, want_machines, number_of_trainees))
            
            with open(f'{self.pathPrefix}trainee{trainee_index}-domain.pddl', "w") as file:
                file.write(self.generate_domain())

    def generate_problem(self, trainee_index: int, want_machines: List[str], number_of_trainees: int) -> str:
        machine_objects = self.generate_machine_objects(lambda machine: f'{self._machine_object_name(machine)} - {machine}')
        free_machines = self.generate_machine_objects(lambda machine: f'(free {self._machine_object_name(machine)})')
        free_machines_spotters = self.generate_machine_objects(
            lambda machine: f'(free-spotter {self._machine_object_name(machine)})', 
            include_without_spotters=False)


        trainees_objects = self.generate_persons_objects(number_of_trainees, lambda index:  f'{self._person_object_name(index)} - trainee')
        at_lobby = self.generate_persons_objects(number_of_trainees, lambda index:  f'(at-lobby {self._person_object_name(index)})')
        
        want_machines_predicate = '\n\t\t'.join([f'(want {self._person_object_name(trainee_index)} {self._machine_object_name(machine)})' for machine in want_machines])
        done_machines_predicate = '\n\t\t\t'.join([f'(done {self._person_object_name(trainee_index)} {self._machine_object_name(machine)})' for machine in want_machines])

        return f'''
(define (problem gym-training) (:domain gym-palnner)
    (:objects
        {machine_objects}
        {trainees_objects}
    )
    (:init
        {at_lobby}
        {free_machines}
        {free_machines_spotters}

        {want_machines_predicate}
    )
    (:goal
        (and
            {done_machines_predicate}
        )
    )
)
        '''

    def generate_machine_objects(self, rule_creator: Callable[[str], str], 
        include_without_spotters = True, include_with_spotter = True,
        prefix: str = '\t\t') -> str:

        machine_objects_list = []
        if include_without_spotters:
            for machine in self.without_spotter_exercies:
                machine_objects_list.append(rule_creator(machine))
        if include_with_spotter:
            for machine in self.with_spotter_exercies:
                machine_objects_list.append(rule_creator(machine))

        return f'\n{prefix}'.join(machine_objects_list)

    def generate_persons_objects(self, amount: int, rule_creator: Callable[[int], str], prefix: str = '\t\t') -> str:
        return f'\n{prefix}'.join([rule_creator(index) for index in range(1, amount + 1)])

    def generate_domain(self) -> str:
        return f'''
(define (domain gym-palnner)
    (:requirements :factored-privacy :typing) 

    (:types
        person - trainee 
        machineWithSpotter machineWithoutSpotter - machine
        {" ".join(self.without_spotter_exercies)} - machineWithoutSpotter
        {" ".join(self.with_spotter_exercies)} - machineWithSpotter
    )

    (:predicates
        (at-lobby ?person - trainee)
        (at-machine-as-trainee ?person - trainee ?mach - machine)
        (at-machine-as-spotter ?person - trainee ?mach - machineWithSpotter)
        (free ?mach - machine)
        (free-spotter ?mach - machineWithSpotter)

        (:private
            (want ?person - trainee ?mach - machine)
            (done ?person - trainee ?mach - machine)
        )
    )

    (:action lobby-to-machine
        :parameters (?person - trainee ?mach - machine)
        :precondition (and
            (free ?mach)
            (at-lobby ?person)
            (want ?person ?mach)
        )
        :effect (and
            (at-machine-as-trainee ?person ?mach)
            (not (free ?mach))
            (not (at-lobby ?person))
        )
    )

    (:action move-machine-to-lobby
        :parameters (?person - trainee ?mach - machine)
        :precondition (and
            (at-machine-as-trainee ?person ?mach)
        )
        :effect (and
            (at-lobby ?person)
            (free ?mach)
            (not (at-machine-as-trainee ?person ?mach))
        )
    )

    (:action lobby-to-spotter-at-machine
        :parameters (?spotter - trainee ?mach - machineWithSpotter)
        :precondition (and
            (at-lobby ?spotter)
            (free-spotter ?mach)
        )
        :effect (and
            (at-machine-as-spotter ?spotter ?mach)
            (not (free-spotter ?mach))
            (not (at-lobby ?spotter))
        )
    )

    (:action move-spotter-machine-to-lobby
        :parameters (?spotter - trainee ?mach - machineWithSpotter)
        :precondition (and
            (at-machine-as-spotter ?spotter ?mach)
        )
        :effect (and
            (at-lobby ?spotter)
            (free-spotter ?mach)
            (not (at-machine-as-spotter ?spotter ?mach))
        )
    )

    (:action train-at-machine-without-spotter
        :parameters (?person - trainee ?mach - machineWithoutSpotter)
        :precondition (and
            (at-machine-as-trainee ?person ?mach)
            (want ?person ?mach)
        )
        :effect (and
            (done ?person ?mach)
            (not (want ?person ?mach))
        )
    )

    (:action train-at-machine-with-spotter
        :parameters (?person - trainee ?spotter - trainee ?mach - machineWithSpotter)
        :precondition (and
            (at-machine-as-trainee ?person ?mach)
            (at-machine-as-spotter ?spotter ?mach)
            (want ?person ?mach)
        )
        :effect (and
            (done ?person ?mach)
            (not (want ?person ?mach))
        )
    )
)'''

    def _person_object_name(self, index: int):
        return f'pers{index}'

    def _machine_object_name(self, machine: str):
        return f'mach_{machine}'


