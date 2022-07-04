from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import curve_fit



def draw(makespanMap, makespanTitle,
    timeMap, timeTitle, xlabelTime):
    plt.figure()
    plt.subplot(211)
    plt.plot(makespanMap.keys(), makespanMap.values(), '--go')
    plt.title(makespanTitle)
    plt.xlabel(xlabelTime)
    plt.ylabel("Makespan")
    plt.grid(True)

    x = np.array(list(timeMap.keys()))
    y = np.array(list(timeMap.values()))

    cubic_interploation_model = interp1d(x, y, kind = 'cubic')
    X_ = np.linspace(x.min(), x.max(), 500)
    Y_ = cubic_interploation_model(X_)

    plt.subplot(212)
    plt.plot(x, y, 'bo', X_, Y_)
    plt.title(timeTitle)
    plt.xlabel(xlabelTime)
    plt.ylabel("Time")
    plt.grid(True)

    plt.show()



def draw_fixed_two_agents():
    resultsMapMakespan = {
        3: 16,
        4: 25,
        5: 30,
        6: 38,
        7: 43,
        9: 57,
    }

    resultsMapTime = {
        3: 0.6672246,
        4: 0.7568155,
        5: 0.8586657,
        6: 1.2440352,
        7: 1.8903971,
        9: 10.1559886,
    }

    draw(resultsMapMakespan, "Two agents", 
        resultsMapTime, "Two agents", "Number of exercises")

def draw_fixed_three_agents():
    resultsMapMakespan = {
        3: 22,
        4: 32,
        5: 34,
        6: 58,
        7: 58,
    }

    resultsMapTime = {
        3: 1.1541094,
        4: 1.4878105,
        5: 1.7315172,
        6: 6.3938031,
        7: 6.8994105,
    }

    draw(resultsMapMakespan, "Three agents", 
        resultsMapTime, "Three agents", "Number of exercises")

def draw_fixed_five_agents():
    resultsMapMakespan = {
        3: 31,
        4: 54,
        5: 59,
        6: 88,
        7: 90,
    }

    resultsMapTime = {
        3: 6.2338869,
        4: 21.2167338,
        5: 30.3580281,
        6: 99.9407701,
        7: 107.0912424,
    }

    draw(resultsMapMakespan, "Five agents", 
        resultsMapTime, "Five agents", "Number of exercises")

def draw_fixed_seven_agents():
    resultsMapMakespan = {
        3: 39,
        4: 68,
    }

    resultsMapTime = {
        3: 43.3101182,
        4: 630.5213756,
    }

    draw(resultsMapMakespan, "Seven agents", 
        resultsMapTime, "Seven agents", "Number of exercises")

def draw_fixed_five_exercies():
    resultsMapMakespan = {
        2: 30,
        3: 40,
        5: 62,
        6: 72,
    }

    resultsMapTime = {
        2: 1.8257663,
        3: 6.4052009,
        5: 49.6501829,
        6: 159.7054054,
    }

    draw(resultsMapMakespan, "Five exercises", 
        resultsMapTime, "Five exercises", "Number of agents")

if __name__ == "__main__":
    draw_fixed_five_exercies()
