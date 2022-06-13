
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

from typing import List


class Generator:
    def __init__(self):
        self.without_spotter_exercies: List(str) = [
            'Lunges', 'PushPress', 'PushUps', 
            'PullUps', 'Back:T-BarRow', 'Back:30-DegreeLatPulldown'
        ]

        self.with_spotter_exercies: List(str) = [
            'Squat', 'Deadlift', 'BenchPress',
            'Arms:SeatedInclineDumbbellCurl'
        ]
    
    def generate(self, number_of_trainees: int):
        return self.generate_p()

    def generate_p(self, number_of_trainees: int) -> str:
        machine_objects = self.generate_machine_objects()
        trainees_objects = self.generate_persons_objects(number_of_trainees)
        
        return f'''
(define (problem gym-training) (:domain gym-palnner)
    (:objects
        {machine_objects}\n
        {trainees_objects}
    )
    (:init
        (at-lobby pers1)
        (at-lobby pers2)
        (want pers1 mach1)
        (free mach1)
        (free mach2)
        (free mach3)
        (free-spotter mach2)
    )
    (:goal
        (and
            (done pers1 mach1)
        )
    )
)
        '''

    def generate_machine_objects(self, prefix: str = '\t\t') -> str:
        machine_objects_list = []
        for machine in self.without_spotter_exercies:
            machine_objects_list.append(f'mach_{machine} - {machine}')
        for machine in self.with_spotter_exercies:
            machine_objects_list.append(f'mach_{machine} - {machine}')

        return f'\n{prefix}'.join(machine_objects_list)

    def generate_persons_objects(self, amount: int, prefix: str = '\t\t') -> str:
        return f'\n{prefix}'.join([f'pers{index} - trainee' for index in range(1, amount + 1)])

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
)
        '''
