class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def print_this(self):
        print("Still trying to learn OOP")

happy_bday_lyrics = ["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]


happy_bday = Song(happy_bday_lyrics)

# happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

# STUDY DRILL
the_way_life_goes = Song(["I know it hurts sometimes but you'll get over it",
                          "You'll find another life to live",
                          "I swear that you'll get over it"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

the_way_life_goes.sing_me_a_song()

the_way_life_goes.print_this()