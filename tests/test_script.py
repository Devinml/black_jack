import pytest
import unittest, os, sys
sys.path.append(os.path.abspath('src'))
from black_jack import CardPlayer, GamePlay, Dealer

def test_names():
    dev = CardPlayer('Devin', "Link", 100)
    first_name = dev.first_name
    last_name = dev.last_name
    assert first_name == "devin"
    assert last_name == 'link'

def test_hand():
    dev = CardPlayer('Dev',"Link", 0)
    dev.cards = [['ace', 'diamonds'],['4','hearts']]
    dev.hand()
    assert dev.score == 15
    bob = CardPlayer('BOB',"BUTT")
    bob.cards = [['2', 'diamonds'],['6','hearts']]
    bob.hand()
    assert bob.score == 8


def test_deal_card():
    players = [CardPlayer('Steeve','jim'),CardPlayer('Jimbo','bob')]
    dealer = Dealer('bing', 'bong',0)
    game1 = GamePlay(players, dealer)
    card1 = game1.deal_card()
    suits = ['hearts', 'spades', 'diamonds', 'clubs']
    cards = [str(i) for i in range(2,11) ]
    faces = ['ace', 'king', 'queen', 'jack']
    face_cards = cards + faces
    assert card1[1] in suits
    assert card1[0] in face_cards

def test_dealer_must():
    players = [CardPlayer('Steeve','jim'),CardPlayer('Jimbo','bob')]
    players[0].cards = [['2', 'diamonds'],['6','hearts']]
    players[1].cards = [['ace', 'diamonds'],['4','hearts']]
    players[0].hand()
    players[1].hand()
    dealer = Dealer("Anita", 'Dick', 0)
    dealer.cards = [['2', 'diamonds'],['6','hearts']]
    dealer.hand()
    game1 = GamePlay(players, dealer)
    must_bool =  game1.dealer_must()
    assert must_bool == True
