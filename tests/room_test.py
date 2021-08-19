import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
   def setUp(self):
      self.room_1 = Room(4, 40)

      self.guest_1 = Guest("David", 50, "Mr. Brightside")
      self.guest_2 = Guest("Colin", 20, "YMCA")
      self.guest_3 = Guest("Jess", 70, "Sabotage")
      self.guest_4 = Guest("Beth", 56, "Freebird")
      self.guest_5 = Guest("Cher", 80, "Dancing on the ceiling")

      self.song_1 = Song("Mr. Brightside", "The Killers" )

   def test_capacity(self):
      self.assertEqual(4, self.room_1.get_capacity())
   
   def test_add_guest(self):
      self.room_1.add_guest(self.guest_1)
      self.assertEqual(1, len(self.room_1.guests))

   def test_add_song(self):
      self.room_1.add_song(self.song_1)
      self.assertEqual(1, len(self.room_1.songs))

   def test_room_full(self):
      self.room_1.add_guest(self.guest_1)
      self.room_1.add_guest(self.guest_2)
      self.room_1.add_guest(self.guest_3)
      self.room_1.add_guest(self.guest_4)
      self.room_1.add_guest(self.guest_5)
      self.assertEqual(4, len(self.room_1.guests)) 
      # 5 guests have been added but the room only holds 4

   