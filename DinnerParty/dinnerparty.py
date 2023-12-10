"""The Dinnerparty project"""

import random

friends_join = int(input("Enter the number of friends joining (including you):"))


def check_total_friends():
    """Checking total amount of friends. If lenght of friends_dict lower than friends_join, adding new friend trough
    friend_name = input(), then adding new values to friends_dict dictionary.

        Parameters:
        None

        Returns:
        list: returns the total_friends list
        dict: friends_dict with values and keys

       """
    while len(friends_dict) < friends_join:
        friend_name = input()
        total_friends.append(friend_name)
        friends_dict[friend_name] = 0


def choose_lucky_one():
    """If selected Yes: randomly choose one of friends in lucky_one, print message, then set value to lucky friend to 0,
    then distribute total amount between all remaining friends.
        If selected No: no lucky friend, distributing total amount between all friends.
        If selected something else: print "Enter correct answer",  then selecting again, until Yes or No.

        Parameters:
        None

        Returns:
        dict: updated friends_dict

       """
    while True:
        global lucky
        if lucky == "Yes":
            lucky_one = random.choice(list(friends_dict.keys()))
            print(f"{lucky_one} is the lucky one!")
            total_friends_lenght = len(total_friends) - 1
            friend_amount = total_amount / total_friends_lenght
            friend_amount = round(friend_amount, 2)
            for friend in friends_dict:
                if friend == lucky_one:
                    friends_dict[friend] = 0
                else:
                    friends_dict[friend] = friend_amount
            print(friends_dict)
            break
        elif lucky == "No":
            print("No one is going to be lucky")
            friend_amount = total_amount / len(total_friends)
            friend_amount = round(friend_amount, 2)
            for friend in friends_dict:
                friends_dict[friend] = friend_amount
            print(friends_dict)
            break
        else:
            if lucky not in ["Yes", "No"]:
                print("Enter correct answer")
                lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No: \n ")


if friends_join < 1:
    print("No one is joining for the party")
else:
    friends_dict = {}
    total_friends = []
    print("Enter the name of every friend (including you), each on a new line:")
    check_total_friends()
    total_amount = int(input("Enter the total amount: \n"))
    lucky = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No: \n ")
    choose_lucky_one()
