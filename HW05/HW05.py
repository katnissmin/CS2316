import pandas as pd
from pprint import pprint

## NOTES:

# CS 2316 - Spring 2023 - HW05 Pandas
# HW05: This homework is due by Sunday, March 5th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW05.py  - Your submission should be named exactly HW05.py
#   - Print your variables as you code in order to see what values they have
#     especially for questions with API and BeautifulSoup

###################################################
###################################################
"""
DATA CLEANING SECTION
"""
###################################################
###################################################

# Question 1
def merge_columns(michelin_guide):
    columns = ['Cuisine_type_1', 'Cuisine_type_2']
    michelin_guide['Cuisine_type_1'].fillna(michelin_guide['Cuisine_type_2'], inplace=True)
    michelin_guide["Cuisine Type"] = michelin_guide['Cuisine_type_1']
    michelin_guide.drop(columns, axis = 1, inplace=True)
    return michelin_guide
    # df.to_csv(michelin_guide, index = False)


# Question 2
def price_cleaning(michelin_guide):
    # Find the average number of dollar signs in each of the cells
    dollar = round(michelin_guide["Price"].str.len().mean())

    # Then, cast the average number to an integer and multiply it by the dollar sign
    dollar_sign = int(dollar) * "$"

    # Fill in any NaN values in the column with the value found
    michelin_guide["Price"].fillna(dollar_sign, inplace=True)
    return michelin_guide


# Question 3
def write_to_file(michelin_guide, output_file, sheet):
    michelin_guide.to_excel(output_file, sheet_name = sheet, index = False)


###################################################
###################################################
"""
DATA ANALYSIS SECTION
"""
###################################################
###################################################


# Question 4
def types_by_country(michelin_guide):
    return michelin_guide.groupby(["Country", "Cuisine Type"]).agg({'Restaurant Name': 'count'})


# Question 5
def best_cities(michelin_guide, country, cuisine_type):
    maxstars = michelin_guide.loc[(michelin_guide["Country"]==country) & (michelin_guide["Cuisine Type"]==cuisine_type), "Number of Stars"].max()
    numcities = michelin_guide.loc[(michelin_guide["Country"]==country) & (michelin_guide["Cuisine Type"]==cuisine_type) & (michelin_guide["Number of Stars"] ==maxstars), "City"].nunique() 
    return numcities

# Question 6
def food_budget(michelin_guide, price_threshold, city):
    cleaned = michelin_guide.loc[(michelin_guide["Price"].str.len()<=len(price_threshold)) & (michelin_guide["City"]==city)]
    restaurants = cleaned.groupby("Cuisine Type").agg({"Restaurant Name": "count"})
    return restaurants


# Question 7
def ranking_restaurants(michelin_guide, cuisine_type, price):
    all_restaurants = michelin_guide.loc[(michelin_guide["Cuisine Type"]==cuisine_type) & (michelin_guide["Price"]==price)]
    semifinal = all_restaurants.sort_values(["Number of Stars", "Country"])
    final = semifinal.reset_index()[["Restaurant Name", "Number of Stars", "Country"]]
    # semifinal.loc[(michelin_guide["Restaurant Name"]) & (michelin_guide["Number of Stars"]) & (michelin_guide["country"])]
    return final


# Question 8
def mean_cuisine(michelin_guide, rating):
    # determine average for all cuisine type 
    # and then figure out which has a higher average than threshold
    # then return series NOT dataframe
    mean = michelin_guide.groupby("Cuisine Type").agg({"Number of Stars": "mean"})
    mean_round = mean.round(decimals=2)
    abovethresh = mean_round.loc[(mean_round["Number of Stars"]>rating)]
    final = abovethresh.squeeze()
    return final


if __name__ == "__main__":

    # # Q1
    # michelin_guide = pd.read_excel("michelin.xlsx")
    # pprint(merge_columns(michelin_guide))

    # # Q2
    # michelin_guide = pd.read_excel("michelin.xlsx")
    # merge_columns(michelin_guide)
    # pprint(price_cleaning(michelin_guide))

    # # Q3
    # michelin_guide = pd.read_excel("michelin.xlsx")
    # merge_columns(michelin_guide)
    # price_cleaning(michelin_guide)
    # write_to_file(michelin_guide, "cleaned_guide.xlsx", "michelin_guide")

    ####################################################
    ####################################################
    """
    DO NOT MODIFY CODE BELOW
    """
    try:
        cleaned_guide = pd.read_excel("cleaned_guide.xlsx")
    except:
        print("##########\n#\nYou must complete questions 1-3 before moving on to questions 4-7\n#\n##########")

    ####################################################
    ####################################################

    # Q4
    # pprint(types_by_country(cleaned_guide))

    # Q5
    # pprint(best_cities(cleaned_guide, "France", "Seafood"))
    # pprint(best_cities(cleaned_guide, "USA", "Korean"))

    # Q6
    # pprint(food_budget(cleaned_guide, "$$$", "Rio de Janeiro"))
    # pprint(food_budget(cleaned_guide, "$$", "Taipei"))

    # Q7
    pprint(ranking_restaurants(cleaned_guide, "Modern Cuisine", "$$$"))
    pprint(ranking_restaurants(cleaned_guide, "Creative", "$$$$"))

    # Q8
    # pprint(mean_cuisine(cleaned_guide, 1.2))
    # pprint(mean_cuisine(cleaned_guide, 1.4))







