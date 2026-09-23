class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

        Player.player_count += 1


p1 = Player("Chandan", 10)
p2 = Player("Rahul", 20)
p3 = Player("Amit", 15)

print("Player 1:", p1.name, p1.level)
print("Player 2:", p2.name, p2.level)
print("Player 3:", p3.name, p3.level)

print("Total players:", Player.player_count)