import random
def get_choices():
    player_choice=input("Enter a choice (rock,paper,scissors): ")
    options=['rock','paper','sissors']
    computer_choice=random.choice(options)
    choices={'player':player_choice,'computer':computer_choice}
    result=check_win(player_choice,computer_choice)
    return result

def check_win(player,computer):
    print(f"You chose {player}.Computer chose {computer}.")
    if(player==computer):
        return "It's a tie"
    elif player=='rock':
        if computer=='paper':
            return 'paper cover rock.Better luck for next time :)'
        else:
            return 'rock smashes sissors!Congratulation you win!!!'

    elif player=='paper':
        if computer=='rock':
            return 'paper cover rock.Congratulation you win!!!'
        else:
            return 'sissors cut paper! you lose!!!'
    
    elif player=='sissors':
        if computer=='paper':
            return 'sissors cut paper.Congratulation you win!!!'
        else:
            return 'rock smashes sissors! you lose!!!'

print(get_choices())