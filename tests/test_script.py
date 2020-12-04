import pytest
import unittest, os, sys
sys.path.append(os.path.abspath('src'))
from black_jack import CardPlayer, GamePlay

def test_names():
    dev = CardPlayer('Devin', "Link", 100)
    first_name = dev.first_name
    last_name = dev.last_name
    assert first_name == "devin"
    assert last_name == 'link'

def test_hand():
    dev = CardPlayer('Dev',"Link", 0)
    cards = [['ace', 'diamonds'],['4','hearts']]
    dev.hand(cards)
    assert dev.score == 15
    bob = CardPlayer('BOB',"BUTT")
    cards = [['2', 'diamonds'],['6','hearts']]
    bob.hand(cards)
    assert bob.score == 8


def test_deal_card():
    players = [CardPlayer('Steeve','jim'),CardPlayer('Jimbo','bob')]
    game1 = GamePlay(players)
    card1 = game1.deal_card()
    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    cards = [str(i) for i in range(2,11) ]
    faces = ['ace', 'king', 'queen', 'jack']
    face_cards = cards + faces
    assert card1[1] in suits
    assert card1[0] in face_cards