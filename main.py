import random

possible_actions = ["R", "P", "S"]
def use_imput():
    user_action = input("Enter a choice (R:rock, P:paper, S:scissors): ")
    while user_action not in possible_actions:
        user_action = input("Invalid choice, choice available (R:rock, P:paper, S:scissors): ")
    return user_action

def computer_imput():
    return random.choice(possible_actions)

def my_function(user_action,computer_action):
    if user_action == "R":
        if computer_action == "S":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose.")
    elif user_action == "P":
        if computer_action == "R":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif user_action == "S":
        if computer_action == "P":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")

dic = {
    'R': 'Rock',
    'P': 'Paper',
    'S': 'Scissors'
}

user_action = use_imput()
computer_action= computer_imput()
while user_action == computer_action:
    print(f"Both players selected {dic[user_action]}. It's a tie!")
    user_action= use_imput()
    computer_action = computer_imput()

print(f"\nPlayer({dic[user_action]}), CPU({dic[computer_action]}).\n")
my_function(user_action, computer_action)

    
