import game
options = ["Rock", "Paper", "Scissor"]
user_choice = game.get_user_choice(options)
if user_choice in options:
    computer_choice = game.get_computer_choice(options)
    game.play_game(user_choice, computer_choice)
#, options)
