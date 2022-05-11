# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 12:44:57 2021

@author: Karina
"""
import pandas as pd
import matplotlib.pyplot as plt


def show_menu_pop():
    """Show menu for POP and process choice in a loop"""
    print('You have entered Population Data.\nSelect the Column you want to analyze:')
    menu_pop = 'a. Pop Apr 1 \nb. Pop Jul 1 \nc. Change Pop \nd. Exit Column\t'
    choice = input(menu_pop)
    while choice != 'd':
        if choice not in ['a', 'b', 'c']:
            print("You can enter only valid menu option, a,b,c, or d")
        elif choice == 'a':
            do_stats('PopChange.csv', 'Pop Apr 1')
        elif choice == 'b':
            do_stats('PopChange.csv', 'Pop Jul 1')
        elif choice == 'c':
            do_stats('PopChange.csv', 'Change Pop')
        choice = input(menu_pop)
    print("You selected to exit the column menu\nSelect the file you want to analyze:")


def show_menu_house():
    """Show menu for HOUSING and process choice in a loop"""
    print('You have entered Housing Data.\nSelect the Column you want to analyze:')
    menu_house = 'a. AGE \nb. BEDRMS \nc. BUILT \nd. ROOMS\ne. UTILITY\nf.Exit Column\t'
    choice = input(menu_house)
    while choice != 'f':
        if choice not in ['a', 'b', 'c', 'd', 'e']:
            print("You can enter only valid menu option, a,b,c,d,e or f")
        elif choice == 'a':
            do_stats('Housing.csv', 'AGE')
        elif choice == 'b':
            do_stats('Housing.csv', 'BEDRMS')
        elif choice == 'c':
            do_stats('Housing.csv', 'BUILT')
        elif choice == 'd':
            do_stats('Housing.csv', 'ROOMS')
        elif choice == 'e':
            do_stats('Housing.csv', 'UTILITY')
        choice = input(menu_house)
    print("You selected to exit the column menu\nSelect the file you want to analyze:")


def do_stats(csv_name, column_p):
    """Do the actions with file named as first parameter, column named as second param"""
    # load file
    dfr = pd.read_csv(csv_name)

    #print(df[column_p].describe())
    #count, mean, std, minis, p_25, p_50, p_75, maxis = df[column_p].describe()
    #print(count, mean, std, minis, maxis)

    if csv_name == 'Housing.csv':
        # show standard histogram for housing, filtered and not filtered
        histog = dfr.hist(column=column_p)
        plt.show(histog)
    elif csv_name == 'PopChange.csv':
        # outliers make the Population histogram look wrong, so filter them out
        q_low = dfr[column_p].quantile(0.01)
        q_hi  = dfr[column_p].quantile(0.99)
        df_filtered = dfr[(dfr[column_p] < q_hi) & (dfr[column_p] > q_low)]
        histog_filt = df_filtered.hist(column=column_p)
        plt.show(histog_filt)

    #print only requested statistics
    print('\nYou selected',column_p, '\nThe statistics for this column are: ')
    print(f'{"Count":<7} {dfr[column_p].count():>7}')
    print(f'{"Mean":<7} {dfr[column_p].mean():>10.2f}')
    print(f'{"Std":<7} {dfr[column_p].std():>10.2f}')
    print(f'{"Min":<7} {dfr[column_p].min():>7}')
    if not column_p == 'UTILITY':
        print(f'{"Max":<7} {dfr[column_p].max():>7}')
    else:
        print(f'{"Max":<7} {dfr[column_p].max():>10.2f}')

def main():
    """Show menu and process choice in a loop"""
    print('***************** Welcome to the Python Data Analysis App**********')
    print('Select the file you want to analyze:')
    menu_main = '1. Population Data\n2. Housing Data\n3. Exit the Program\t'
    choice = input(menu_main)
    while choice != '3':
        if choice not in ['1', '2', '3']:
            print("You can enter only valid menu option, 1, 2, or 3")
        elif choice == '1':
            show_menu_pop()
        elif choice == '2':
            show_menu_house()
        choice = input(menu_main)

    print("*************** Thanks for using the Data Analysis App**********")

main()
