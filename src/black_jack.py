from random import randint

class CardPlayer(object):
    def __init__(self,first_name, last_name, wins=0):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.wins = wins
        self.faces = ['ace','king', 'queen', 'jack']
        self.suits = ['hearts',
                      'spades',
                      'clubs',
                      'diamonds']
        self.score = 0
        self.cards = []

    def hand(self, list_of_cards):
        '''
        Calculate hand (not sure if i should do this in game play)
        '''
        for card in self.cards:
            if card[0] == 'ace':
                self.score += 11
            elif card[0] in self.faces:
                self.score += 10
            else: 
                self.score += int(card[0])

class Dealer(CardPlayer):
    def __init__(self, fname, lname, previous_wins):
        super().__init__(fname, lname, previous_wins)


class GamePlay(object):
    def __init__(self,players):
        '''
        players is a dictionary of player objects
        '''
        self.num_players = len(players)
        self.players = players 
        self.faces = ['ace','king', 'queen', 'jack']
        self.suits = ['hearts',
                      'spades',
                      'clubs',
                      'diamonds']
    
    def setup_game(self, play_game_str):
        if play_game_str == 'y':
            pass
    
    def deal_card(self):
        
        numbers = [str(i) for i in range (2,11)]
        face_nums = numbers + self.faces
        suit_rand = randint(0,3)
        face_num_rand = randint(0,12) 
        card = [face_nums[face_num_rand], self.suits[suit_rand]]
        return card
    
    def award_winner(self):
        pass



if __name__ == "__main__":
    my_dealer = Dealer('Cam', "Johnson",0)
    my_player = CardPlayer('Cam', 'Johnson')
    cards = [['2', 'diamonds'],['6','hearts']]
    my_dealer.hand(cards)
    my_player.hand(cards)
    print(my_player.score)
    print(my_dealer.score)
                
                
                
                
