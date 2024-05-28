# HW07 - OOP and Comprehensions

class Song:

    def __init__(self, title, release_date, artist, length, single=False):
        self.title = title
        self.release_date = release_date
        self.artist = artist
        self.length = length
        self.single = single
        """
        Question 1
            Complete the __init__ method for the Song class. Attributes are as follows:
            title (str):             It is passed as a parameter (title). Represents the song's title.
                                    E.g. 'All Too Well (10 Minute Version) (Taylor's Version)'
            release_date (str):     It is passed as a parameter (release_date). Represents the songs release date.
                                    E.g. 'November 15, 2021'
            artist (str):           It is passed in as a parameter (artist). It is a string representing the songs artist.
                                    E.g. 'Taylor Swift'
            length (float):         It is passed in as paramater (length). It is a float representing the duration in minutes.
                                    E.g. 10.2
            single (bool)           It CAN be passed in as a parameter. This is an optional parameter that represents if a song is a
                                    single or not
                                    E.g. False

            Examples:
                >>> song1 = Song('All Too Well (10 Minute Version)', 'November 15, 2021', 'Taylor Swift', 10.20)
                >>> print(song1.title, song1.length, student1.single)
                ('All Too Well (10 Minute Version) (Taylor's Version)', 10.2, False)

                >>> song2 = Song('Exile', 'December 11, 2020', 'Taylor Swift', 4.78, False)
                >>> print(song2.title, song2.length, student2.single)
                ('Exile', 4.78, False)
        """

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist
        """
        Question 2.1.a
            Complete the __eq__ method. Two Student objects are equal if and only
            they have the same title and artist.

            ONE LINE

            Example:
                >>> song1 = Song('All Too Well (10 Minute Version)', 'November 15, 2021', 'Taylor Swift', 10.20)
                >>> song3 = Song('All Too Well', 'November 15, 2021', 'Taylor Swift', 5.50, False)
                >>> song4 = Song('All Too Well', 'October 22, 2012', 'Taylor Swift', 5.50)

                >>> song1 == song3
                False
                >>> song3 == song4
                True
        """

    def __lt__(self, other):
        return self.length < other.length
        """
        Question 2.1.b
            Complete the __lt__ method. A Song object is less than another if it's length is shorter than another objects length

            ONE LINE

            Example:
                >>> song5 = Song('ceilings', 'April 8, 2022', 'Lizzy McAlpine', 3.03)
                >>> song6 = Song('I Bet You Think About Me', 'November 15, 2021', 'Taylor Swift', 4.75, True)

                >>> song5 < song6
                True

                >>> song1 < song2
                False
        """

    def __repr__(self):
        return f"{self.title}, a {self.length} minute song by {self.artist} released on {self.release_date}."
        """
        Question 2.1.c
            Complete the __repr__ method. Calling or printing a Song object
            should be represented as the following string:

                '{title}, a {length} minute song by {artist} released on {date}.'

            ONE LINE

            Example:
                >>> song7 = Song('The Last Time', 'November 15, 2021', 'Taylor Swift', 4.98, False)
                >>> print(song7)
                The Last Time, a 4.98 minute song by Taylor Swift released on November 15, 2021.

                >>> song1 = Song('All Too Well (10 Minute Version)', 'November 15, 2021', 'Taylor Swift', 10.20)
                >>> print(song1)
                All Too Well (10 Minute Version), a 10.2 minute song by Taylor Swift released on November 15, 2021.
        """

class Album:

    def __init__(self, title, artist, song_list=[]):
        self.title = title
        self.artist = artist
        self.song_list = []

        for song in song_list:
            if self.artist == song.artist:
                self.song_list.append(song)
        
        single_list = []

        for song in song_list:
             if song.single == True:
                  single_list.append(song)

        self.num_songs = len(self.song_list)
        self.num_singles = len(single_list)
        
        """
        Question 3.1
            Complete the __init__ method for the Album class. Attributes are as follows:
            title (str)                   It is passed as a parameter (title). Represents the album title
            artist (str)                  It is passed as a parameter (artist). Represents the artist who made the album
            song_list (list)              It CAN be passed as a parameter (song_list). This is a list of song objects
                                          in the album. If a song is passed in that isn't by the same artist it should be removed.

            num_songs (int)               Derived Attribute - number of songs in the Albums song_list
            num_singles (int)             Derived Attrribute - number of songs in the Albums song_list that have the single attribute as True

            Example:
            >>> song_list1 = [song1, song3, song7, song9, song5]
            >>> album1 = Album('Red (Taylor's Version)', 'Taylor Swift', song_list1)
            >>> print(album1.title, album1.num_songs)
            ('Red (Taylor's Version)', 4)

            >>> song_list2 = [song11, song12, song5]
            >>> album2 = Album('midnights', 'Taylor Swift', song_list2)
            >>> print(album2.title, album2.num_songs)
            ('midnights', 2)
        """

    def __repr__(self):
        return f"{self.title} - by {self.artist} has {self.num_songs} songs and {self.num_singles} singles."
        """
        Question 3.2
        Complete the __repr__ method. Calling or printing a Album object
        should be represented as the following string:

            '{title} - by {artist} has {number of songs} songs and {number of singles} singles.'

        Example:
            >>> song_list3 = [song2]
            >>> album3 = Album('folklore', 'Taylor Swift', song_list3)
            >>> print(album3)
            folklore - by Taylor Swift has 1 songs and 0 singles.

            >>> song_list4 = [song13, song10]
            >>> album4 = Album('Formula 1 Theme - Single', 'Brian Tyler', song_list4)
            >>> print(album4)
            Formula 1 Theme - Single - by Brian Tyler has 1 songs and 1 singles.
        """

    def addsong(self, song):
        if song.artist == self.artist:
            self.song_list.append(song)
            self.num_songs += 1
            if song.single:
                self.num_singles += 1
        """
        Question 4
            Add a song to the album. Make sure to pass in the object rather
            than simply an attribute name of the object.
            Update everything that needs to be updated and make sure that the song
            has the same artist.

            Assume that the song is not already in the album.

            You should have no returns on this function

            Example:
                >>> album3.addsong(song10)
                >>> print(album3.song_list)
                [
                    "Exile, a 4.78 minute song by Taylor Swift released on December 11, 2020.",
                    "Snow on the Beach, a 4.26 minute song by Taylor Swift released on October 21, 2022."
                        ]


                >>> album2.addsong(song4)
                >>> print(album2.song_list)
                [
                    "Anti-Hero, a 3.33 minute song by Taylor Swift released on October 21, 2022.",
                    "Paris, a 3.26 minute song by Taylor Swift released on October 21, 2022.",
                    "All Too Well, a 5.5 minute song by Taylor Swift released on October 22, 2012."
                        ]
        """

    def removesong(self, song_name):
        for i in range(0, len(self.song_list)):
            if self.song_list[i].title == song_name:
                self.song_list.remove(self.song_list[i])

        self.num_songs = len(self.song_list)

        single_list = []

        for song in self.song_list:
             if song.single == True:
                  single_list.append(song)

        self.num_singles = len(single_list)
    
    """
        Question 5
            Remove a song from the album. You will be given the song title
            you should remove the corresponding song object.
            update everything that needs to be updated.

            Assume that the song is in the album

            You should have no returns on this function

            Example:
                >>> album2.removesong("All Too Well")
                >>> print(album2.song_list)
                [
                    "Anti-Hero, a 3.33 minute song by Taylor Swift released on October 21, 2022.",
                    "Paris, a 3.26 minute song by Taylor Swift released on October 21, 2022."
                        ]
        """

    def sorting(self):
        self.song_list.sort(key = lambda self: ((self.single), (self.length)), reverse=True)
        """
        Question 6
            Sort the album's song_list. Songs that are singles should come first followed by songs that are not.
            After sorting by singles you should sort by length. Longer songs should come before shorter longs.

            You should have no returns on this function

            ONE LINE

            Example:
                >>> album1.sorting()
                >>> print(album1.song_list)
                [
                    "Message in a Bottle, a 3.75 minute song by Taylor Swift released on November 15, 2021.",
                    "All Too Well (10 Minute Version), a 10.2 minute song by Taylor Swift released on November 15, 2021.",
                    "All Too Well, a 5.5 minute song by Taylor Swift released on November 15, 2021.",
                    "The Last Time, a 4.98 minute song by Taylor Swift released on November 15, 2021."
                        ]
        """



if __name__ == "__main__" :

    pass

    # All of the test cases below should be tested INDEPENDENTLY

    # # Song objects
    # song1 = Song('All Too Well (10 Minute Version)', 'November 15, 2021', 'Taylor Swift', 10.20)
    # song2 = Song('Exile', 'December 11, 2020', 'Taylor Swift', 4.78, False)
    # song3 = Song('All Too Well', 'November 15, 2021', 'Taylor Swift', 5.50, False)
    # song4 = Song('All Too Well', 'October 22, 2012', 'Taylor Swift', 5.50)
    # song5 = Song('ceilings', 'April 8, 2022', 'Lizzy McAlpine', 3.03)
    # song6 = Song('I Bet You Think About Me', 'November 15, 2021', 'Taylor Swift', 4.75, True)
    # song7 = Song('The Last Time', 'November 15, 2021', 'Taylor Swift', 4.98, False)
    # song8 = Song('Forever Winter', 'November 15, 2021', 'Taylor Swift', 4.38)
    # song9 = Song('Message in a Bottle', 'November 15, 2021', 'Taylor Swift', 3.75, True)
    # song10 = Song('Snow on the Beach', 'October 21, 2022', 'Taylor Swift', 4.26, False)
    # song11 = Song('Anti-Hero', 'October 21, 2022', 'Taylor Swift', 3.33, True)
    # song12 = Song('Paris', 'October 21, 2022', 'Taylor Swift', 3.26, False)
    # song13 = Song('Formula 1 Theme', 'March 22, 2018', 'Brian Tyler', 3.23, True)


    # # Album objects
    # song_list1 = [song1, song3, song7, song9, song5]
    # album1 = Album('Red (Taylor\'s Version)', 'Taylor Swift', song_list1)

    # song_list2 = [song11, song12, song5]
    # album2 = Album('midnights', 'Taylor Swift', song_list2)

    # song_list3 = [song2]
    # album3 = Album('folklore', 'Taylor Swift', song_list3)

    # song_list4 = [song13, song10]
    # album4 = Album('Formula 1 Theme - Single', 'Brian Tyler', song_list4)



    # # Song init
    # print(song1.title, song1.length, song1.single)
    # print(song2.title, song2.length, song2.single)

    # # Song eq
    # print(song1 == song3)
    # print(song3 == song4)

    # # Song lt
    # print(song5 < song6)
    # print(song1 < song2)

    # # Song repr
    # print(song7)
    # print(song1)



    # # Album init
    # print(album1.title, album1.num_songs)
    # print(album2.title, album2.num_songs)

    # # Album repr
    # print(album3)
    # print(album4)

    # # Album addsong
    # album3.addsong(song10)
    # print(album3.song_list)

    # # Album removesong
    # album2.addsong(song4)
    # print(album2.song_list)

    # album2.removesong("All Too Well")
    # print(album2.song_list)

    # # Album sorting
    # print(album1.song_list)
    # album1.sorting()
    # print(album1.song_list)









