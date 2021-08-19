class Guest:
    def __init__(self, name, money, favourite_song):
        self.name = name
        self.money = money
        self.favourite_song = favourite_song

    def get_name(self):
        return self.name
    
    def pay_room(self, room):
        self.money -= room.price
    
    def favourite_song_is_on(self, room):
        for song in room.songs:
            if song.title == self.favourite_song:
                return "Whoo!"
        return "Aww!"