# -*- coding: utf-8 -*-
class Match:

    def __init__(self, player1, player2, pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets
        self.p1_wins = 0
        self.p2_wins = 0
        self.p1_sets = ['', '', '', '', '']
        self.p2_sets = ['', '', '', '', '']

    def score(self):
        if self.p1_wins == 0 and self.p2_wins == 0:
            return "{0} plays with {1} | 0-0".format(self.p1, self.p2)

        # Pacted sets: 3
        if self.pacted_sets == 3:
            if self.p1_wins - self.p2_wins == 2:
                return "{0} defeated {1} | {2}, {3}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1])
            elif self.p1_wins - self.p2_wins == 1:
                return "{0} defeated {1} | {2}, {3}, {4}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1], self.p1_sets[2])
            elif self.p2_wins - self.p1_wins == 2:
                return "{0} defeated {1} | {2}, {3}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1])
            elif self.p2_wins - self.p1_wins == 1:
                return "{0} defeated {1} | {2}, {3}, {4}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1], self.p2_sets[2])

        # Pacted sets: 5
        elif self.pacted_sets == 5:
            if self.p1_wins - self.p2_wins == 3:
                return "{0} defeated {1} | {2}, {3}, {4}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1], self.p1_sets[2])
            elif self.p1_wins - self.p2_wins == 2:
                return "{0} defeated {1} | {2}, {3}, {4}, {5}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1], self.p1_sets[2], self.p1_sets[3])
            elif self.p1_wins - self.p2_wins == 1:
                return "{0} defeated {1} | {2}, {3}, {4}, {5}, {6}".format(self.p1, self.p2, self.p1_sets[0], self.p1_sets[1], self.p1_sets[2], self.p1_sets[3], self.p1_sets[4])

            elif self.p2_wins - self.p1_wins == 3:
                return "{0} defeated {1} | {2}, {3}, {4}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1], self.p2_sets[2])
            elif self.p2_wins - self.p1_wins == 2:
                return "{0} defeated {1} | {2}, {3}, {4}, {5}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1], self.p2_sets[2], self.p2_sets[3])
            elif self.p2_wins - self.p1_wins == 1:
                return "{0} defeated {1} | {2}, {3}, {4}, {5}, {6}".format(self.p2, self.p1, self.p2_sets[0], self.p2_sets[1], self.p2_sets[2], self.p2_sets[3], self.p2_sets[4])

    def win_set(self, player, set_num, points1, points2):
        if self.p1 == player:
            self.p1_wins = self.p1_wins + 1
            self.p1_sets[set_num - 1] = points1 + '-' + points2
            self.p2_sets[set_num - 1] = points2 + '-' + points1

        else:
            self.p2_wins = self.p2_wins + 1
            self.p2_sets[set_num - 1] = points1 + '-' + points2
            self.p1_sets[set_num - 1] = points2 + '-' + points1
