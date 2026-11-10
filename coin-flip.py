"""flips a coin 1000 times, prints the sequence, finds longest streak"""

import random

def flip_1000():
    coins = ['H'] * 500 + ['T'] * 500 #100% 50/50, so the house does not always win :) to increase the amount of coin flips change the numbers and u can rig them too
    random.shuffle(coins)
    return coins

def longest_streak(flips):
    best_char = flips[0]
    best_len = 1
    cur_len = 1

    for i in range(1, len(flips)):
        if flips[i] == flips[i-1]:
            cur_len += 1
            if cur_len > best_len:
                best_len = cur_len
                best_char = flips[i]
        else:
            cur_len = 1

    return best_char, best_len

flips = flip_1000()
print(''.join(flips))
print()

char, length = longest_streak(flips)
name = "Heads" if char == 'H' else "Tails"
print(f"Longest streak: {length}x {name} in a row")
print(f"Total H: {flips.count('H')}  T: {flips.count('T')}")