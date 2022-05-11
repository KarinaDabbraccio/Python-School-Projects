# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 11:59:50 2021

@author: Karina
"""
import re
import numpy as np

def show_menu():
    """Menu options to show"""
    print('Select a Matrix Operation from the list below:')
    print('a. Addition\nb. Subtraction\nc. Matrix Multiplication')
    print('d. Element by element multiplication.')
    choice = input()
    return choice

def ask_play():
    """Get valid answer to the question, Y y for yes or N n for no"""
    invalid = True
    to_play = ''
    while invalid:
        to_play = input('Do you want to play the Matrix Game?')
        if to_play in ('Y', 'y', 'N', 'n'):
            invalid = False
        else:
            print('Invalid input, enter only "y" for yes of "n" for no.')

    return to_play

def ask_phone_zip():
    """Ask for valid phone and valid zip+4, use method match(), regex"""
    phone = input('Enter your phone number (XXX-XXX-XXXX): ')
    res_ph = re.fullmatch(r'\d{3}-\d{3}-\d{4}', phone)
    while not res_ph:
        phone = input('Your phone number is not in correct format. Please renter XXX-XXX-XXXX: ')
        res_ph = re.fullmatch(r"\d{3}-\d{3}-\d{4}", phone)
    print('Phone saved:' , phone)

    #ask zip
    zip_4 = input('Enter your zip code+4 (XXXXX-XXXX): ')
    res_z = re.fullmatch(r"\d{5}-\d{4}", zip_4)
    while not res_z:
        zip_4 = input('Your zip code+4 is not in correct format. Please renter XXXXX-XXXX: ')
        res_z = re.fullmatch(r"\d{5}-\d{4}", zip_4)
    print('Zip saved:' , zip_4)


def get_matrix(order):
    """Get 9 integers or floats, show as matrix #1 or #2
    to get each number separately:
    print('Enter your 3x3 matrix left-to-write:')
    matr = []
    for i in range (0,9):
        invalid = True
        if (i<3):
            row = '1'
        elif(i>2 and i<6):
            row = '2'
        else:
            row = '3'
        while invalid:
            try:
                numb = float(input("row " + row + ", n: "))
                matr.append(numb)
                invalid = False
            except ValueError:
                print("Invalid input. Only numbers.")"""
    # to get the whole string of numbers:
    invalid = True
    prompt = 'Enter your '+ order + ' 3x3 matrix, whitespaces between numbers:'
    while invalid:
        matr  = []
        matr_str = input(prompt).strip()
        matr_l = matr_str.split(' ')
        if len(matr_l) != 9:
            print('Your input should have 9 numbers.')
            continue
        for i in range (0, len(matr_l)):
            try:
                numb = float(matr_l[i])
                matr.append(numb)
                invalid = False
            except ValueError:
                print("Invalid input. Only numbers.")
                invalid = True
                break

    matrix = np.array(matr)
    #reshape returns a view (shallow copy) of the original array with the new dimensions.
    #It does not modify the original array
    #resize modifies the original array’s shape, np.resize(matrix, (3, 3)) - doesn't return anything
    matrix_33 = np.reshape(matrix, (3, 3))

    print('Your ', order, ' 3x3 matrix is:\n')
    #call method for print(matrix_33)
    print_nd(matrix_33)
    return matrix_33

def print_nd(arr_nd):
    """Print 2d array without [] """
    for i in arr_nd:
        for j in i:
            print(format(j, '>10.2f'), end = ' ')
        print()
    print()

def result_stats(matr):
    """transpose , the mean of the rows , and the mean of the columns for the results"""
    #The T attribute returns a transposed view (shallow copy) of the array
    print('The Transpose is:\n')
    print_nd(matr.T)
    #tr = np.transpose(matr)
    #print('The Transpose is:\n', print_nd(tr))
    #average of the column’s and row's
    print('The row and column mean values of the results are:\n')
    # f'{17.489:.2f}'
    print('Row:    ', end = ' ')
    for num in matr.mean(axis=1):
        print (format(num, '>10.2f'), end = ' ')
    print()
    print('Column: ', end = ' ')
    for num in matr.mean(axis=0):
        print (format(num, '>10.2f'), end = ' ')
    print()
    print('* ' * 30)


def main():
    """Main method"""

    do_play = ask_play()
    start = True

    while do_play in ('Y', 'y'):
        if start:
            ask_phone_zip()
            start = False
        matr_1 = get_matrix('first')
        matr_2 = get_matrix('second')
        choice = show_menu()
        while choice not in ['a', 'b', 'c', 'd']:
            choice = input("Enter again only valid menu option, lowercase:")
        # do  the user choice and get result of thechosen action
        if choice == 'a':
            act = 'Addition'
            result = np.add(matr_1, matr_2)
        elif choice == 'b':
            result = np.subtract(matr_1, matr_2)
            act = 'Subtraction'
        elif choice == 'c':
            # .dot() is also used, and for 2d arrays they should give the same result
            act = 'Multiplication'
            result = np.matmul(matr_1, matr_2)
            #result = np.dot(matr_1, matr_2)  for arrays of two different dimensions
        elif choice == 'd':
            # multiply() - when we want multiply two arrays,
            #returns the product of arr1 and arr2, element-wise
            # another way is np.array(matr_1)*np.array(matr_2)
            act = 'Element by element Multiplication'
            result = np.multiply(matr_1, matr_2)
        print('You selected', act, 'The results are:\n')
        print_nd(result)
        # do statistics for result
        result_stats(result)
        do_play = ask_play()

    print("\n*********** Thanks for playing Python Numpy ***************")

main()
