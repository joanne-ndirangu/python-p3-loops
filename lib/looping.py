#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    num = 10
    while num > 0:
        print(num)
        num -= 1
    print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    pass
    int_list = [integer * integer for integer in int_list]
    return int_list

def fizzbuzz():
    # code goes here!
    pass
    count = 1
    while count <= 100:
        if (count % 3 == 0 and count % 5 == 0):
            print("FizzBuzz")
            count += 1
        elif (count % 3 == 0):
            print("Fizz")
            count += 1
        elif (count % 5 == 0):
            print("Buzz")
            count += 1
        else:
            print(count)
            count += 1