from black_jack import GamePlay, CardPlayer

    
first_question = input('Want to play black jack?(y/n)')
if first_question == 'y':
    num_players = input('How many players(2-6)')
    players = {}
    for i in range(int(num_players)):
        first_name = input(f'Input player number {i} first name ')
        last_name = input(f'Input player number {i} last name ')
        previous_wins = input(f'Input player number {i} previous wins ')
        players[i] = CardPlayer(first_name, last_name)
        first_name = ''
        last_name = ''
    my_game = GamePlay(players)
    game_on = True
while game_on:
    for _,player in my_game.players.items():
        card_1 = my_game.deal_card()
        card_2 = my_game.deal_card()
        player.cards.append(card_1)
        player.cards.append(card_2)
        player.hand([card_1,card_2])
        print(player.first_name, f'Your current score is {player.score}')
        hit = input("Do you want another card?(y/n)")
        if hit == 'y' and player.score <= 21:
            pass
            

                