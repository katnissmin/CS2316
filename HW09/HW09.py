import pymysql
import getpass
from pprint import pprint
import csv
# No other imports allowed

'''
First, run the provided vail.sql file to create the vail database.

For the following functions,
  - use the cursor, to execute SQL statements
  - call connection.commit() to save changes you make to the database
  - to examine the different tables in the database, make use of the sql script provided!

Reference the pymysql handout for more details on using pymysql
This assignment is due on Sunday, April 9th @ 11:59PM
'''

############################################################################
# THIS PART IS WRITTEN FOR YOU
############################################################################
def reset_database(cursor):

    d3 = "DROP TABLE IF EXISTS areas;"
    c1 = "CREATE TABLE areas (\
                areaname        VARCHAR (30)    NOT NULL UNIQUE,\
                pheight         INTEGER (5),\
                bheight         INTEGER (5),\
                verticle        INTEGER (5),\
                atype           ENUM('Bowl', 'Basin', 'Peak', 'MISC') NOT NULL,\
                PRIMARY KEY     (areaname)\
            );"

    d4 = "DROP TABLE IF EXISTS lifts;"
    c2 = "CREATE TABLE lifts (\
                liftnumber      INTEGER (2) NOT NULL UNIQUE,\
                liftname        VARCHAR (30) NOT NULL UNIQUE,\
                lifttype        ENUM('Express', 'Chair', 'Downloading', 'Gondola', 'Surface', 'Magic Carpet'),\
                openingtime     CHAR (5),\
                closingtime     CHAR (5),\
                capacity        INTEGER (2),\
                num_runs        INTEGER (2),\
                PRIMARY KEY     (liftnumber)\
            );"

    d1 = "DROP TABLE IF EXISTS runs;"
    c3 = "CREATE TABLE runs (\
                runname         VARCHAR (30) NOT NULL UNIQUE,\
                location        VARCHAR (30) NOT NULL,\
                accessed_by     INTEGER (2),\
                level           ENUM    ('Green', 'Blue', 'Black', 'Double Black', 'Terrain Park', 'Adventure Zone') NOT NULL,\
                snow_status     ENUM    ('Groomed', 'Ungroomed') NOT NULL,\
                status          ENUM    ('Open', 'Closed') NOT NULL,\
                run_type        ENUM    ('Run', 'Glade', 'Chute', 'Meadow') NOT NULL,\
                known_obstacle  VARCHAR (30),\
                PRIMARY KEY     (runname),\
                FOREIGN KEY     (location) REFERENCES areas(areaname),\
                FOREIGN KEY     (accessed_by) REFERENCES lifts(liftnumber)\
            );"

    d2 = 'DROP TABLE IF EXISTS area_data;'
    d5 = 'DROP TABLE IF EXISTS restaurants;'

    cursor.execute(d1) # runs has to be dropped first because it has foreign keys
    cursor.execute(d2) # area_data is next for the same reason

    cursor.execute(d3) # Then the other three tables
    cursor.execute(d4)
    cursor.execute(d5)

    cursor.execute(c1) # These lines create the new empty relations
    cursor.execute(c2)
    cursor.execute(c3)


############################################################################
# ANSWER THE QUESTIONS BELOW. USE THE CURSOR TO EXECUTE YOUR QUERIES
############################################################################

def question1(cursor):
    cursor.execute("SELECT * FROM lifts")
    return cursor.fetchall()
    '''
    Send a query to the vail database. Fetch all the rows in the lifts table and return them.

    # Test Case (No parameters)

    # Expected Return Value:
    # =========== Lifts Table ===========
    # ((2, 'Avanti', 'Express', '08:30', '16:00', 6, None),
    #  (19, 'Eagle Bahn', 'Gondola', '08:30', '16:00', 8, None),
    #  (21, 'Orient', 'Express', '09:00', '15:00', 4, None),
    #  (22, 'Mongolia', 'Surface', '09:00', '14:45', 1, None),
    #  (24, 'Wapiti', 'Surface', None, None, 1, None),
    #  (36, 'Tea Cup', 'Express', '09:00', '15:00', 4, None),
    #  (37, 'Skyline', 'Express', '10:00', '14:30', 4, None),
    #  (39, 'Petes', 'Express', '10:00', '14:15', 4, None))

    '''

def question2a(cursor, areaname, pheight, verticle, atype): # 1 point
    query = "INSERT INTO areas (areaname, pheight, bheight, verticle, atype) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(query, (areaname, pheight, None, verticle, atype))
    '''
    Insert a new area into the areas table. The new area will have bheight initialized as null.

    # Test Case
    # NULLS will show as None in the console.
    question2a(cursor, 'Lionshead', 12250, 1900, 'MISC')

    # Expected Modified Table
    # =========== Updated areas Table ===========
    # ('Blue Sky', 11570, None, 1900, 'Basin')
    # ('China', 11375, None, 1535, 'Bowl')
    # ('Game Creak', None, 10981, 1900, 'Bowl')
    # ('Golden', 9600, None, 1400, 'Peak')
    # ('Lionshead', 12250, None, 1900, 'MISC')
    # ('Mid-Vail', 11250, None, 1060, 'MISC')
    # ('Mongolia', 11455, None, 1615, 'Bowl')
    # ('Siberia', 11455, None, 1615, 'Bowl')
    '''

def question2b(cursor, data):
    for i in data:
        cursor.execute("INSERT INTO runs VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", i)
    
    '''
    You want to add multiple runs at one time. The parameter 'data' is a list of tuples
    that contains value for runname, location, accessed_by, level, snow_status, status, run_type, and known_obstacles.
    Insert these runs into the the runs table.

    # Test Case
    data = [('Rasputins Revenge', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Meadow', None),('Chopstix', 'China', 36, 'Blue', 'Groomed', 'Closed', 'Run', 'Ravine')]
    question2b(cursor, data)

    # Expected Modified Table:
    # =========== Updated runs Table ===========
    # ('Bolshoi Ballroom', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Glade', 'Trees')
    # ('Chopstix', 'China', 36, 'Blue', 'Groomed', 'Closed', 'Run', 'Ravine')
    # ('Genghis Khan', 'China', 36, 'Black', 'Ungroomed', 'Open', 'Meadow', None)
    # ('In The Wuides', 'Blue Sky', 37, 'Blue', 'Ungroomed', 'Open', 'Meadow', 'Cliffs')
    # ('Inner Mongolia', 'Blue Sky', 22, 'Black', 'Ungroomed', 'Open', 'Glade', 'Ravine')
    # ('Lovers Leap', 'Blue Sky', 37, 'Black', 'Ungroomed', 'Open', 'Glade', 'Cliffs')
    # ('O.S.', 'Blue Sky', 37, 'Black', 'Ungroomed', 'Open', 'Chute', 'Cliffs')
    # ('Rasputins Revenge', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Meadow', None)
    # ('Red Square', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Glade', 'Cliffs')
    # ('Resolution', 'Blue Sky', 39, 'Black', 'Ungroomed', 'Open', 'Glade', None)
    '''
    pass

def question3a(cursor):
    cursor.execute("CREATE TABLE area_data (\
                area_name VARCHAR (30) NOT NULL,\
                run_type enum('Green', 'Blue', 'Black', 'Double Black', 'Terrain Park', 'Adventure Zone'),\
                num_runs INTEGER,\
                FOREIGN KEY (area_name) REFERENCES areas(areaname)\
            );")

    cursor.execute("CREATE TABLE restaurants (\
                restaurant_name VARCHAR (50),\
                cuisine VARCHAR (20),\
                price VARCHAR (4),\
                type VARCHAR (50),\
                primary key (restaurant_name)\
            );")
    
    '''
    Create two new tables in vail database called area_data and restaurants

    The table area_data will have three attributes:
    - area_name             which is a non-null string with maximum 30 characters  - foreign key referencing areas(areaname)
    - run_type              which is a string from the set {'Green', 'Blue', 'Black', 'Double Black', 'Terrain Park', 'Adventure Zone'}
    - num_runs              which is an integer

    The table restaurants will have four attributes:
    - restaurant_name       which is a unique, non-nnull string with a maximum 50 characters. (Primary key of the table)
    - cuisine               which is a string with a maximum 20 characters
    - price                 which is a string with a maximum 4 characters
    - type                  which is a string with a maximum 50 characters

    Make sure that you initialize the attributes with the right SQL datatypes.
    Hint: You should use ENUM for the run_type attribute. Also, be careful with the quotations ...

    '''
    pass

def question3b(cursor):
    query = "INSERT INTO restaurants (restaurant_name, cuisine, price, type) VALUES (%s, %s, %s, %s);"
    data = list(csv.reader(open('vail_restaurants.csv')))[1:]
    cursor.executemany(query, data)
    '''
    In this question, you should populate the table restaurants you created in question 3a by importing data from csv files.
    Use the provided vail_restaurants.csv files to retrieve relevant data and insert it into the tables
    using pymysql. You should use the csv module!

    # Test Case
    # Expected Modified Tables

    # =========== Updated restaurants Table ===========
    # ('El Segundo', 'Mexican', '$$', 'Happy Hour & Aprés-Ski')
    # ('Matsuhisa Vail', 'Sushi', '$$$$', 'Special Occasions')
    # ('Pho 20', 'Vietnamese', '$', 'Happy Hour & Aprés-Ski')
    # ('Root & Flower', 'American', '$$$', 'Happy Hour & Aprés-Ski')
    # ('Splendido ', 'French', '$$$$', 'Special Occasions')
    # ('Ti Amo', 'Italian', '$$$', 'Special Occasions')
    # ('Vail Brewing Co', 'Brewery', '$', 'Happy Hour & Aprés-Ski')
    # ('Zino Ristorante', 'Italian', '$$$', 'Special Occasions')
    '''
    pass

def question3c(cursor):
    query1 = "SELECT areaname, `level`, count(*) from areas join runs on areaname = location group by areaname, `level`;"
    cursor.execute(query1)
    data = cursor.fetchall()
    query2 = "INSERT INTO area_data (area_name, run_type, num_runs) VALUES (%s, %s, %s);"
    cursor.executemany(query2, data)
    
    '''
    Insert data into the area_data table created in question 3a by writing a query that finds the areaname, run label,
    and the number of runs for each area name and run label.

    # Test Case
    question3a(cursor)

    # Expected Modified Table:
    # =========== Updated area_data Table ===========
    # ('Siberia', 'Black', 2)
    # ('China', 'Black', 1)
    # ('Blue Sky', 'Blue', 1)
    # ('Blue Sky', 'Black', 4)
    '''
    pass

def question4a(cursor):
    query = "UPDATE areas SET bheight = pheight - verticle;"
    cursor.execute(query)
    '''
    Fill-up the bheight column in the areas table. This value should be
    equal to the pheight column minus the verticle column.

    # Test Case
    question4(cursor)

    # # Expected Modified Table:
    # =========== Updated areas Table ===========
    # ('Blue Sky', 11570, 9670, 1900, 'Basin')
    # ('China', 11375, 9840, 1535, 'Bowl')
    # ('Game Creak', None, None, 1900, 'Bowl')
    # ('Golden', 9600, 8200, 1400, 'Peak')
    # ('Mid-Vail', 11250, 10190, 1060, 'MISC')
    # ('Mongolia', 11455, 9840, 1615, 'Bowl')
    # ('Siberia', 11455, 9840, 1615, 'Bowl')
    '''
    pass

def question4b(cursor):
    query = "UPDATE lifts SET num_runs = (SELECT COUNT(*) FROM runs WHERE accessed_by = liftnumber);"
    cursor.execute(query)
    '''
    Update the lifts table by setting the num_runs attribute equal to the number of runs
    accessed_by that particular lift.

    # Test Case
    question5(cursor)

    # # Expected Modified Table:
    # =========== Updated lifts Table ===========
    # (2, 'Avanti', 'Express', '08:30', '16:00', 6, 0)
    # (19, 'Eagle Bahn', 'Gondola', '08:30', '16:00', 8, 0)
    # (21, 'Orient', 'Express', '09:00', '15:00', 4, 2)
    # (22, 'Mongolia', 'Surface', '09:00', '14:45', 1, 1)
    # (24, 'Wapiti', 'Surface', None, None, 1, 0)
    # (36, 'Tea Cup', 'Express', '09:00', '15:00', 4, 1)
    # (37, 'Skyline', 'Express', '10:00', '14:30', 4, 3)
    # (39, 'Petes', 'Express', '10:00', '14:15', 4, 1)
    '''
    pass

def question5(cursor, restaurant_name): # 1 point
    query = "DELETE FROM restaurants WHERE restaurant_name = %s;"
    cursor.execute(query, restaurant_name)
    '''
    Delete a restaurant from the restaurants table when given the restaurant name.
    You must have completed all of question 3 before starting this question.

    # Test Case
    question5(cursor, 'Matsuhisa Vail')

    # Expected Modified Table:
    # =========== Updated restaurants Table ===========
    # ('El Segundo', 'Mexican', '$$', 'Happy Hour & Aprés-Ski')
    # ('Pho 20', 'Vietnamese', '$', 'Happy Hour & Aprés-Ski')
    # ('Root & Flower', 'American', '$$$', 'Happy Hour & Aprés-Ski')
    # ('Splendido ', 'French', '$$$$', 'Special Occasions')
    # ('Ti Amo', 'Italian', '$$$', 'Special Occasions')
    # ('Vail Brewing Co', 'Brewery', '$', 'Happy Hour & Aprés-Ski')
    # ('Zino Ristorante', 'Italian', '$$$', 'Special Occasions')
    '''
    pass

############################################################################
# TESTING PORTION
############################################################################
def populate_database(cursor):
    #Populate the areas relation
    cursor.execute("INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Blue Sky', 11570, null, 1900, 'Basin');")
    cursor.execute("INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('China', 11375, null, 1535, 'Bowl');")
    cursor.execute("INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Game Creak', null, 10981, 1900, 'Bowl');")
    cursor.execute("INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Golden', 9600, null, 1400, 'Peak');")
    cursor.execute("INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Mid-Vail', 11250, null, 1060, 'MISC');")
    cursor.execute("INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Mongolia', 11455, null, 1615, 'Bowl');")
    cursor.execute("INSERT INTO areas(areaname, pheight, bheight, verticle, atype) VALUES ('Siberia', 11455, null, 1615, 'Bowl');")

    #Populate the lifts relation
    cursor.execute("INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (37, 'Skyline', 'Express', '10:00', '14:30', 4, null);")
    cursor.execute("INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (39, 'Petes', 'Express', '10:00', '14:15', 4, null);")
    cursor.execute("INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (36, 'Tea Cup', 'Express', '09:00', '15:00', 4, null);")
    cursor.execute("INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (24, 'Wapiti', 'Surface', null, null, 1, null);")
    cursor.execute("INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (21, 'Orient', 'Express', '09:00', '15:00', 4, null);")
    cursor.execute("INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (22, 'Mongolia', 'Surface', '09:00', '14:45', 1, null);")
    cursor.execute("INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (2, 'Avanti', 'Express', '08:30', '16:00', 6, null);")
    cursor.execute("INSERT INTO lifts(liftnumber, liftname, lifttype, openingtime, closingtime, capacity, num_runs) VALUES (19, 'Eagle Bahn', 'Gondola', '08:30', '16:00', 8, null);")

    #Populate the runs relation
    cursor.execute("INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Lovers Leap', 'Blue Sky', 37, 'Black', 'Ungroomed', 'Open', 'Glade', 'Cliffs');")
    cursor.execute("INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Resolution', 'Blue Sky', 39, 'Black', 'Ungroomed', 'Open', 'Glade', null);")
    cursor.execute("INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('In The Wuides', 'Blue Sky', 37, 'Blue', 'Ungroomed', 'Open', 'Meadow', 'Cliffs');")
    cursor.execute("INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Genghis Khan', 'China', 36, 'Black', 'Ungroomed', 'Open', 'Meadow', null);")
    cursor.execute("INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Red Square', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Glade', 'Cliffs');")
    cursor.execute("INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Bolshoi Ballroom', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Glade', 'Trees');")
    cursor.execute("INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('Inner Mongolia', 'Blue Sky', 22, 'Black', 'Ungroomed', 'Open', 'Glade', 'Ravine');")
    cursor.execute("INSERT INTO runs(runname, location, accessed_by, level, snow_status, status, run_type, known_obstacle) VALUES ('O.S.', 'Blue Sky', 37, 'Black', 'Ungroomed', 'Open', 'Chute', 'Cliffs');")

def main():
    user_password = getpass.getpass('\n# Enter your MySQL Server password: ')

    connection = pymysql.connect(host = 'localhost',
                                 user = 'root',
                                 password = user_password,
                                 db = 'vail',
                                 charset = "utf8mb4",
                                 cursorclass = pymysql.cursors.Cursor)

    # Always create the cursor
    cursor = connection.cursor()

    reset_database(cursor)
    populate_database(cursor)


    ############################################################################
    # TEST CASES BELOW.
    ############################################################################
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY
    # WE RECOMMEND YOU RUN EACH OF THEM SEPARATELY
    ############################################################################
    ############################################################################
    # IF YOU DO NOT TEST THEM SEPARATELY YOUR ANSWERS MAY DIFFER


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 1 TEST CASE
    # rows_returned = question1(cursor)
    # pprint(rows_returned)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 2A TEST CASE
    # question2a(cursor, 'Lionshead', 12250, 1900, 'MISC')
    # print('=========== Updated students Table ===========')
    # cursor.execute("SELECT * FROM areas;")
    # for row in cursor.fetchall():
    #     print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # QUESTION 2B TEST CASE
    # data = [('Rasputins Revenge', 'Siberia', 21, 'Black', 'Ungroomed', 'Open', 'Meadow', None),('Chopstix', 'China', 36, 'Blue', 'Groomed', 'Closed', 'Run', 'Ravine')]
    # question2b(cursor, data)
    # print('=========== Updated classes Table ===========')
    # cursor.execute("SELECT * FROM runs;")
    # for row in cursor.fetchall():
    #   print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 3A TEST CASE
    # question3a(cursor)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 3B TEST CASE
    # question3a(cursor)
    # question3b(cursor)
    # print('=========== Updated restaurants Table ===========')
    # cursor.execute("SELECT * FROM restaurants")
    # for row in cursor.fetchall():
    #   print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 3C TEST CASE
    # question3a(cursor)
    # question3c(cursor)
    # print('=========== Updated area_data Table ===========')
    # cursor.execute("SELECT * FROM area_data")
    # for row in cursor.fetchall():
    #   print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 4A TEST CASE
    # question4a(cursor)
    # print('=========== Updated areas Table ===========')
    # cursor.execute("SELECT * FROM areas")
    # for row in cursor.fetchall():
    #   print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # # QUESTION 4B TEST CASE
    # question4b(cursor)
    # print('=========== Updated lifts Table ===========')
    # cursor.execute("SELECT * FROM lifts")
    # for row in cursor.fetchall():
    #   print(row)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # QUESTION 5 TEST CASE
    # question3a(cursor)
    # question3b(cursor)
    # question5(cursor, 'Matsuhisa Vail')
    # print('=========== Updated restaurants Table ===========')
    # cursor.execute("SELECT * FROM restaurants;")
    # for row in cursor.fetchall():
    #     print(row)


    # Always commit the connection when you are done
    connection.commit()


if __name__ == "__main__":
    main()
