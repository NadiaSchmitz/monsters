# The Lavin Interactive Company, which has developed the turn-based strategy Losers-V,
# is constantly extending its target market by localizing the game to as many languages as it can.
# In particular, they are interested in creating a version of the game in Anindilyakwa,
# which is one of the languages spoken by indigenous Australians.
# However, the localization is complicated by the fact that Anindilyakwa has no numerals.
# How can a phrase such as “You have seven black dragons and your enemy has forty black
# dragons” be translated into this language? The localizers have decided to translate
# it as follows: “You have few black dragons and your enemy has lots of black dragons.”
# They have compiled a table showing the rule of replacing numbers of monsters
# by Anindilyakwa words.
# Number	Designation in Anindilyakwa
# from 1 to 4	few
# from 5 to 9	several
# from 10 to 19	pack
# from 20 to 49	lots
# from 50 to 99	horde
# from 100 to 249	throng
# from 250 to 499	swarm
# from 500 to 999	zounds
# from 1000	legion
# Help the localizers automatize the process. Write a program that would output
# the appropriate word given the number of monsters.

i = 0

while i == 0:
    n = int(input("Enter a number between 1 and 2000: "))

    if n < 1 or n > 2000:
        print("Wrong number")
    else:
        i = 1
        word = ''
        if n <= 4:
            word = 'few'
        elif n <= 9:
            word = 'several'
        elif n <= 19:
            word = 'pack'
        elif n <= 49:
            word = 'lots'
        elif n <= 99:
            word = 'horde'
        elif n <= 249:
            word = 'throng'
        elif n <= 499:
            word = 'swarm'
        elif n <= 999:
            word = 'zounds'
        elif n <= 2000:
            word = 'legion'


print(word)