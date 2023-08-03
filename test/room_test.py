import unittest
from src.person import *
from src.song import *
from src.room import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song = Song("Berlin", "Take My Breath Away")
        self.customer_1 = Person("Oleksii", 10.00, self.song)
        self.customer_2 = Person("Sam", 15.00, self.song)
        self.customer_3 = Person("John", 0.00, self.song)
        self.room_1 = Room("Tokyo", 2, 5.00)

    def test_room_has_name(self):
        self.assertEqual("Tokyo", self.room_1.name)

    def test_room_has_0_guests(self):
        self.assertEqual(len(self.room_1.guests), 0)

    def test_if_guest_has_checked_in(self):
        self.room_1.check_in(self.customer_1)
        self.assertEqual(len(self.room_1.guests), 1)

    def test_if_guest_has_checked_out(self):
        self.room_1.check_in(self.customer_1)
        self.room_1.check_out(self.customer_1)
        self.assertEqual(len(self.room_1.guests), 0)

    def test_if_song_has_been_added(self):
        self.room_1.add_song(self.song)
        self.assertEqual(len(self.room_1.songs), 1)

    def test_exceeding_capacity(self):
        self.room_1.check_in(self.customer_1)
        self.room_1.check_in(self.customer_2)
        self.room_1.check_in(self.customer_3)
        self.assertEqual(len(self.room_1.guests), 2)

    def test_room_has_price(self):
        self.assertEqual(self.room_1.entry_fee, 5.00)

