import time
import random

list = [1,2,3,4,5,6,7,8,9]

def display():
    print("-------+-----+------") 
    for i in range(len(list)):
        if list[i] % 3 == 0:
            print(" | " + str(list[i])+ " | ")
            print("-------+-----+------") 
        elif list[i] % 3 != 0:
            print(" | " + str(list[i]) + " | ", end="") 
        else:
            print(list[i], end="")

    print()


def input(type):
    if(type == "o"):
        tgt = int(input("0~8の座標を入れてください: "))
    else:
        tgt = random.randint(0,8)

    if(list[tgt] == 'o' or list[tgt] == 'x'):
        input(type)
    else:
        list[tgt] = type

def winner():
    lines = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9],
      [1, 5, 9],
      [3, 5, 7],
    ]
    for i in range(0, len(lines)):
        [a, b, c] = lines[i]
        if list[a] and list[a] == list[b] and list[a] == list[c]: 
            return list[a]
    return None

display()

for turn in range(0,8):
    if(turn %2 == 0) : 
        print("You")
        input("o")
    else: 
        print("CPU")
        input("x")

    display() 

    if winner(): 
        print(winner() + "の勝ち")
        break

    if turn == 8: 
        print("引き分け")
        break