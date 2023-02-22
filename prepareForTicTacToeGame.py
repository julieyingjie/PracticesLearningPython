# print([1, 2, 3])
# print([4, 5, 6])
# print([7, 8, 9])
#
#
# def display(row1, row2, row3):
#     print(row1)
#     print(row2)
#     print(row3)
#
#
# #
# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']
#
# display(row1, row2, row3)
#
# row2[1] = 'X'
#
# display(row1, row2, row3)
#
# result = input("Please enter a value: ")
#
# print(type(result))
#
# result_int = int(result)
#
# print(type(result_int))
#
# print(type(2.3))
#
# print(float("3.14"))

# position_index = int(input("Choose an index position: "))
#
# print(type(position_index))
#
# print(row2[position_index])
#


# game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)


#
# display_game(game_list)
#
def position_choice():
    choice = "wrong"

    while choice not in ['0', '1', '2']:

        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice! ")

    return int(choice)


#
# print(position_choice())
#
#
def replacement_choice(game_list, position):
    user_placement = input("Type a string to place at position: ")
    game_list[position] = user_placement

    return game_list


#
# print(replacement_choice(game_list, position_choice()))


def gameon_choice():
    choice = 'WRONG'

    while choice not in ['Y', 'N']:

        choice = input("Keep playing? (Y/N) ")

        if choice not in ['Y', 'N']:
            print("Sorry, I don't understand, please choose Y or N ! ")

    if choice == 'Y':
        return True
    else:
        return False


game_on = True
game_list = [0, 1, 2]

while game_on:
    display_game(game_list)

    position = position_choice()

    game_list = replacement_choice(game_list, position)

    display_game(game_list)

    game_on = gameon_choice()
