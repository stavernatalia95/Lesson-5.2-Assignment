
# Define a class Songs, it will show the lyrics of a song.
# Its __init__() method should have two arguments:self and lyrics.
# lyrics is a list. Inside your class create a method called sing_me_a_song()
# that prints each element of lyrics on its own line.



class songs:
    def __init__(self, lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

the_chain_song=songs(["And if, you don't love me now",
                      "You will never love me again",
                      "I can still hear you saying",
                      "You would never break the chain"])

print(the_chain_song.sing_me_a_song())
