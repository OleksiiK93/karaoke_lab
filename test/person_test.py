import unittest
from src.person import *
from src.song import *
from src.room import *

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("Berlin", "Take My Breath Away")
        self.song_2 = Song("Journey", "Don't Stop Believin'")
        self.customer_1 = Person("Sam", 15.00, self.song_1)
        self.customer_2 = Person("John", 5.00, self.song_2)
        self.room_1 = Room("Tokyo", 2, 5.00)

    def test_person_has_favourite_song(self):
        self.assertEqual(self.customer_1.favourite_song, self.song_1)

    def test_person_has_enough_money_for_room(self):
        self.customer_1.buy_ticket(self.room_1)
        self.assertEqual(self.customer_1.wallet, 10.00)

    def test_person_doesnt_have_enough_money_for_room(self):
        self.customer_2.buy_ticket(self.room_1)
        self.assertEqual(self.customer_2.wallet, 0.00)

    def test_if_favourite_song_is_in_room(self):
        self.room_1.add_song(self.song_1)
        self.customer_1.buy_ticket(self.room_1)
        self.assertEqual("Whoo!", self.customer_1.buy_ticket(self.room_1))

    def test_if_favourite_song_is_not_in_room(self):
        self.room_1.add_song(self.song_1)
        self.customer_2.buy_ticket(self.room_1)
        self.assertEqual(self.customer_2.wallet, 0.00)
        self.assertEqual(None, self.customer_2.buy_ticket(self.room_1))
    
    
