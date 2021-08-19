class Room:
    def __init__(self, capacity, price):
        self.capacity = capacity
        self.price = price
        self.songs = []
        self.guests = []


    def get_capacity(self):
        return self.capacity
    
    def add_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            guest.pay_room(self)

    def add_song(self, song):
        self.songs.append(song)

    





    
