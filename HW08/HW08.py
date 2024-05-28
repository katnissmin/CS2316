import pymysql
from pprint import pprint
import getpass

def create_cursor(host_name, user_name, pw, db_name):
    try:
        connection = pymysql.connect(host = host_name, user = user_name, password = pw, db = db_name, \
                                    charset = "utf8mb4", cursorclass = pymysql.cursors.Cursor)
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print(e)
        print(f"Couldn't log in to MySQL server using this password: {pw}.\n")

def query1(cursor):
    '''
    QUERY 1

    Given the episodes table from the friends database, write a query that
    returns all the episode titles that have an air date greater than 1996 and
    episode number less than 15.

    Expected Output:

    (('The One With the Cat',),
    ('The One With All the Kissing',),
    ('The One With the Apothecary Table',),
    ('The One With the Red Sweater',),
    ('The One Where Monica Sings',),
    ('The One After Joey and Rachel Kiss',),
    ('The One With the Cake',),
    ('The One With Princess Consuela',))
    '''

    query = 'select title from episodes where episode_num < 15 and air_date > 1996;'

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query2(cursor, character_id_min):
    '''
    QUERY 2

    Given the quotes table from the friends database and an integer character_id_min,
    return all quote IDs whose quote text starts with the letter "I" and
    have a character ID that is larger than the parameter character_id_min.

    Hint: What would you use to fill in the place of a parameter for PyMySQL?
          A quick google search will help.

    Expected Output:

    ((4,), (6,), (7,), (16,), (27,))
    '''

    query = 'select quote_id from quotes where quote_text like "I%%" and character_id > "%s";'

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query, (character_id_min,))
    result = cursor.fetchall()
    return result

def query3(cursor):
    '''
    QUERY 3

    Given the characters table, write a query that gives the char_id, char_name, and age
    of the oldest character. If multiple characters have the same age, then find the
    character with the largest char_id.

    Expected Output:

    ((9, 'Mike Hannigan', 28),)
    '''

    query = 'select char_id, char_name, age from characters where age = (select MAX(age) from characters) ORDER BY char_id DESC LIMIT 1;'

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query4(cursor):
    '''
    QUERY 4

    Given the apartments table, write a query that gives the building_name and count of buildings
    (renamed num_buildings) for the corresponding building_name. Only include buildings that
    do NOT have a street name beginning with 'B', and only return the rows with ONLY ONE building.

    Expected Output:

    (('East Village', 1),)
    '''

    query = 'select building_name, COUNT(building_name) as num_buildings from apartments where street_name not like "B%" group by building_name having num_buildings = 1;'

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query5(cursor):
    '''
    QUERY 5

    Looking at the relationships of the characters in the show, you want to make a list of all of the characters
    in a certain type of relationship. Create a query that will return the name of every character involved in a hopeless relationship.

    Hint: This involves nested queries

    Hint: Make sure to account for both characters in the relationship (char1_id and char2_id)

    Expected Output:

    (('Rachel Green',), ('Ross Geller',), ('Gunther',), ('Emily Waltham',))
    '''

    query = 'select char_name from characters where char_id in (select char1_id from relationships where type = "hopeless" union select char2_id from relationships where type = "hopeless");'

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query6(cursor):
    '''
    QUERY 6

    Given the episodes and characters table, write a query that gives the air_date and the average
    of the episode ids for each air date (renamed as 'avg_ep_ids' and rounded to 1 decimal place).
    Only incldue values that have an actor's age greater than or equal to 26 and an average
    episode_id greater than 5. Order these values by the average of the episode ids and
    return them in descending order.

    Expected Output:

    ((2004, Decimal('24.0')),
    (2003, Decimal('21.5')),
    (2001, Decimal('17.0')),
    (2000, Decimal('14.5')),
    (1999, Decimal('13.0')),
    (1998, Decimal('11.5')),
    (1997, Decimal('9.5')),
    (1996, Decimal('7.0')))
    '''

    query = 'select air_date, round(avg(episode_id), 1) as avg_ep_ids from episodes join characters on actor_id = char_id where age >= 26 group by air_date having avg(episode_id) > 5 order by avg_ep_ids desc;'

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def query7(cursor):
    '''
    QUERY 7

    Given the episodes and characters table, write a query that gives the actor_id,
    char_name (renamed as 'char'), and average percentage of episodes each actor was in
    (renamed as ep_percentage and rounded to a whole number). Order the rows by the ep_percentage and only return the rows
    with the 2nd, 3rd, and 4th highest percentages.

    Hint: The percentage of episodes an actor starred in can be calulated by:

          ((# of episodes the actor was in) / (total # of episodes)) * 100

    Hint: You will need to write another query to find the total # of episodes

    Hint: When ordering rows by a column name, you should not put quotes around the column name

    Expected Output:

    ((3, 'Phoebe Buffay', Decimal('24')),
    (1, 'Rachel Green', Decimal('20')),
    (4, 'Ross Geller', Decimal('16')))
    '''

    query = 'select actor_id, char_name as "char", count(char_id)/(select count(*) from episodes) * 100 as "ep_percentage" from episodes join characters on actor_id = char_id group by actor_id order by ep_percentage desc limit 3 offset 1;'

    '''DO NOT CHANGE THE CODE BELOW'''
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def main():

    ######################## Insert MySQL Server password if applicable ########################

    user_password = getpass.getpass('\n# Enter your MySQL Server password: ')
    cursor = create_cursor('localhost', 'root', user_password, 'friends')

    # If you do not want to enter your password every time, you can replace
    # user_password with your password (as a string) and comment out
    # this line of code: user_password = getpass.getpass('\n# Enter your MySQL Server password: ')
    # We recommend resetting this before uploading your HW.

    ########################### Test Cases ###########################

    # # Query 1
    # print(">>> query1(cursor)")
    # pprint(query1(cursor))

    # # Query 2
    # character_id_min = 2
    # print(">>> query2(cursor, character_id_min)")
    # pprint(query2(cursor, character_id_min))


    # # Query 3
    # print(">>> query3(cursor)")
    # pprint(query3(cursor))

    # # Query 4
    # print(">>> query4(cursor)")
    # pprint(query4(cursor))


    # # Query 5
    # print(">>> query5(cursor)")
    # pprint(query5(cursor))

    # # Query 6
    # print(">>> query6(cursor)")
    # pprint(query6(cursor))


    # # Query 7
    # print(">>> query7(cursor)")
    # pprint(query7(cursor))



if __name__ == '__main__':
    main()
