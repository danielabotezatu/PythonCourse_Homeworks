import numpy as np
import time

matrix = np.array((["1","2","3"], ["4", "5", "6"], ["7","8", "9"]))
empty_places = 9
robot = "Robot"

def robot_choice(matrix):
    global empty_places
    choice = 5
    if matrix[(choice - 1) // 3][(choice - 1) % 3] != ("X" or "0"):
        matrix[(choice - 1) // 3][(choice - 1) % 3] = 0
        empty_places -= 1
        return matrix

    for choice in [1, 3, 7, 9]:
        if matrix[(choice - 1) // 3][(choice - 1) % 3] != ("X" or "0"):
            matrix[(choice-1)//3][(choice-1)%3] = 0
            empty_places -= 1
            return matrix
    for choice in [2, 4, 6, 8]:
        if matrix[(choice - 1) // 3][(choice - 1) % 3] != ("X" or "0"):
            matrix[(choice-1)//3][(choice-1)%3] = 0
            empty_places -= 1
            break
    return matrix


def person_choice(matrix):
    global empty_places
    while True:
        while True:
            choice = input("Introduceti pozitia: ")
            try:
                choice = int(choice)
                choice -= 1
                break
            except ValueError:
                print("Nu ati introdus date corecte")

        if matrix[choice // 3][choice % 3] == ("X" or "0"):
            print("Pozitia aleasa nu este libera!")
            continue

        else:
            matrix[choice // 3][choice % 3] = 'X'
            empty_places -= 1
            break

    return matrix

def winner(matrix, person_name):

    if all(matrix[:,0] == "X") or all(matrix[:,1] == "X") or all(matrix[:,2] == "X") or all(matrix[0,:] == "X") or all(matrix[1,:] == "X") or all(matrix[2,:] == "X"):
        the_winner = person_name
        return the_winner
    elif all(np.fliplr(matrix).diagonal() == "X") or all(np.diagonal(matrix) == "X"):
        the_winner = person_name
        return the_winner
    elif all(matrix[:,0] == "0") or all(matrix[:,1] == "0") or all(matrix[:,2] == "0") or all(matrix[0,:] == "0") or all(matrix[1,:] == "0") or all(matrix[2,:] == "0"):
        the_winner = robot
        return the_winner
    elif all(np.fliplr(matrix).diagonal() == "0") or all(np.diagonal(matrix) == "0"):
        the_winner = robot
        return the_winner
    return False

def modelare_matrix(matrix):
    string = "\n"
    for line in range(len(matrix)-1):
        string += "  |  ".join(matrix[line])
        string += "\n"
        string += "_____________"
        string += "\n"
        string += "             "
        string += "\n"

    string += "  |  ".join(matrix[len(matrix)-1])
    string += "\n"

    return string

def start_Game():

    print("Welcome!")
    time.sleep(.5)
    person_name = input("Introduceti numele dumneavoastra: ")
    print("Ready?")
    time.sleep(.2)
    print("\n")
    print("3!")
    print("\n")
    time.sleep(.5)
    print("2!")
    print("\n")
    time.sleep(.5)
    print("1!")
    print("\n")
    time.sleep(.5)
    print("Go!")
    time.sleep(.6)
    return person_name

def game_Play(matrix):

    person_name = start_Game()

    while empty_places > 0:
        print(modelare_matrix(matrix))
        person_choice(matrix)
        robot_choice(matrix)
        if not winner(matrix, person_name) == False:
            the_winner = winner(matrix, person_name)
            break
    print(modelare_matrix(matrix))
    print("The winner is: ", the_winner)


game_Play(matrix)
