## NOTES:

# CS 2316 - Spring 2023 - HW02 
# HW02: This homework is due by Friday, February 3rd @ 11:59PM through Gradescope

# This homework is divided into three sections.
# Questions 1 and 2 MUST BE DONE IN ONE LINE
# Questions 3 and 4 require you to download the "cats.txt" file
# Questions 5 and 6 require you to download the "michelin.csv" file

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW02.py  - Your submission should be named exactly HW02.py

# cats.txt and michelin.csv must be located in the same folder as HW02.py in order for your
# code to run properly

import json, csv
from pprint import pprint

#question 1
def character_gryffindor(character_list):
    return sorted(list(set(filter(lambda x: x.split()[-1] == "Gryffindor", character_list))), key=lambda x: x.split()[0])

#question 2
def character_dict(prof_dict):
    return {char: sorted(prof_list, key=lambda x: (x.split()[-1][-1], x.split()[0][0])) for char, prof_list in prof_dict.items()}

#question 3
def txt_to_csv(input_file):
    newlist = []
    with open(input_file, "r") as infile: #Reading data
        data = infile.readlines() #list of every line as a string in a list, has all the \t \n

    for line in data:
        line = line.strip('\n')
        line = line.split('\t')
        strip_line = []
        for i in line:
            if i != "":
                strip = i.strip('"')
                strip_line.append(strip)

        if len(strip_line) < 5:
            continue
        newlist.append(strip_line[:2] + strip_line[3:])

    # header = data[0].split("\t") #separate header, add it separately
    # header.remove(header[2])
    # newlist.append(header)
    # print(newlist)

    # for line in data[1:]:
    #     for i in line:
    #         if i != "":
    #             line = i.strip('"')
    #     clean = line.split("\t") # Cleaned line broken into list
    #     # clean.remove(clean[2])
    #     if len(clean) >= 5:
    #         newlist.append(clean)

    with open("cleaned_cats.csv", "w") as outfile: # Writing the output csv file
        writer = csv.writer(outfile)
        writer.writerows(newlist) # writing list of lists to csv

    return newlist


#question 4
def write_to_json(alist, output_file):
    adict = {}
    for i, line in enumerate(alist):
        if i % 2 == 0 and i != 0:
            pattern = line[2]
            if pattern not in adict.keys():
                adict[pattern] = []
                adict[pattern].append(line[3])
            else:
                adict[pattern].append(line[3])

    for pattern in adict:
        adict[pattern] = list(set(adict[pattern]))

    # print(adict["Semi-long"])

    json.dump(adict, open(output_file, "w"))
    return(adict)


#question 5
def csv_cleaner(input_file):
    with open(input_file, "r", encoding='utf8') as infile:
        read = csv.reader(infile)
        data = list(read)

    for row in data:
        row[-2] = row[-2] + row[-1]
        del row[-1]
    data[0][-1] = "Cuisine Type"

    dollarsign = 0
    count = 0
    for row in data[1:]:
        row[-1] = row[-1].strip()
        row[-3] = row[-3].strip()
 
        if len(data[-2]) != 0:
            dollarsign += len(row[-2])
            count += 1

    for i in data:
        if i[-2] == '':
            i[-2] = "$" * int(dollarsign/count)

    # write to new csv file
    with open("clean_michelin.csv", 'w', encoding='utf8') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(data)
    return list(data)


#question 6
def michelin_guide(input_file):
    popular = {}
    with open(input_file, "r", encoding='utf8') as infile:
        read = csv.reader(infile)
        data = list(read)


    for i in data[1:]:
        if i[-3] not in popular.keys():
            popular[i[-3]] = {}
            popular[i[-3]][i[-1]] = 1
        else:
            if i[-1] in popular[i[-3]].keys():
                popular[i[-3]][i[-1]]+= 1
            else:
                popular[i[-3]][i[-1]] = 1

    return popular

if __name__ == "__main__":
    ## Question 1
    # print(character_gryffindor(["Scorpius Malfoy, Slytherin", "Harry Potter, Gryffindor", "Cedric Diggory, Hufflepuff", "Ronald Weasley, Gryffindor", "Luna Lovegood, Ravenclaw"]))
    # print(character_gryffindor(["Hermione Granger, Gryffindor", "Hermione Granger, Gryffindor", "Cedric Diggory, Hufflepuff", "Sirius Black, Gryffindor", "James Potter, Gryffindor"]))

    ## Question 2
    # print(character_dict({"Harry": ["Albus Dumbledore", "Minerva McGonagall", "Severus Snape", "Rubeus Hagrid"], "Hermione": ["Remus Lupin", "Alastor Moody", "Horace Slughorn"]}))
    # print(character_dict({"Scorpius": ["Severus Snape", "Dolores Umbridge", "Horace Slughorn"], "Neville": ["Cuthbert Binns", "Rubeus Hagrid", "Minerva McGonagall"]}))

    ## Question 3
    # print(txt_to_csv("cats.txt"))

    ## Question 4
    # pprint(write_to_json(txt_to_csv("cats.txt"), 'cats.json'))

    ## Question 5
    # pprint(csv_cleaner('michelin.csv'))

    ## Question 6
    pprint(michelin_guide("clean_michelin.csv"))

    pass



