class Room:
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.guests = []
        self.songs = []

    def check_in(self, customer):
        if len(self.guests) < self.capacity:
            self.guests.append(customer)

    def check_out(self, customer):
        self.guests.remove(customer)

    def add_song(self, song):
        self.songs.append(song)
