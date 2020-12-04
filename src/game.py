from black_jack import GamePlay, CardPlayer, Dealer


def dict_players(num_players):
    players = []
    for i in range(int(num_players)):
        first_name = input(f'Input player number {i} first name ')
        last_name = input(f'Input player number {i} last name ')
        previous_wins = input(f'Input player number {i} previous wins ')
        players.append(CardPlayer(first_name, last_name,previous_wins))
        first_name = ''
        last_name = ''
    return players


first_question = input('Want to play black jack?(y/n)')
if first_question == 'y':
    num_players = input('How many players(2-6)')
    players = dict_players(num_players)
    dealer = Dealer('Bob', 'Ross',0)
    my_game = GamePlay(players, dealer)
    game_on = True
while game_on:
    dealer.cards = [my_game.deal_card() for _ in range(2)]
    dealer.hand()
    for player in my_game.players:
        play_bool = True
        player.cards = [my_game.deal_card() for _ in range(2)]
        player.hand()
        print(f'the dealers score is {dealer.score}')
        while play_bool:
            print(player.first_name, f', your current score is {player.score}')
            hit = input("Do you want another card?(y/n)")
            if hit == 'y' and player.score <= 21:
                player.cards.append(my_game.deal_card())
                player.hand()
            if hit =='n':
                play_bool = False
            if player.score > 21:
                print(player.first_name, f', your current score is {player.score}')
                print('You lost')
                players = False
                break
    dealer_must = True
    while dealer_must:
        if my_game.dealer_must():
            dealer.cards.append(my_game.deal_card())
            dealer.hand()
            print(f'the dealer took another card and his score is now {dealer.score}')
        else:
            dealer_must = False
        
        if dealer.score == 21:
            print('Dealer won')
            # calculate who won
        else:
            for player in my_game.players:
                print(f'The dealer had a score of {dealer.score}')
                print(f'you , {player.first_name} had a score of {player.score}')

    game_on = False    
            
            

                