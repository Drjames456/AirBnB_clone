#!/usr/bin/python3
"""this module defines a function of Student data"""


def Student_data():
    """define a funtion that check the age of student"""
    name = input("Please enter valid name: ")
    lastname = input('please enter first  name: ')
    username = name[:3] + lastname[3:]
    age = input('please enter a age: ')
    age = int(age)
    if age > 30:
        print('exceed  the age to take the test!')
    elif age < 18:
        print('Too young to take the test!')
    else:
        print('Proceed to take the test!')
    print(username)


Student_data()
