# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.p1points = 0
        self.p2points = 0
        # If both players have equal points, use following key-values
        self.equal_points = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"
        }
        # Use following key-values to assign values for points of each player
        self.individual_points = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player):
        # Player wins 1 point
        if player == self.player1:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):
        if self.p1points == self.p2points:
            # If both players have more than 2 points, assign a Deuce
            result = self.equal_points.get(self.p1points, "Deuce")
        elif self.p1points >= 4 or self.p2points >= 4:
            difference = self.p1points - self.p2points
            if difference == 1:  # If P1 has 1 more point than P2
                result = "Advantage " + self.player1
            elif difference == -1:  # If P2 has 1 more point than P1
                result = "Advantage " + self.player2
            elif difference >= 2:  # P1 wins
                result = "Win for " + self.player1
            else:  # P2 wins
                result = "Win for " + self.player2
        else:
            # Set appropriate result with points of both players
            result = self.individual_points[self.p1points] + "-" + \
                     self.individual_points[self.p2points]
        return result


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if (self.p1points == self.p2points and self.p1points < 3):
            if (self.p1points == 0):
                result = "Love"
            if (self.p1points == 1):
                result = "Fifteen"
            if (self.p1points == 2):
                result = "Thirty"
            result += "-All"
        if (self.p1points == self.p2points and self.p1points > 2):
            result = "Deuce"

        P1res = ""
        P2res = ""
        if (self.p1points > 0 and self.p2points == 0):
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if (self.p2points > 0 and self.p1points == 0):
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p1points < 4):
            if (self.p1points == 2):
                P1res = "Thirty"
            if (self.p1points == 3):
                P1res = "Forty"
            if (self.p2points == 1):
                P2res = "Fifteen"
            if (self.p2points == 2):
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if (self.p2points > self.p1points and self.p2points < 4):
            if (self.p2points == 2):
                P2res = "Thirty"
            if (self.p2points == 3):
                P2res = "Forty"
            if (self.p1points == 1):
                P1res = "Fifteen"
            if (self.p1points == 2):
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if (self.p1points > self.p2points and self.p2points >= 3):
            result = "Advantage " + self.player1Name

        if (self.p2points > self.p1points and self.p1points >= 3):
            result = "Advantage " + self.player2Name

        if (self.p1points >= 4 and self.p2points >= 0 and (self.p1points - self.p2points) >= 2):
            result = "Win for " + self.player1Name
        if (self.p2points >= 4 and self.p1points >= 0 and (self.p2points - self.p1points) >= 2):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1) else "Win for " + s
