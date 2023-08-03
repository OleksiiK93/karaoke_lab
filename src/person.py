class Person:
    
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
    
    def buy_ticket(self, room):
        if self.wallet >= room.entry_fee:
            self.wallet -= room.entry_fee
        if self.favourite_song in room.songs:
            return "Whoo!"
    
    # def cheer(self, room):
    #     if self.favourite_song in room.songs:
    #         return "Whoo!"
