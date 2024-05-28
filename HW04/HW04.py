## Notes:

# CS 2316 - Spring 2023 - HW04 Numpy
# HW04: This homework is due by Sunday, February 26th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW04.py  - Your submission should be named exactly HW04.py

import numpy as np
import random

def shopping_spree(spending_limit, store_nums):
    return(np.array(((spending_limit)/store_nums)/1.07))

def serial_numbers(num_players):
    return(np.linspace(1, 100, num=num_players, dtype=int, endpoint=True))

def bath_and_body(price_arr):
    return(np.sum(price_arr) - np.max(price_arr))

def shoe_shopping(shoe_arr):
    prices = np.array(shoe_arr[1:], dtype=np.float_)
    averages = np.mean(prices, axis=0)
    smallest = np.argmin(averages)
    # index = np.argsort(smallest)
    # print(index)
    answer = str(shoe_arr[0][smallest])
    return answer

def coupons(my_list, on_sale, prices):
    return my_list[(on_sale[:len(my_list)]) & (prices[:len(my_list)] > 5.00)]

def missing_bags(week1, week2, start_day, stop_day):
    # arry = np.concatenate((week1, week2), axis=None)
    # print(arry[start_day:stop_day+1]+4)
    return np.concatenate((week1, week2), axis=None)[start_day:stop_day+1]+4

def purchases(transactions):
    return np.where((transactions[:, 1].astype(float) / transactions[:, 2].astype(float)) > 150, "Above", np.where((transactions[:, 1].astype(float) / transactions[:, 2].astype(float)) < 130, "Below","Within Range"))


def not_stealing(items):
    # DO NOT REMOVE#
    random.seed(1)

    for i in range(0, len(items)):
        if np.isnan(items[i]):
            items[i] = np.random.uniform(5, 9)
            # items[i] = (np.random.random() * (9 - 5)) + 5

    average = round(np.mean(items), 2)
    return average

if __name__ == "__main__":

    pass

    ## Question 1
    # store_nums = np.array([15, 12, 8, 3, 4, 3, 6, 5, 7, 4])
    # spending_limit = np.array([200, 500, 330, 120, 85, 60, 220, 190, 490, 300])
    # print(shopping_spree(spending_limit, store_nums))

    # store_nums = np.array([10, 14, 5, 2, 8, 1, 9, 3])
    # spending_limit = np.array([220, 400, 330, 130, 280, 50, 250, 170])
    # print(shopping_spree(spending_limit, store_nums))

    ## Question 2
    # print(serial_numbers(10))
    # print(serial_numbers(12))

    ## Question 3
    # price_arr1 = np.array([10.25, 12.5, 5.25, 29.5, 2.5], dtype = "float64")
    # print(bath_and_body(price_arr1))

    # price_arr2 = np.array([3.5, 13.35, 5.5, 13.15, 2.5, 2.5], dtype = "float64")
    # print(bath_and_body(price_arr2))

    ## Question 4
    # shoe_arr1 = np.array([["Nike", "Adidas", "New Balance"],
    #                              ["110.99", "135.99", "94.99"],
    #                              ["85.99", "150.99", "105.99"],
    #                              ["225.99", "145.99", "130.99"]])
    # print(shoe_shopping(shoe_arr1))

    # shoe_arr2 = np.array([["Converse", "Vans", "Dr. Martens", "Steve Madden"],
    #                              ["82.99", "250.99", "180.99", "109.99"],
    #                              ["99.99", "150.99", "115.99", "75.99"],
    #                              ["125.99", "115.99", "110.99", "99.99"]])
    # print(shoe_shopping(shoe_arr2))

    ## Question 5
    # on_sale = np.array([True, False, True, True, True, True, False, False, False, True, False, True, False])
    # my_list = np.array(["eggs", "2% milk", "green onions", "whole wheat bread",
    #                         "onions", "spinach", "peanut butter", "boxed spaghetti",
    #                         "salt and vinegar chips", "alfredo sauce"])
    # prices = np.array([5.13, 4.29, 1.99, 5.19, 8.99, 3.50, 6.79, 2.19, 3.49, 2.09])
    # print(coupons(my_list, on_sale, prices))

    ## Question 6
    # week1 = np.array([27, 25, 25, 24, 24, 24, 20])
    # week2 = np.array([19, 18, 14, 11, 7, 5, 4])
    # start_day = 6
    # stop_day = 13
    # print(missing_bags(week1, week2, start_day, stop_day))

    # week3 = np.array([50, 48, 47, 47, 46, 40, 36])
    # week4 = np.array([35, 30, 28, 25, 21, 16, 15])
    # start_day1 = 6
    # stop_day1 = 13
    # print(missing_bags(week3, week4, start_day1, stop_day1))

    ## Question 7
    # transactions = np.array([['01-31-2022', 5462101, 24752],
    #             ['02-28-2022', 7081547.30, 34615],
    #             ['03-31-2022', 3287654.57, 16588],
    #             ['04-30-2022', 8725851.81, 45621],
    #             ['05-31-2022', 6730748.72, 26741],
    #             ['06-30-2022', 9562745.43, 76436],
    #             ['07-31-2022', 8641735.21, 61448],
    #             ['08-31-2022', 7641748.57, 52846],
    #             ['09-30-2022', 7645277.02, 65457],
    #             ['10-31-2022', 9416274.67, 65109],
    #             ['11-30-2022', 9841378.97, 57254],
    #             ['12-31-2022', 10654298.18, 98651]])
    # print(purchases(transactions))

    ## Question 8
    # items = np.array([4.63, np.nan, 3.78, 7.12, 12.35, 7.19, np.nan, 1.50, 2.41])
    # print(not_stealing(items))

    # items = np.array([np.nan, np.nan, 6.18, np.nan, 18.42, 2.67, 9.14, np.nan, 14.32])
    # print(not_stealing(items))
