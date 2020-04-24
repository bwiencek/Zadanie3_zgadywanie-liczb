#python program in which user picks a number from the range between 1 and 1000 and computer guess this number in 10 tries.

#function that
def user_input():
    possible_input = ["to small", "to big", "you win"]
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['to small', 'to big', 'you win']")
    return user_answer