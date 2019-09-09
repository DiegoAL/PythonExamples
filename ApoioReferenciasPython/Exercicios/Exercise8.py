'''
Make a two-player Rock-Paper-Scissors game,
compare them, print out a message of congratulations to the winner, 
and ask if the players want to start a new game

(Hint: Ask for player plays (using input).

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
'''
#var
_player1 = ""
_palyer2 = ""
_options = ["rock", "scissors", "paper"]
 
#logic
print("Let's start a Rock-Paper-Scissors game....\n")
while True:
    _player1 = input("Player 1 type a option: ").lower()
    _player2 = input("Player 2 type a option: ").lower()
    
    if _player1 not in _options or _player2 not in _options :
        print("\nThere are some option invalid! Try again...\n")
    else:
        if _player1 == _player2:
            print("occurred a draw, try again...\n")
            
        elif _player1 == "rock" and _player2 == "scissors":
            print("Player 1 Win")
            break
            
        elif _player1 == "scissors" and _player2 == "paper":
            print("Player 1 Win")
            break
        
        elif _player1 == "paper" and _player2 == "rock":
            print("Player 1 Win")
            break
                
        else:
            print("Player 2 Win")
            break
