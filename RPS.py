# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
last_play = ['R']
play_order = {
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0
            }
play_count = 0
strategy = ""
ideal_plays = {'R':'P', 'P': 'S', 'S': 'R'}

def player(prev_play, opponent_history=[]):
    global last_play, play_count, strategy, play_order

    if play_count >= 1000:
        play_count = 0
        strategy = ""
        last_play = ['R']
        play_order = {
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0
        }
    
    opponent_history.append(prev_play)

    guess = last_play[-1]
    while guess == last_play[-1]:
        guess = random.choice(['R', 'P', 'S'])

    if play_count >= 20 and play_count % 50 == 0:
        if "PPSRRPPSR" in "".join(opponent_history[-10:]):
            strategy = "quincy"
        else:
            last_ten = last_play[-10:]
            last_opponent_ten = opponent_history[-10:]
            isKris = True
            for i in range(1,10):
                if ideal_plays[last_ten[i-1]] != last_opponent_ten[i]:
                    isKris = False
            if isKris:
                strategy = "kris"
            else:
                strategy = "abbey"
    
    if strategy == "quincy":
        match prev_play:
            case "R":
                if opponent_history[-2] == "R":
                    guess = "S"
                else:
                    guess = "P"
            case "P":
                if opponent_history[-2] == "P":
                    guess = "R"
                else:
                    guess = "S"
            case "S":
                guess = "P"
    
    elif strategy == "kris":
        last_guess = last_play[-1]
        krisMove = ideal_plays[last_guess]
        guess = ideal_plays[krisMove]
    
    else:
        my_prev_play = last_play[-1]
        possible_combinations = max([(play_order[my_prev_play+move],move) for move in ['R', 'P', 'S']])
        predicted = ideal_plays[possible_combinations[1]]
        guess = ideal_plays[predicted]

    
    last_play.append(guess)
    play_count += 1

    if play_count > 1:
        play_order[last_play[-2] + guess] += 1

    return guess
