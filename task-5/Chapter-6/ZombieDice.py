import zombiedice
import random
# A bot that stops rolling after it has rolled two brains


class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll()  # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break
# A bot that, after the first roll, randomly decides if it will continue or stop


class MyZombie1:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            if random.randint(0, 1) != 0:
                diceRollResults = zombiedice.roll()
            else:
                break


# A bot that stops rolling after it has rolled two shotguns

class MyZombie2:
    def __init__(self, name):
        self.name = name
    def turn(self, gamestate):
        shotguns = 0
        diceRollResults = zombiedice.roll()
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break

# A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns

class MyZombie3:
    def __init__(self, name):
        self.name = name
    def turn(self, gamestate):
        diceRollResults = zombiedice.roll()
        count=0
        shotguns=0
        while diceRollResults is not None and count<=4:
            shotguns+= diceRollResults['shotgun']
            count+=1
            if shotguns<2:
                diceRollResults= zombiedice.roll()
            else:
                break


# A bot that stops rolling after it has rolled more shotguns than brains

class MyZombie4:
    def __init__(self, name):
        self.name = name
    def turn(self, gamestate):
        diceRollResults = zombiedice.roll()
        shotguns=0
        brains=0
        while diceRollResults is not None:
            shotguns+= diceRollResults['shotgun']
            brains+= diceRollResults['brains']
            if shotguns< brains:
                diceRollResults= zombiedice.roll()
            else:
                break


zombies = (
    # zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    # zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(
    #     name='Stop at 2 Shotguns', minShotguns=2),
    # zombiedice.examples.MinNumShotgunsThenStopsZombie(
    #     name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    MyZombie1(name='RandomDecision'),
    MyZombie2(name='TwoGunsStop'),
    MyZombie3(name='ConfusedBot'),
    MyZombie4(name='MoreGunsThanBrains'))

# Add any other zombie players here.


# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)