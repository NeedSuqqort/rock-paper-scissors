# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
last_play = ['R']

# for countering abbey's strategy
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
    
    # reset after 1000 plays to adjust to new strategies
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

    # review current strategies every 50 rounds and change if necessary (specifically for mrugesh and abbey)
    if play_count >= 10 and play_count % 50 == 0:
        if "RPPSRRPPSR" in "".join(opponent_history[-10:]):
            strategy = "quincy"
        else:
            last_ten = last_play[-10:]
            last_opponent_ten = opponent_history[-10:]
            isKris = True
            for i in range(1,10):
                if ideal_plays[last_ten[i-1]] != last_opponent_ten[i]:
                    isKris = False
            strategy = "kris" if isKris else "abbey"
    
    # strategy to counter quincy's pattern (RRPPS)
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
    
    # strategy to counter Kris's pattern (ideal response to last play)
    elif strategy == "kris":
        last_guess = last_play[-1]
        krisMove = ideal_plays[last_guess]
        guess = ideal_plays[krisMove]
    
    else:
        if play_count < 10:
            # not enough rounds to determine who the computer is playing against, randomly play but avoid repeating last play
            while guess == last_play[-1]:
                guess = random.choice(['R', 'P', 'S'])
        else:
            # general strategy to counter abbey (and mrugesh) by predicting their guesses based on last 2 rounds
            my_prev_play = last_play[-1]
            possible_combinations = max([(play_order[my_prev_play+move],move) for move in ['R', 'P', 'S']])
            predicted = ideal_plays[possible_combinations[1]]
            guess = ideal_plays[predicted]

    
    last_play.append(guess)
    play_count += 1

    # update play_order for abbey's counter-strategy
    if play_count > 1:
        play_order[last_play[-2] + guess] += 1

    return guess
