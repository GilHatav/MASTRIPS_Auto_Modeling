
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
    )
    (:init
        (at-lobby pers1)
		(at-lobby pers2)
		(at-lobby pers3)
		(at-lobby pers4)
		(at-lobby pers5)
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

        (want pers5 mach_Lunges)
		(want pers5 mach_Back_30DegreeLatPulldown)
		(want pers5 mach_PushPress)
		(want pers5 mach_PushUps)
		(want pers5 mach_Arms_SeatedInclineDumbbellCurl)
		(want pers5 mach_Squat)
		(want pers5 mach_BenchPress)
    )
    (:goal
        (and
            (done pers5 mach_Lunges)
			(done pers5 mach_Back_30DegreeLatPulldown)
			(done pers5 mach_PushPress)
			(done pers5 mach_PushUps)
			(done pers5 mach_Arms_SeatedInclineDumbbellCurl)
			(done pers5 mach_Squat)
			(done pers5 mach_BenchPress)
        )
    )
)
        