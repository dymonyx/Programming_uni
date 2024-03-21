from random import randint
guess_number = randint(1, 100)
count = 0
def guessing_game(guess_number, count):
    if count == 10:
        return("попытки кончились =(")
    else:
        guess_people = int(input("попробуйте угадать число: "))
        count += 1
        if guess_people == guess_number:
            return(f'yeah, right! {count}')
        else:
            print("задуманное число больше введенного") if guess_people < guess_number else print("задуманное число меньше введенного")
            return(guessing_game(guess_number, count))

print(guessing_game(guess_number, count))