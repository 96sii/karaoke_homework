import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("No surprises", "Radiohead")

    def test_song_artist(self):
        self.assertEqual("Radiohead", self.song.song_artist())

    def test_song_title(self):
        self.assertEqual("No surprises", self.song.song_title())
