
(define (problem gym-training) (:domain gym-palnner)
    (:objects
        mach_Lunges - Lunges
		mach_PushPress - PushPress
		mach_PushUps - PushUps
		mach_PullUps - PullUps
		mach_Back:T-BarRow - Back:T-BarRow
		mach_Back:30-DegreeLatPulldown - Back:30-DegreeLatPulldown
		mach_Squat - Squat
		mach_Deadlift - Deadlift
		mach_BenchPress - BenchPress
		mach_Arms:SeatedInclineDumbbellCurl - Arms:SeatedInclineDumbbellCurl
        pers1 - trainee
		pers2 - trainee
		pers3 - trainee
    )
    (:init
        (at-lobby pers1)
		(at-lobby pers2)
		(at-lobby pers3)
        (free mach_Lunges)
		(free mach_PushPress)
		(free mach_PushUps)
		(free mach_PullUps)
		(free mach_Back:T-BarRow)
		(free mach_Back:30-DegreeLatPulldown)
		(free mach_Squat)
		(free mach_Deadlift)
		(free mach_BenchPress)
		(free mach_Arms:SeatedInclineDumbbellCurl)
        (free-spotter mach_Squat)
		(free-spotter mach_Deadlift)
		(free-spotter mach_BenchPress)
		(free-spotter mach_Arms:SeatedInclineDumbbellCurl)

        (want pers1 mach_Lunges)
		(want pers1 mach_PushPress)
		(want pers1 mach_PushUps)
    )
    (:goal
        (and
            (done pers1 mach_Lunges)
			(done pers1 mach_PushPress)
			(done pers1 mach_PushUps)
        )
    )
)
        