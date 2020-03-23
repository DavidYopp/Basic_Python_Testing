import os
import simple_db
import sqlite3
import unittest
from unittest import skip


class TestMusicDatabase(unittest.TestCase):
    """
    Tests for the music database
    """

    def setUp(self):
        """
        Setup a temporary databse for testing against
        """
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()

        # create a table
        cursor.execute("""CREATE TABLE albums
                          (title text, artist text, release_date text,
                           publisher text, media_type text)
                       """)
        # insert some data
        cursor.execute("INSERT INTO albums VALUES "
                       "('Glow', 'Andy Hunter', '7/24/2012', "
                       "'Xplore Records', 'MP3')")

        #save data to database
        conn.commit()

        # insert multiple records using the mroe secure '?' method
        albums = [('Exodus', 'Andy Hunter', '7/9/2002',
                   'Sparrow Records', 'CD'),
                  ('Until We Have Faces', 'Red', '2/1/2011',
                   'Essential Records', 'CD'),
                  ('The End is Where We Begin', 'Thousand Foot Krutch',
                   '4/17/2012', 'TFKmusic', 'CD'),
                  ('The Good Life', 'Trip Lee', '4/10/2012',
                   'Reach Records', 'CD')]
        cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)",
                           albums)
        conn.commit()


    def tearDown(self):
        """
        Delete the database so we are good to go again for each test
        """
        os.remove("mydatabase.db")


    def test_updating_artist(self):
        """
        Test that we cn successfully update an artist's name
        """
        simple_db.update_artist('Red', 'Redder')
        actual = simple_db.select_all_albums('Redder')
        expected = [('Until We Have Faces', 'Redder',
                    '2/1/2011', 'Essential Records', 'CD')]
        self.assertEqual(expected, actual)


    def test_artist_does_not_exist(self):
        """
        Test that an artist does not exist
        """
        result = simple_db.select_all_albums('Redder')
        self.assertFalse(result)
