"""
name : Yeh Fu
stud ID 30838932
Date the script was created : 30/5/20
Last edited : 7/6/20
This file is a part of pandemic simulation task.
There is only one function visual_curve which would draw a pandemic line chart
Scenario_A : match prediction - the patient0's health point is really low
Scenario_B : match prediction - the trend is more unpredictable because patient0's health point
                                and meeting probability are close to medium value
Scenario_C : match prediction - pandemic would probably die out due to low meeting probability
"""


from a2_30838932_task2 import *
from matplotlib import pyplot as plt
import numpy as np


def visual_curve(days, meeting_probability, patient_zero_health):
    """visualisation the data of simulation using np and plt"""
    # create patient data for simulation
    load_patients(75)
    # get the data of daily contagious from run_simulation
    num_of_contagious = run_simulation(days, meeting_probability, patient_zero_health)

    # starts from day 0 to day (days - 1)
    # create a nd-array object straightly
    x = np.arange(days)
    # transfer list to a 1D np array
    y = np.array(num_of_contagious)

    plt.plot(x, y)

    # give a title for the graph and name the axis x and axis y
    plt.title("pandemic trend")
    plt.xlabel("day")
    plt.ylabel("number of contagious people")

    # Get Current Axes and give a legend for the trend line
    plt.gca().legend(['variation trend'])
    # show the graph
    plt.show()


if __name__ == '__main__':
    visual_curve(30, 0.6, 25)
    visual_curve(60, 0.25, 49)
    visual_curve(90, 0.18, 40)

