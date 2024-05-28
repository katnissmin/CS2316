#question 0
def welcome_class():
    print("Welcome to CS2316!")

#question 1
def where_to(message):
    new = ""
    for i in message:
        if i.isdigit():
            new += ""
        else:
            new += i
    return new

#question 2
def name_sort(staff):
    staff.sort(key=lambda x: x.split()[-1])
    for i in staff:
        if i[0] == "Q" or i[0] == "X":
            staff.remove(i)
        else:
            staff = staff
    return staff

#question 3
def gpa_manipulation(gpa_list):
    for i in range(0, len(gpa_list)):
        if gpa_list[i] == None:
            gpa_list[i] = 3.80

    gpa_list = gpa_list[::-1]
    gpa_list = tuple(gpa_list)
    return gpa_list

#question 4
def motto_maker(slogan1, slogan2):
    return f"From '{slogan1}' and '{slogan2}' comes '{slogan1} {slogan2}'. How does that sound?"

#question 5
def engineering_types(majors):
    for i in majors:
        if "engineering" not in i.lower():
            majors.remove(i)

    newmajors = []
    for j in majors:
        l = j.lower()
        k = l.replace(" engineering", "")
        newmajors.append(k)

    newmajors.sort()
    newwmajors = []
    for k in newmajors:
        if k.capitalize() not in newwmajors:
            newwmajors.append(k.capitalize())

    return newwmajors

#question 6
def traditions_dict(adict):
    sorted_adict = {}
    for i, j in adict.items():
        sorted_adict[i] = sorted(j, key=lambda x: (x[-1], x[0]))
    return sorted_adict

##print(traditions_dict({"Jacob": ["The Horse", "Stealing the t", "Midnight Bud"], "Athena": ["Mini Five-Hundred", "Freshman Cake Race", "Buzzweiser Song"], "Liv": ["Freshman Cake Race", "George P. Burdell", "Buzzweiser Song"]}))
##print(traditions_dict({"Madison": ["The Horse", "Midnight Bud", "Buzzweiser Song"], "Anna": ["Mini Five-Hundred", "Buzzweiser Song", "Freshman Cake Race"],"Ashok": ["The Horse", "Freshman Cake Race", "Stealing the t", "Midnight Bud"]}))
##print('---')

#question 7
def classes(adict, major):
    x = []
    for i in adict:
        if major in adict[i]:
            x.append(i)
    x = set(x)
    return x


if __name__ == "__main__":

    # # Q0
    # welcome_class()
    # print('---')

    # # Q1
    # print(where_to("Le1t's5 me8et0 a777t Ken4d6eda!"))
    # print(where_to("Ho0w a2bo8ut ha8vin2g 3lun2ch7 a3t W99ill0age?"))
    # print('---')

    # # Q2
    # print(name_sort(['Damon Williams', 'Xngel Cabrera', 'George Burdell', 'Brett Key', 'David Joyner', 'Qon Lowe']))
    # print(name_sort(['Melinda McDaniel', 'Buzz Yellowjacket', 'Josh Pastner', 'Nell Fortner', 'Michelle Collier']))
    # print('---')

    # # Q3
    # print(gpa_manipulation([3.72, 3.25, 3.43, 2.99, None, 3.87]))
    # print(gpa_manipulation([3.11, 3.23, None, 3.97, 2.47, 3.36]))
    # print('---')

    # # Q4
    # print(motto_maker("Put in", " a Ramblin' Wreck from Georgia Tech"))
    # print('---')

    # # Q5
    # print(engineering_types(['Electrical engineering', 'Industrial engineering', 'Computer Science', 'Aerospace engineering', 'Industrial Engineering', 'Chemical Engineering', "International affairs", 'Aerospace Engineering']))
    # print('---')

    # # Q6
    # print(traditions_dict({"Jacob": ["The Horse", "Stealing the t", "Midnight Bud"], "Athena": ["Mini Five-Hundred", "Freshman Cake Race", "Buzzweiser Song"], "Liv": ["Freshman Cake Race", "George P. Burdell", "Buzzweiser Song"]}))
    # print(traditions_dict({"Madison": ["The Horse", "Midnight Bud", "Buzzweiser Song"], "Anna": ["Mini Five-Hundred", "Buzzweiser Song", "Freshman Cake Race"],"Ashok": ["The Horse", "Freshman Cake Race", "Stealing the t", "Midnight Bud"]}))
    # print('---')

    # # Q7
    # classes_dict = {4232: ["ISYE", "MATH", "HTS"], 2316: ["CS", "CX", "MGT"], 3000: ["ISYE", "MGT", "ECE"], 2027: ["ISYE", "PSYC", "HTS"]}

    # print(classes(classes_dict, "ISYE"))
    # print(classes(classes_dict, "CS"))
    # print('---')

    pass



