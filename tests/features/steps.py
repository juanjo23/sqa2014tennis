# -*- coding: utf-8 -*-
from lettuce import *
import app.match as m


@step(u'Given: "([^"]*)" and "([^"]*)" start a match to "([^"]*)" sets')
def given_players_and_player2_start_match_to_num_sets(step, player1, player2, sets):
    world.match = m.Match(player1, player2, int(sets))


@step(u'Then: I see score: "([^"]*)"')
def then_i_see_score_group1(step, score):
    assert world.match.score() == score, \
        "Got %s " % world.match.score()


@step(u'When: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def when_player_won_the_numberOfSet_set_p1_p2(step, player, set_number, p1, p2):
    world.match.win_set(player, int(set_number[0]), p1, p2)


@step(u'And: "([^"]*)" won the "([^"]*)" set "([^"]*)"-"([^"]*)"')
def and_player_won_the_numberOfSet_set_p1_p2(step, player, set_number, p1, p2):
    world.match.win_set(player, int(set_number[0]), p1, p2)


@step(u'Then: The match score is: "([^"]*)"')
def then_the_match_score_is_group1(step, score):
    assert world.match.score() == score, \
        "Got %s " % world.match.score()
