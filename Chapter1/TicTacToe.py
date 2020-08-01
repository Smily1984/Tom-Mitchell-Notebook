# Basic TicTacToe implementation
#!/bin/python3

import math
import os
import random
import re
import sys
import copy

cache = {}

def get_winner(state):
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] and \
        (state[i][0] == 'O' or state[i][0] == 'X'):
            return state[i][0]
        if state[0][i] == state[1][i] == state[2][i] and \
        (state[0][i] == 'O' or state[0][i] == 'X'):
            return state[0][i]
    if state[0][0] == state[1][1] == state[2][2] and \
    (state[0][0] == 'O' or state[0][0] == 'X'):
        return state[0][0]
    if state[0][2] == state[1][1] == state[2][0] and \
    (state[0][2] == 'O' or state[0][2] == 'X'):
        return state[0][2]
    return '_'

def flip_player(player):
    if player == 'X':
        return 'O'
    elif player == 'O':
        return 'X'

def get_tup(i, j, player, state):
    tup = []
    for row in state:
        tup.append(tuple(row))
    return (i, j, player, tuple(tup))

def get_score(move, i, j, player, state):
    global cache
    tup = get_tup(i, j, player, state)
    if tup in cache:
        return cache[tup]
    state = copy.deepcopy(state)
    state[i][j] = player
    winner = get_winner(state)
    score = -math.inf
    if winner == player:
        score = 100
    elif winner == '_' and move <= 8:
        max_score = -math.inf
        for l in range(3):
            for m in range(3):
                if state[l][m] == '_':
                    max_score = max(max_score, get_score(move + 1, l, m, flip_player(player), state))
        score = -max_score if max_score != -math.inf else 0
    elif winner == '_' and move > 8:
        score = 0
    else:
        score = -100
    cache[tup] = score
    return score

def get_move(player, state):
    max_score = -math.inf
    max_i = None
    max_j = None
    for i in range(3):
        for j in range(3):
            if state[i][j] == '_':
                current_score = get_score(0, i, j, player, state)
                if current_score > max_score:
                    max_score = current_score
                    max_i = i
                    max_j = j
    return (max_i, max_j)

def print_state(state):
    for row in state:
        print(row)

def console_interface():
    print("Press 1 for Alpha-Beta Vs Alpha-Beta")
    print("Press 2 for Human Vs Alpha-Beta")
    inp_choice = int(input())
    print("Chose symbol for player 1 ('X' or 'O')")
    inp_symbol = input() 
    assert inp_symbol == 'X' or inp_symbol == 'O'
    print("Chose who plays first ('X' or 'O')")
    player1 = input()
    assert player1 == 'X' or player1 == 'O'
    if inp_choice == 1:
        state = [['_' for _ in range(3)] for _ in range(3)]
        i = None
        j = None
        winner = None
        cnt = 0
        while True:
            if winner != None and i != None and j != None and cnt < 9:
                print("{} has made the move. Now {}'s turn".format(player1, flip_player(player1)))
                print()
            i, j = get_move(player1, state)
            winner = get_winner(state)
            cnt += 1
            if not (i != None and j != None and winner == '_'):
                break            
            state[i][j] = player1
            print_state(state)
            winner = get_winner(state)
            if not (i != None and j != None and winner == '_'):
                break            
            player1 = flip_player(player1)
        print("Winner is %s" % winner if winner != "_" else "It's a draw")
    if inp_choice == 2:
        state = [['_' for _ in range(3)] for _ in range(3)]
        i = None
        j = None
        winner = None
        cnt = 0
        while True:
            if winner != None and i != None and j != None and cnt < 9:
                print("{} has made the move. Now {}'s turn".format(player1, flip_player(player1)))
                print()
            i, j = get_move(player1, state) if cnt % 2 == 1 else (int(input("Enter Row Number ")) - 1, int(input("Enter Column Number ")) - 1)
            winner = get_winner(state)
            cnt += 1
            if not (i != None and j != None and winner == '_'):
                break                        
            state[i][j] = player1
            print_state(state)
            winner = get_winner(state)
            if not (i != None and j != None and winner == '_'):
                break            
            player1 = flip_player(player1)
        print("Winner is %s" % winner if winner != "_" else "It's a draw")

if __name__ == '__main__':
    console_interface()