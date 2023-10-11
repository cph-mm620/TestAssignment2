class BowlingGame:

    #Constructor
    def __init__(self):
        self.rolls = [0] * 21
        self.currentRoll = 0

    # Method for rolls
    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    #Method for calculating the score
    def score(self):
        score = 0
        frameIndex = 0
        for frame in range(10):
            if self.is_strike(frameIndex):
                score += 10 + self.strike_bonus(frameIndex)
                frameIndex += 1
            elif self.is_spare(frameIndex):
                score += 10 + self.spare_bonus(frameIndex)
                frameIndex += 2
            else:
                score += self.sum_of_balls_in_frame(frameIndex)
                frameIndex += 2
        return score

    #Helper methods
    def is_strike(self, frameIndex):
        return self.rolls[frameIndex] == 10

    def sum_of_balls_in_frame(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1]

    def spare_bonus(self, frameIndex):
        return self.rolls[frameIndex + 2]

    def strike_bonus(self, frameIndex):
        return self.rolls[frameIndex + 1] + self.rolls[frameIndex + 2]

    def is_spare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1] == 10


import unittest
from BowlingGame import BowlingGame

class BowlingGameTest(unittest.TestCase):

    #Initializes the Game class
    def setUp(self):
        self.g = BowlingGame()

    #Helper method to roll the ball
    def rollMany(self, n, pins):
        for i in range(n):
            self.g.roll(pins)

    #Tests the different scenarios
    def testGutterGame(self):
        self.rollMany(20, 0)
        self.assertEqual(0, self.g.score())

    def testAllOnes(self):
        self.rollMany(20, 1)
        self.assertEqual(20, self.g.score())

    def testOneSpare(self):
        self.rollSpare()
        self.g.roll(3)
        self.rollMany(17, 0)
        self.assertEqual(16, self.g.score())

    def testOneStrike(self):
        self.rollStrike()
        self.g.roll(3)  
        self.g.roll(4)  
        self.rollMany(16, 0)
        self.assertEqual(24, self.g.score())

    def testPerfectGame(self):
        self.rollMany(12, 10)
        self.assertEqual(300, self.g.score())

    def rollStrike(self):
        self.g.roll(10)

    def rollSpare(self):
        self.g.roll(5)
        self.g.roll(5) 
   

if __name__ == '__main__':
    unittest.main()