
(define (domain gym-palnner)
    (:requirements :factored-privacy :typing) 

    (:types
        person - trainee 
        machineWithSpotter machineWithoutSpotter - machine
        Lunges PushPress PushUps PullUps Back:T-BarRow Back:30-DegreeLatPulldown - machineWithoutSpotter
        Squat Deadlift BenchPress Arms:SeatedInclineDumbbellCurl - machineWithSpotter
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