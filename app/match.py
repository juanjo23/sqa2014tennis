# -*- coding: utf-8 -*-
class Match:

    def __init__(self, player1, player2, pacted_sets):
        self.p1 = player1
        self.p2 = player2
        self.pacted_sets = pacted_sets
        self.p1_wins = 0
        self.p2_wins = 0
        self.played_sets = 0
        self.p1s = ['', '', '', '', '']
        self.p2s = ['', '', '', '', '']

    def score(self):
        if self.p1_wins == 0 and self.p2_wins == 0:
            return "{0} plays with {1} | 0-0".format(self.p1, self.p2)

        if self.p1_wins > self.p2_wins:
            return self.form_score( self.played_sets, self.p1 )
        else:
            return self.form_score( self.played_sets, self.p2 )
            

    def win_set(self, player, set_num, points1, points2):
        if self.p1 == player:
            self.p1_wins += 1
            self.p1s[set_num - 1] = points1 + '-' + points2
            self.p2s[set_num - 1] = points2 + '-' + points1

        else:
            self.p2_wins += 1
            self.p2s[set_num - 1] = points1 + '-' + points2
            self.p1s[set_num - 1] = points2 + '-' + points1

        self.played_sets += 1

    def form_score(self, cant, who_win):
        lsets = self.p1s if who_win == self.p1 else self.p2s
        if who_win == self.p1:
            score = "{0} defeated {1} | ".format(self.p1, self.p2)
        else:
            score = "{0} defeated {1} | ".format(self.p2, self.p1)

        for i in range(cant):
            score = score + str(lsets[i]) + (", " if cant - 1 != i else "")

        return score
