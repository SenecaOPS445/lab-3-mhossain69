#!/usr/bin/env python3

# Author ID: mhossain69


def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting


def return_number_value():
    value1 = 10
    value2 = 5
    return value1 + value2

if __name__ == '__main__':
    print('python code')
    text = return_text_value()
    print(text)
    number = return_number_value()
    print(str(number))