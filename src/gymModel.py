from typing import List

class GymModel:
    def __init__(self):
        self.without_spotter_exercies: List[str] = [
            'Lunges', 'PushPress', 'PushUps', 
            'PullUps', 'Back_TBarRow', 'Back_30DegreeLatPulldown'
        ]

        self.with_spotter_exercies: List[str] = [
            'Squat', 'Deadlift', 'BenchPress',
            'Arms_SeatedInclineDumbbellCurl'
        ]