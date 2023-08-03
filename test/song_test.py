import unittest
from src.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Thin Lizzy", "Dancing in the moonlight")

    def test_song_has_title(self):
        self.assertEqual("Dancing in the moonlight", self.song.title)
        