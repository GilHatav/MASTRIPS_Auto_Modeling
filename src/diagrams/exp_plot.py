import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
import sympy


"""
create a function to fit with your data. a, b, c and d are the coefficients
that curve_fit will calculate for you. 
In this part you need to guess and/or use mathematical knowledge to find
a function that resembles your data
"""
def func(x, a, b, c, d):
    return a*(b**(c*x)) + d 

def func_linear(x, a, b):
    return a*x +b  

def plot_exp(data):

    """
    Generate some data, let's imagine that you already have this. 
    """
    x = list(data.keys())
    y = list(data.values())
  
    """
    Plot your data
    """
    plt.plot(x, y, 'ro',label="Original Data")

    """
    brutal force to avoid errors
    """    
    x = np.array(x, dtype=float) #transform your data in a numpy array of floats 
    y = np.array(y, dtype=float) #so the curve_fit can work


    """
    make the curve_fit
    """
    popt, pcov = curve_fit(func, x, y)


    """
    Print the coefficients and plot the funcion.
    """

    x_sample = np.linspace(min(x), max(x),50)
    # plt.plot(x, func(x_sample, *popt), label="Fitted Curve") #same as line above \/
    plt.plot(x_sample, popt[0]*popt[1]**(popt[2]*x_sample) + popt[3]  , label="Fitted Curve") 

    plt.legend(loc='upper left')
    plt.show()
    
def plot_linear(data):

    """
    Generate some data, let's imagine that you already have this. 
    """
    x = list(data.keys())
    y = list(data.values())
  
    """
    Plot your data
    """
    plt.plot(x, y, 'ro',label="Original Data")

    """
    brutal force to avoid errors
    """    
    x = np.array(x, dtype=float) #transform your data in a numpy array of floats 
    y = np.array(y, dtype=float) #so the curve_fit can work


    """
    make the curve_fit
    """
    popt, pcov = curve_fit(func_linear, x, y)


    """
    Print the coefficients and plot the funcion.
    """

    x_sample = np.linspace(min(x), max(x),50)
    # plt.plot(x, func(x_sample, *popt), label="Fitted Curve") #same as line above \/
    plt.plot(x_sample, popt[0]*x_sample + popt[1]  , label="Fitted Curve") 
    plt.legend(loc='upper left')
    plt.show()


def fixed_2_agents():
    data_makespan = {2:10, 3:16, 4:22, 5:28, 6:34}
    data_time = {2:0.5042762, 3:0.6123672, 4:0.8033596, 5:0.9235658, 6:1.1943377}
    plot_linear(data_makespan)
    plot_linear(data_time)

def fixed_2_agents_c():
    data_makespan = {0:0 ,2:18 , 3:28 , 4:38 }
    data_time = {0:0, 2:0.7021268 , 3:0.8936109 , 4:1.6702687 }
    plot_exp(data_makespan)
    plot_exp(data_time)

def fixed_3_agents():
    data_makespan = {2:16, 3:24, 4:33, 5:42, 6:52}
    data_time = {2:1.3664788, 3:1.8800073, 4:3.0058173, 5:5.089197, 6:5.7911757}
    plot_exp(data_makespan)
    plot_exp(data_time)

def fixed_3_agents_c():
    data_makespan = {0:0, 2:27, 3:42, 4:57}
    data_time = {0:0, 2:3.1405821, 3:5.7971867, 4:12.0838632}
    plot_exp(data_makespan)
    plot_exp(data_time)
    
def fixed_4_agents():
    data_makespan = {2:21, 3:33, 4:46, 5:57, 6:69}
    data_time = {2:3.8316908, 3:7.5344777, 4:21.6450441, 5:22.5030575, 6:35.3324963}
    plot_linear(data_makespan)
    plot_exp(data_time)

def fixed_4_agents_c():
    data_makespan = {0:0, 2:36 , 3:56 ,4:80}
    data_time = {0:0, 2:22.2027794, 3:97.9863251, 4:292.9357663}
    plot_exp(data_makespan)
    plot_exp(data_time)

def fixed_5_agents():
    data_makespan = {2:27, 3:41, 4:58, 5:72, 6:87}
    data_time = {2:13.0860307, 3:34.426766, 4:113.8670589, 5:172.8753762, 6:340.1845551}
    plot_linear(data_makespan)
    plot_exp(data_time)

def fixed_5_agents_c():
    data_makespan = {0:0, 2:51}
    data_time = {0:0, 2:702.4899893}
    plot_exp(data_makespan)
    plot_exp(data_time)
    
def fixed_4_Exercises():
    data_makespan = {2:22, 3:33, 4:46, 5:58}
    data_time = {2:0.8033596, 3:3.0058173, 4:21.6450441, 5:113.8670589}
    plot_exp(data_makespan)
    plot_exp(data_time)

def fixed_4_Exercises_c():
    data_makespan = {0:0, 2:38 , 3:57 ,4:80}
    data_time = {0:0, 2:1.6702687, 3:12.0838632, 4:292.9357663}
    plot_exp(data_makespan)
    plot_exp(data_time)
    
    
    
fixed_4_Exercises_c()
    



