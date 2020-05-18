#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random
import numpy as np
from IPython.display import clear_output
import time
import math

def create_board(n=5):
    
    board = np.zeros([n, n], dtype=int)
    board = random_spawn(board, n)
    return board

def random_spawn(board, n=5):
    
    selections = list(zip(*np.where(board==0)))
    selection = random.choice(selections)
    spawn_choice = (2,)
    if n>4:
        spawn_choice = (2, 4)
    if board[selection] == 0:
        board[selection] = random.choice(spawn_choice)
    return board

def move(board, player_choice, n=5, w=2048):
    
    skip_check = 0
    spawn_check = 0
    
    if player_choice == 'w' or player_choice == 'W':
        for second_iteration in range(n):
            for first_iteration in range(n):
                for j in range(n):
                    for i in range(n):
                        if board[i][j] == 0 and i<(n-1) and board[i+1][j] != 0:
                            board[i][j] = board[i+1][j]
                            board[i+1][j] = 0
                            spawn_check = 1
            if second_iteration == 0:
                for j in range(n):
                    for i in range(n):
                        if skip_check == 1:
                            skip_check = 0
                            continue
                        if board[i][j] != 0 and i<(n-1) and board[i+1][j] == board[i][j]:
                            board[i][j] = board[i+1][j] + board[i][j]
                            board[i+1][j] = 0
                            skip_check = 1
                            spawn_check = 1

    elif player_choice == 'a' or player_choice == 'A':
        for second_iteration in range(n):
            for first_iteration in range(n):
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == 0 and j<(n-1) and board[i][j+1] != 0:
                            board[i][j] = board[i][j+1]
                            board[i][j+1] = 0
                            spawn_check = 1
            if second_iteration == 0:
                for i in range(n):
                    for j in range(n):
                        if skip_check == 1:
                            skip_check = 0
                            continue
                        if board[i][j] != 0 and j<(n-1) and board[i][j+1] == board[i][j]:
                            board[i][j] = board[i][j+1] + board[i][j]
                            board[i][j+1] = 0
                            skip_check = 1
                            spawn_check = 1

    elif player_choice == 's' or player_choice =='S':
        for second_iteration in range(n):
            for first_iteration in range(n):
                for j in range(n):
                    for i in reversed(range(n)):
                        if board[i][j] == 0 and i>0 and board[i-1][j] != 0:
                            board[i][j] = board[i-1][j]
                            board[i-1][j] = 0
                            spawn_check = 1
            if second_iteration == 0:
                for j in range(n):
                    for i in reversed(range(n)):
                        if skip_check == 1:
                            skip_check = 0
                            continue
                        if board[i][j] != 0 and i>0 and board[i-1][j] == board[i][j]:
                            board[i][j] = board[i-1][j] + board[i][j]
                            board[i-1][j] = 0
                            skip_check = 1
                            spawn_check = 1

    elif player_choice == 'd' or player_choice == 'D':
        for second_iteration in range(n):
            for first_iteration in range(n):
                for i in range(n):
                    for j in reversed(range(n)):
                        if board[i][j] == 0 and j>0 and board[i][j-1] != 0:
                            board[i][j] = board[i][j-1]
                            board[i][j-1] = 0
                            spawn_check = 1
            if second_iteration == 0:
                for i in range(n):
                    for j in reversed(range(n)):
                        if skip_check == 1:
                            skip_check = 0
                            continue
                        if board[i][j] != 0 and j>0 and board[i][j-1] == board[i][j]:
                            board[i][j] = board[i][j-1] + board[i][j]
                            board[i][j-1] = 0
                            skip_check = 1
                            spawn_check = 1
                            
    send = (board, spawn_check)
    return send

def check_win(board, n=5, w=2048):
    
    adjacent_equals_check = 0
    if any(z == w for z in np.nditer(board)) == True:
        print("\nYou won !\n")
        return 1
    
    for i in range(n):
        for j in range(n):
            if j<(n-1) and board[i][j] == board[i][j+1]:
                adjacent_equals_check = 1
                return 0
            elif i<(n-1) and board[i][j] == board[i+1][j]:
                adjacent_equals_check = 1
                return 0
    
    selections = list(zip(*np.where(board==0)))
    if not selections and adjacent_equals_check == 0:
        print("\nGame over, you lost\n")
        return -1
    
    return 0
                        
def play_game():
    t1 = time.perf_counter()
    
    try:
        print("Enter board size:\n")
        n = int(input())
        if n<1 or type(n)!=int:
            raise ValueError
    except ValueError:
        print("\nInvalid board size entered\n")
        n = 5
        print("Board size has been set to 5")
    try:
        print("\nEnter winning value:\n")
        w = int(input())
        if w%2 != 0 or type(w)!=int:
            raise ValueError
    except ValueError:
        print("\nInvalid winning value entered\n")
        w = 2048
        print("Winning value has been set to 2048\n")
    print("Enter any key to continue\n")
    continue_choice = input()
    board = create_board(n)
    player_choice = 'q'
    result = 0
    moves_count = 0
    invalid_check = 0
    restart_check = 0
    spawn_check = 0
    attempts = 0
    valid_moves = ('w', 'a', 's', 'd', 'W', 'A', 'S', 'D')
    while result == 0:
        clear_output()
        if invalid_check == 1:
            print("\nInvalid move, enter move again\n")
            invalid_check = 0
        if restart_check == 1:
            print("\nYou have cleared the board\n")
            board = create_board(n)
            t1 = time.perf_counter()
            moves_count = 0
            restart_check = 0
        print(board)
        result = check_win(board, n, w)
        if result != 0:
            break
        selections = list(zip(*np.where(board==0)))
        if not selections:
            print("\nNo more spaces left\n")
        if (attempts > 0 and moves_count != 0 and spawn_check == 1) and (player_choice == 'Z' or restart_check == 0):
            print("\nEnter next move\n")
        if attempts != 0 and spawn_check == 0 and player_choice != 'r':
            print("\nBoard unchanged, enter some other move\n")
        if moves_count == 0 and player_choice != 'Z' and attempts == 0:
            print("\nYou have the following choices throughout the game:")
            print("\n1. Enter move\n2. Press n to stop\n3. Press r to clear board\n")
            t1 = time.perf_counter()
        player_choice = input()
        if player_choice in valid_moves:
            attempts = attempts + 1
            received = move(board, player_choice, n, w)
            (board, spawn_check) = received
            if spawn_check == 1:
                board = random_spawn(board, n)
                moves_count = moves_count + 1
        elif player_choice == 'n' or player_choice == 'N':
            print("\nYou have stopped the game\n")
            break
        elif player_choice == 'r' or player_choice == 'R':
            restart_check = 1
        elif player_choice == 'Z':
            selections = list(zip(*np.where(board==0)))
            for multiple_spawns in range(len(selections)):
                board = random_spawn(board, n)
            moves_count = moves_count + 1
            attempts = attempts + 1
        else:
            invalid_check = 1

    t2 = time.perf_counter()
    print("\nGame stats:")
    print("Number of valid moves made for current board : ", moves_count)
    print("Number of total moves played throughout the session : ", attempts)
    
    seconds_spent = t2-t1
    minutes_spent = 0
    if seconds_spent > 60:
        minutes_spent = int(seconds_spent / 60)
        seconds_spent = int(math.remainder(seconds_spent, 60))
    print ("Time spent on current board : ", minutes_spent, " minute(s) and ", round(seconds_spent), " second(s)")
        
play_game()

