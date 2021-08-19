import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob", 40, "Old Dan Tucker")
        self.guest2 = Guest ("Jimmy", 50, "Mr. Brightside")
        self.room = Room(5, 30)
        self.song_1 = Song("Bananas", "Gwen Stefani")
        self.song_2 = Song("Levitate", "Due Lipa")
        self.song_3 = Song("Old Dan Tucker", "Bruce Springsteen")

    def test_guest_name(self):
        self.assertEqual("Bob", self.guest.get_name())
    
    def test_pay_room(self):
        self.guest.pay_room(self.room)
        self.assertEqual(10, self.guest.money)

    def test_favourite_song_is_on(self):
        self.room.add_song(self.song_1)
        self.room.add_song(self.song_2)
        self.room.add_song(self.song_3)
        self.assertEqual("Whoo!", self.guest.favourite_song_is_on(self.room))
        self.assertEqual("Aww!", self.guest2.favourite_song_is_on(self.room))



        


    