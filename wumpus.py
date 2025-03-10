# Here we are going to create a game called Wumpus World!
# A is AI Agent, G is Gold, W is Wumpus, P is pit
# The Environment is consist of 4X4 matrix.

import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.player_pos = [0, 0]
        self.gold_pos = self.place_randomly()
        self.wumpus_pos = self.place_randomly()
        self.pit_pos = self.place_randomly()
        self.game_over = False
        
    def place_randomly(self):
        while True:
            pos = [random.randint(0, self.size - 1), random.randint(0, self.size - 1)]
            if pos != [0, 0]:  # Avoid placing on the player's start position
                return pos

    def display_grid(self):
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] == self.player_pos:
                    print('A', end=' ')
                elif [i, j] == self.gold_pos:
                    print('G', end=' ')
                elif [i, j] == self.wumpus_pos:
                    print('W', end=' ')
                elif [i, j] == self.pit_pos:
                    print('P', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()

    def move(self, direction):
        if self.game_over:
            print("Game over! Restart to play again.")
            return

        x, y = self.player_pos
        if direction == 'w' and x > 0:
            self.player_pos[0] -= 1
        elif direction == 's' and x < self.size - 1:
            self.player_pos[0] += 1
        elif direction == 'a' and y > 0:
            self.player_pos[1] -= 1
        elif direction == 'd' and y < self.size - 1:
            self.player_pos[1] += 1
        else:
            print("Invalid move!")
            return

        self.check_status()

    def check_status(self):
        if self.player_pos == self.wumpus_pos:
            print("Oh no! You were eaten by the Wumpus!")
            self.game_over = True
        elif self.player_pos == self.pit_pos:
            print("You fell into a pit! Game over.")
            self.game_over = True
        elif self.player_pos == self.gold_pos:
            print("Congratulations! You found the gold!")
            self.game_over = True
        else:
            print("You're still alive. Keep moving!")

# To Run the game
game = WumpusWorld()
while not game.game_over:
    game.display_grid()
    move = input("Enter move (up/down/left/right): ").strip().lower()
    game.move(move)

game.display_grid()
