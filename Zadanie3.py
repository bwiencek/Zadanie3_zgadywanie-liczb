#python program in which user picks a number from the range between 1 and 1000 and computer guess this number in 10 tries.

#function that gives user input
def user_input():
    possible_input = ["to small", "to big", "you win"]
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['to small', 'to big', 'you win']")
    return user_answer

#main function - guessing game where computer quess
def guess_the_number():
    print("Imagine number between 0 and 1000!")
    print("Press 'Enter' to continue")
    input()
    min_number = 0
    max_number = 1000
    user_answer = ""
    while user_answer != "you win":
        guess = (max_number - min_number) // 2 + min_number
        print(f"Your number is: {guess}")
        user_answer = user_input()
        if user_answer == "to big":
            max_number = guess
        elif user_answer == "to small":
            min_number = guess

    print("Hurra! I guess!")