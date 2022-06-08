(define (problem gym-training) (:domain gym-palnner)
    (:objects
        mach1 - MachineA
        mach2 - MachineD
        mach3 - MachineB
        pers1 - trainee
        pers2 - trainee 

    )
    (:init
        (at-lobby pers1)
        (at-lobby pers2)
        (want pers2 mach2)
        (free mach1)
        (free mach2)
        (free mach3)
        (free-spotter mach2)
    )
    (:goal
        (and
            (done pers2 mach2)
        )
    )
)