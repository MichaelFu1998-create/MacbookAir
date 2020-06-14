"""
name : Yeh Fu
stud ID 30838932
Date the script was created : 30/5/20
Last edited : 7/6/20
This file is a part of pandemic simulation task.
There are class Person and function for reading data from txt file
"""


class Person:
    """class Person stores the data of one single Person"""

    def __init__(self, first_name, last_name):
        """initialise the fields of Person object"""
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []

    def add_friend(self, friend_person):
        """append a friend to Person's friend array"""
        self.friends.append(friend_person)

    def get_first_name(self):
        """get Person's first name"""
        return self.first_name

    def get_last_name(self):
        """get Person's last name"""
        return self.last_name

    def get_name(self):
        """get Person's full name"""
        return self.first_name + self.last_name

    def get_friends(self):
        """get Person's friend list"""
        return self.friends

    def __str__(self):
        """print Person object"""
        return self.get_first_name() + " " + self.get_last_name()


def load_people():
    """load each person and their friends from txt file"""
    f = open("a2_sample_set.txt", "r")
    # read txt file line by line
    f1 = f.readlines()
    # array for storing Person object
    people = []

    for line in f1:
        # for each line in txt file
        # split the line by ":" to get the full name of one Person
        line_split_list = line.split(":")
        # split the full name by " " to get the first name and last name
        person_split_list = line_split_list[0].split()
        # use first name and last name to create a Person then append to the people array
        person = Person(person_split_list[0], person_split_list[1])
        people.append(person)

    # index for the iterating people array
    cur_index = 0
    for line in f1:
        # split the line by ":" and get each person's friend array
        # split each friend by ","
        line_split_list = line.split(":")
        all_friend_split_list = line_split_list[1].split(",")

        # for each friend in a Person's friend array
        for friend_name in all_friend_split_list:
            # get the full name of one friend and
            # strip to make sure there is no blank character
            single_friend_split_list = friend_name.split()
            name = single_friend_split_list[0].strip() + single_friend_split_list[1].strip()

            # iterate people array
            for person in people:
                # compare name to find the correct reference of a single friend
                if person.get_name() == name:
                    # when finding out the correct ref.
                    # use add_friend to append that friend
                    people[cur_index].add_friend(person)
                    break
        # at the end of iterator
        # +1 to cur_index,
        # so we can add friend for the next person in the people array when moving to the next line
        cur_index += 1

    f.close()


if __name__ == '__main__':
    load_people()

