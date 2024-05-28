
import requests, re, json
from pprint import pprint
from bs4 import BeautifulSoup

## NOTES:

# CS 2316 - Spring 2023 - HW03 Regex, APIs, BeautifulSoup
# HW03: This homework is due by Sunday, February 19th @ 11:59PM.

# You are required to complete the missing bodies of the functions below.
# Further instructions are provided in the comments ...
# A few tips:
#   - Make sure you return the right value and datatype
#   - Test your code for each function by uncommenting the respective test cases
#     in the if __name__ == '__main__' block
#   - Do not import modules within functions
#   - Do not leave any print statements within your functions
#   - Submit in Gradescope as HW03.py  - Your submission should be named exactly HW03.py
#   - Print your variables as you code in order to see what values they have
#     especially for questions with API and BeautifulSoup

# Question 1
def ohno_twozero(placeholder, statement):
    return re.sub("[a-zA-Z][0][0]\w*", placeholder, statement)

# Question 2
def shakespeare_position(role, section):
    return re.search(r": ([^\.\?]+[\.\?]) " + role, section).group(1)
    #re.search(?<=\n)[A-Z][a-z]+(?::\s.*?[.?])\s(?={role}:\s)", section).group(0)[len(role)+2:] -> doesn't work damn it?? need to check

# Question 3
def dna_slice(strand, first_nucleotides, last_nucleotides):
    return len(re.search(first_nucleotides+"[A-Z]*?"+last_nucleotides, strand).group())

# Question 4
def pokehelp(poke_name, stat_min):
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
    response = requests.get(url)

    if response.status_code == 200:
        stats = response.json()["stats"]
        result = {}
        for stat in stats:
            name = stat["stat"]["name"]
            base_stat = stat["base_stat"]
            if base_stat > stat_min:
                result[name] = base_stat
        return result
    else:
        raise ValueError(f"Error {response.status_code}: {response.text}")

# Question 5
def typehelper(poke_name):
    # Make a GET request to the PokeAPI for the Pokemon's data
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke_name}")

    # Create the dictionary for the doubledamage
    doubledamage = {}
    if response.status_code == 200:
        for type in response.json()["types"]:
            name = type["type"]["name"]
            if name not in doubledamage.keys():
                doubledamage[name] = []
            typeresp = requests.get(type["type"]["url"])
            for ability in typeresp.json()["damage_relations"]["double_damage_from"]:
                doubledamage[name].append(ability["name"])
    return doubledamage

    # # Get the list of types for the Pokemon
    # # Need dictionary mapping each type to a list of types that do double damage

    # response.json()["types"]
    # for type in response_json:
    #     types = [type_data['type']['name']]???
    #
    # doubledamage = {}
    # relations = type_data["damage_relations"]
    # for damage in relations["double_damage_to"]:
    #     da = [damage["name"]]
    #     doubledamageto.append(da)
    # doubledamage[type_name] = double_damage_to
    # return doubledamage

# Question 6
def agatha_christie(website):
    response = requests.get(website)
    soup = BeautifulSoup(response.text, "html.parser")

    alist = []

    titles = soup.find_all("td")
    cleantitle = []
    for title in titles:
        a = title.text.replace("*", ""). strip()
        cleantitle.append(a)

    i = -1
    for line in cleantitle:
        i += 1
        if line == "":
            cleantitle[i] = None

    for j in range(0, len(cleantitle), 3):
        alist.append(cleantitle[j:j+3])

    alist[0][1] = "Publication Year"

    return alist

    # Get website and do soup
    # make a new list
    # get the titles and find all in table data
    # loop through cleantitle
    # if empty, None
    # append all the other elements using the j loop
    # change the alist element to match the conditions

# Question 7
def acotar(website):
    response = requests.get(website)
    soup = BeautifulSoup(response.text, "html.parser")
    tabledata = soup.find_all(class_ = "vevent")
    synopsisdata = soup.find_all(class_="expand-child")
    count = 1

    adict = {}

    for i, j in enumerate(tabledata):
        number = j.find("th").text
        isbn = j.find_all("td")[-1].text[-13:]
        date = j.find_all("td")[1].text
        synopsis = synopsisdata[i].find("td").text.strip()
        title = j.find(class_ = "summary").find("i").text

        adict[count] = {"ISBN": isbn, "Publication Date": date, "Synopsis": synopsis, "Title": title}

        count += 1
    return adict


if __name__ == "__main__":
    pass

    # # Q1
    # pprint(ohno_twozero('epic', "I am n0w l00king at 500 t0tal h0urs 0n Super Smash Br0s."))
    # pprint(ohno_twozero('bruh', "And I w0uld have g0tten away with it t00 if it wasn't f0r all 200 0f y0u meddling kids!"))

    # # Q2
    # section_1 = 'Benvolio: By my head, here come the Capulets. Mercutio: By my heel, I care not. ' + \
    # 'Tybalt: Gentlemen, good den: a word with one of you. Mercutio: And but one word with one of us?'
    # pprint(shakespeare_position('Tybalt', section_1))
    # pprint(shakespeare_position('Mercutio', section_1))

    # # Q3
    # strand_1 = 'TATGGGTCGAGCATGT'
    # pprint(dna_slice(strand_1, 'AT', 'CG'))
    # pprint(dna_slice(strand_1, 'GT', 'TG'))

    # # Q4
    # pprint(pokehelp("porygon", 65))
    # pprint(pokehelp("koraidon", 100))

    # # Q5
    # pprint(typehelper("bulbasaur"))
    # pprint(typehelper("corviknight"))

    # # Q6
    # pprint(agatha_christie("https://everythingagatha.com/home/every-agatha-christie-novel-in-order/"))

    # # Q7
    # pprint(acotar("https://en.wikipedia.org/wiki/A_Court_of_Thorns_and_Roses"))







