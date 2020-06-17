"""
name : Yeh Fu
stud ID 30838932
Date the script was created : 30/5/20
Last edited : 7/6/20
This file is a part of pandemic simulation task.
There are class Patient and functions that
reading data from txt file and performing the simulation of pandemic spread
"""


from pandemic_simulation1 import *
import random


class Patient(Person):
    """class Patient stores the data of one single patient"""

    def __init__(self, first_name, last_name, health):
        """initialise the fields"""
        super().__init__(first_name, last_name)
        self.health = health

    def get_health(self):
        """get the health point of a single patient"""
        return self.health

    def set_health(self, new_health):
        """set the health point for a single patient"""
        self.health = new_health

    def increase_health(self, amount):
        """method for increasing health point"""
        self.set_health(self.get_health() + amount)
        # the ceiling of health point is 100
        if self.get_health() > 100:
            self.set_health(100)

    def is_contagious(self):
        """
        check if the patient is contagious
        return boolean, True means contagious, False means not
        """
        if round(self.health, 0) < 50:
            return True
        else:
            return False

    def infect(self, viral_load):
        """
        performing the process of infection
        for different level of health point
        adjust the effect of viral_load
        """
        if self.get_health() <= 29:
            self.reduce_health(0.1 * viral_load)

        elif 29 < self.get_health() < 50:
            self.reduce_health(viral_load)

        elif self.get_health() >= 50:
            self.reduce_health(2 * viral_load)

        # make the minimum health point 0
        if self.get_health() < 0:
            self.set_health(0)

    def reduce_health(self, amount):
        """method for reducing health point"""
        self.set_health(self.get_health() - amount)
        # the floor for health point is 0
        if self.get_health() < 0:
            self.set_health(0)

    def sleep(self):
        """sleep to recover health points"""
        if self.get_health() < 96:
            self.increase_health(5)

        # make the maximum of health point 100
        else:
            self.set_health(100)

    def __str__(self):
        """method for printing out a patient object"""
        return self.get_first_name() + " " + self.get_last_name() + " " + str(self.get_health())


def run_simulation(days, meeting_probability, patient_zero_health):
    """demonstrate the whole process of pandemic simulation"""
    patients = load_patients(75)

    # empty the total_contagious to make sure we append the data from the index of 0
    total_contagious = []

    # retrieve the first patient and set the health point for that patient
    first_patient = patients[0]
    first_patient.set_health(patient_zero_health)

    # loop for each day of simulation
    for day in range(0, days):
        # for the start of everyday, make the contagious people 0
        # so we can start counting from 0
        day_contagious = 0

        # on each day, simulate every meeting between patient and their friends
        for man in patients:
            # calculate each patient's viral_load
            viral_load = 5 + ((man.get_health() - 25) ** 2) / 62
            # get patient's friend array
            friends = man.get_friends()

            # for each patient's friend
            # simulate the meeting with the specific probability
            for friend in friends:
                # calculate each friend's viral_load
                viral_load_friend = 5 + ((friend.get_health() - 25) ** 2) / 62
                # generate a random number from 0(inclusive) to 1(exclusive)
                r = random.uniform(0, 1)

                # the 0 is inclusive for r
                # so not include the ceiling of r
                # first situation is both friend and man are contagious
                if meeting_probability > r and man.is_contagious() and friend.is_contagious():
                    man.infect(viral_load_friend)
                    friend.infect(viral_load)
                # second situation is only the man is contagious
                elif meeting_probability > r and man.is_contagious():
                    friend.infect(viral_load)
                # third situation is only the friend is contagious
                elif meeting_probability > r and friend.is_contagious():
                    man.infect(viral_load_friend)

        # after simulating all of the meetings
        # check the total contagious people and let each person sleep after checking
        for man in patients:
            if man.is_contagious():
                day_contagious += 1
            man.sleep()
        # append the data of today's total contagious people
        total_contagious.append(day_contagious)

    return total_contagious


def load_patients(initial_health):
    """
    load patients from txt file
    the process is similar to load_people() method in a2_30838932_task1.py
    the difference is that we add another variable in Patient that is health
    refer to 'a2_30838932_task1.py - load_people()' for more information
    """
    f = open("a2_sample_set.txt", "r")
    f1 = f.readlines()

    patients = []

    for line in f1:
        line_split_list = line.split(":")
        patient_split_list = line_split_list[0].split()
        one_patient = Patient(patient_split_list[0], patient_split_list[1], initial_health)
        patients.append(one_patient)

    cur_index = 0
    for line in f1:
        line_split_list = line.split(":")
        all_patient_split_list = line_split_list[1].split(",")

        for patient_name in all_patient_split_list:
            single_patient_split_list = patient_name.split()
            name = single_patient_split_list[0].strip() + single_patient_split_list[1].strip()

            for patient in patients:
                if patient.get_name() == name:
                    patients[cur_index].add_friend(patient)
                    break
        cur_index += 1
    f.close()
    return patients


if __name__ == '__main__':
    load_patients(75)
    test_result = run_simulation(15, 0.8, 49)
    print(test_result)

    load_patients(75)
    test_result = run_simulation(40, 1, 1)
    print(test_result)
