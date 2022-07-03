
(define (problem gym-training) (:domain gym-palnner)
    (:objects
        mach_Lunges - Lunges
		mach_PushPress - PushPress
		mach_PushUps - PushUps
		mach_PullUps - PullUps
		mach_Back_TBarRow - Back_TBarRow
		mach_Back_30DegreeLatPulldown - Back_30DegreeLatPulldown
		mach_Squat - Squat
		mach_Deadlift - Deadlift
		mach_BenchPress - BenchPress
		mach_Arms_SeatedInclineDumbbellCurl - Arms_SeatedInclineDumbbellCurl
        pers1 - trainee
		pers2 - trainee
		pers3 - trainee
		pers4 - trainee
		pers5 - trainee
		pers6 - trainee
		pers7 - trainee
		pers8 - trainee
		pers9 - trainee
    )
    (:init
        (at-lobby pers1)
		(at-lobby pers2)
		(at-lobby pers3)
		(at-lobby pers4)
		(at-lobby pers5)
		(at-lobby pers6)
		(at-lobby pers7)
		(at-lobby pers8)
		(at-lobby pers9)
        (free mach_Lunges)
		(free mach_PushPress)
		(free mach_PushUps)
		(free mach_PullUps)
		(free mach_Back_TBarRow)
		(free mach_Back_30DegreeLatPulldown)
		(free mach_Squat)
		(free mach_Deadlift)
		(free mach_BenchPress)
		(free mach_Arms_SeatedInclineDumbbellCurl)
        (free-spotter mach_Squat)
		(free-spotter mach_Deadlift)
		(free-spotter mach_BenchPress)
		(free-spotter mach_Arms_SeatedInclineDumbbellCurl)

        (want pers3 mach_Lunges)
		(want pers3 mach_PullUps)
		(want pers3 mach_Back_30DegreeLatPulldown)
		(want pers3 mach_PushPress)
		(want pers3 mach_Deadlift)
		(want pers3 mach_BenchPress)
		(want pers3 mach_Squat)
    )
    (:goal
        (and
            (done pers3 mach_Lunges)
			(done pers3 mach_PullUps)
			(done pers3 mach_Back_30DegreeLatPulldown)
			(done pers3 mach_PushPress)
			(done pers3 mach_Deadlift)
			(done pers3 mach_BenchPress)
			(done pers3 mach_Squat)
        )
    )
)
        