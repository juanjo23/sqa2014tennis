# -*- coding: utf-8 -*-
class Match:

    def __init__(self, player1, player2, pacted_sets):
        s = self
        s.p1 = player1
        s.p2 = player2
        s.pacted_sets = pacted_sets
        s.p1_wins = 0
        s.p2_wins = 0
        s.p1s = ['', '', '', '', '']
        s.p2s = ['', '', '', '', '']

    def score(s):
        if s.p1_wins == 0 and s.p2_wins == 0:
            return "{0} plays with {1} | 0-0".format(s.p1, s.p2)

        # Pacted sets: 3
        if s.pacted_sets == 3:
            if s.p1_wins - s.p2_wins == 2:
                return "{0} defeated {1} | {2}, {3}".format(s.p1, s.p2, s.p1s[0], s.p1s[1])
            elif s.p1_wins - s.p2_wins == 1:
                return "{0} defeated {1} | {2}, {3}, {4}".format(s.p1, s.p2, s.p1s[0], s.p1s[1], s.p1s[2])
            elif s.p2_wins - s.p1_wins == 2:
                return "{0} defeated {1} | {2}, {3}".format(s.p2, s.p1, s.p2s[0], s.p2s[1])
            elif s.p2_wins - s.p1_wins == 1:
                return "{0} defeated {1} | {2}, {3}, {4}".format(s.p2, s.p1, s.p2s[0], s.p2s[1], s.p2s[2])

        # Pacted sets: 5
        elif s.pacted_sets == 5:
            if s.p1_wins - s.p2_wins == 3:
                return "{0} defeated {1} | {2}, {3}, {4}".format(s.p1, s.p2, s.p1s[0], s.p1s[1], s.p1s[2])
            elif s.p1_wins - s.p2_wins == 2:
                return "{0} defeated {1} | {2}, {3}, {4}, {5}".format(s.p1, s.p2, s.p1s[0], s.p1s[1], s.p1s[2], s.p1s[3])
            elif s.p1_wins - s.p2_wins == 1:
                return "{0} defeated {1} | {2}, {3}, {4}, {5}, {6}".format(s.p1, s.p2, s.p1s[0], s.p1s[1], s.p1s[2], s.p1s[3], s.p1s[4])

            elif s.p2_wins - s.p1_wins == 3:
                return "{0} defeated {1} | {2}, {3}, {4}".format(s.p2, s.p1, s.p2s[0], s.p2s[1], s.p2s[2])
            elif s.p2_wins - s.p1_wins == 2:
                return "{0} defeated {1} | {2}, {3}, {4}, {5}".format(s.p2, s.p1, s.p2s[0], s.p2s[1], s.p2s[2], s.p2s[3])
            elif s.p2_wins - s.p1_wins == 1:
                return "{0} defeated {1} | {2}, {3}, {4}, {5}, {6}".format(s.p2, s.p1, s.p2s[0], s.p2s[1], s.p2s[2], s.p2s[3], s.p2s[4])

    def win_set(s, player, set_num, points1, points2):
        if s.p1 == player:
            s.p1_wins = s.p1_wins + 1
            s.p1s[set_num - 1] = points1 + '-' + points2
            s.p2s[set_num - 1] = points2 + '-' + points1

        else:
            s.p2_wins = s.p2_wins + 1
            s.p2s[set_num - 1] = points1 + '-' + points2
            s.p1s[set_num - 1] = points2 + '-' + points1
