#©Justin Knecht

print("Ich habe eine Zahl zwischen 1 und 32 gewählt. Suchen sie sie!")

c = (0)

while c != 23:

    c = int(input("Raten sie: "))

    if c > 23:

        print(c)

        print("Zu Gross!")

    if c < 23:

        print(c)

        print("Zu Klein!")

    if c == 23:

        print(c)

        print("Bingo!")
