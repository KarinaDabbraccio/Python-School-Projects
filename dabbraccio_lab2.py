# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 19:30:01 2021

@author: Karina
"""
import string
import secrets
import math
import datetime

def show_menu():
    """Menu options to show"""
    print('\na. Generate Secure Password')
    print('b. Calculate and Format a Percentage')
    print('c. How many days from today until July 4, 2025?')
    print('d. Use the Law of Cosines to calculate the leg of a triangle. ')
    print('e. Calculate the volume of a Right Circular Cylinder')
    print('f. Exit program')

def password_gener():
    """Generate Secure Password"""
    #accept input

    try:
        p_len = int(input('\nHow long password should be between 4 and 64 characters:  '))
    except ValueError:
        print("Invalid input. Only numbers allowed Operation cancellled.")
        return
    if p_len in range(4, 65):
        print('By default, password will include lowercase letters only.')
        p_let = input('For lower + uppercase press 1, only uppercase press 2, default - any key:  ')
        if not p_let == "1" and not p_let == "2":
            p_let = "3"
        p_dig = input('To include digits press 1, not include press other key:   ')
        p_sym = input('To include symbols press 1, not include press other key:  ')
    else:
        print("Invalid password length. Cannot perform this operaton")
        return
    #specify what password should include

    # lower and uppercase
    # and digits
    if p_let == "1" and p_dig == "1":
        characters = string.ascii_letters + string.digits
        if p_sym == "1":
            characters = string.ascii_letters + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(characters) for i in range(p_len))
            if (any(c.islower() for c in password) and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
                break

    # lower and uppercase
    # and no digits
    elif p_let =="1" and not p_dig == "1":
        characters = string.ascii_letters
        if p_sym == "1": # p_dig != "1" if here
            characters = string.ascii_letters + string.punctuation
        while True:
            password = ''.join(secrets.choice(characters) for i in range(p_len))
            if (any(c.islower() for c in password) and any(c.isupper() for c in password)):
                break

    #only lowercase
    # and digit
    elif p_let =="3" and p_dig == "1":
        characters = string.ascii_lowercase + string.digits
        if p_sym == "1":
            characters = string.ascii_lowercase + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(characters) for i in range(p_len))
            if (any(c.islower() for c in password) and any(c.isdigit() for c in password)):
                break

    # lowercase
    # and no digits
    elif p_let =="3" and not p_dig == "1":
        characters = string.ascii_lowercase
        if p_sym == "1":
            characters = string.ascii_lowercase + string.punctuation
        password = ''.join(secrets.choice(characters) for i in range(p_len))

    #only uppercase
    # and digit
    elif p_let =="2" and p_dig == "1":
        characters = string.ascii_uppercase + string.digits
        if p_sym == "1":
            characters = string.ascii_uppercase + string.digits + string.punctuation
        while True:
            password = ''.join(secrets.choice(characters) for i in range(p_len))
            if (any(c.isupper() for c in password) and any(c.isdigit() for c in password)):
                break

    # uppercase
    # and no digits
    elif p_let =="2" and not p_dig == "1":
        characters = string.ascii_uppercase
        if p_sym == "1":
            characters = string.ascii_uppercase + string.punctuation
        password = ''.join(secrets.choice(characters) for i in range(p_len))

    print('Your password of length ' + str(p_len) + ' is:\n\n' + password)



def percentage():
    """Calculate and Format a Percentage"""
    print('Enter only positive numbers. integers for decimal points')
    try:
        numer = float(input("Enter the numerator:     "))
        denom = float(input("Enter denominator:       "))
        if denom <= 0 or numer < 0:
            print("Only positive numbers. Denominator cannot be 0. Operation cancelled.")
            return
        dec_p = int(input("How many decimal points: "))
    except ValueError:
        print("Invalid input. Only numbers allowed. Operation cancellled.")
        return
    res = 100 * numer / denom
    round_res = round(res, dec_p)
    print("Result:     ", round_res)

def days_count():
    """How many days from today until July 4, 2025?"""
    print('c. How many days from today until July 4, 2025?')
    today = datetime.date.today()
    future = datetime.date(2025, 7, 4)
    #future = datetime.date(2021, 6, 21)
    count_days = (future - today).days
    print('From today, ', today, ' to July,4, 2025 is', count_days, 'days.')


def leg_triangle():
    """Use the Law of Cosines to calculate the leg of a triangle.
    Input is two lengths of sides and value of angle
    C^2 = a^2 + b^2 - 2ab * cos_C"""
    print('d. Use the Law of Cosines to calculate the leg of a triangle. ')
    try:
        side_a = float(input('Enter positive value of side a: '))
        side_b = float(input('Enter positive value of side b: '))
        angle = float(input('Enter positive value of angle between a nd b in degrees:  '))
    except ValueError:
        print("Invalid input. Only numbers allowed. Operation cancellled.")
        return
    # positive, sum of triangle angles is 180, so angle must be less
    if side_a <= 0 or side_b <= 0 or angle >= 180 or angle <= 0:
        print("Invalid input values. Only positive numbers , 0 < angle < 180. Operation cancelled.")
        return
    #calculate
    # math.cos returns cos of x in radians, so transform to radians
    ang_rad = math.radians(angle)
    side_csq = side_a ** 2 + side_b ** 2 - 2 * side_a * side_b * math.cos(ang_rad)
    side_c = math.sqrt(side_csq)
    #round answer to two decimal points
    side_c_round = round(side_c, 2)
    print('The third side c is ', side_c_round)

def cylinder_volume():
    """Calculate the volume of a Right Circular Cylinder, formula is:
    vol = pi * r^2 * h"""
    print('e. Calculate the volume of a Right Circular Cylinder')
    try:
        radius = float(input('Enter positive value of radius: '))
        height = float(input('Enter positive value of height: '))
    except ValueError:
        print("Invalid input. Only numbers allowed. Operation cancellled.")
        return
    # positive
    if radius <= 0 or height <= 0:
        print("Invalid input values. Only positive numbers. Operation cancelled.")
        return
    #calculate, round to two decimal points
    vol = math.pi * radius ** 2 * height
    vol_round = round(vol, 2)
    print('The volume of the cylinder is ', vol_round)

def main():
    """Show menu and process choice in a loop"""
    show_menu()
    choice = input('Enter your choice from the menu, letter: ')
    while choice != 'f':
        if choice not in ['a', 'b', 'c', 'd', 'e']:
            print("You can enter only valid menu option, lowercase")
        elif choice == 'a':
            password_gener()
        elif choice == 'b':
            percentage()
        elif choice == 'c':
            days_count()
        elif choice == 'd':
            leg_triangle()
        elif choice == 'e':
            cylinder_volume()
        show_menu()
        choice = input('Enter your choice, letter: ')

    print("Thank you for using the program. Goodbye!")

main()
