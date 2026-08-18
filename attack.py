import re

import pandas as pd
import random
from consts import *
from Screen import *

def save_plain_forge(file_name):
    try:
        df = pd.read_csv(file_name, header=None)
        matrix = df.astype(int).values.tolist()
        consts_list = (EMPTY_BLOCK, FLAG, BOMB, BUSH, SOLDIER, GUARD, TELEPORT)

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] != EMPTY_BLOCK:
                    matrix[row][col] = EMPTY_BLOCK
                elif matrix[row][col] == EMPTY_BLOCK:
                    matrix[row][col] = random.choice(consts_list)

        df_updated = pd.DataFrame(matrix)
        df_updated.to_csv(file_name, index=False, header=False)

        print(f"The file '{file_name}' was successfully updated and saved in the project folder!")
        return matrix

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found in the folder. Ensure the name and extension are correct.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def teleport_to_flag_hack(file_name,terrain):
    df = pd.read_csv(file_name, header=None)
    matrix = df.values.tolist()
    current_row, current_col = get_soldier_position(matrix)
    for r in range(current_row, current_row + 4):
        for c in range(current_col, current_col + 2):
            matrix[r][c] = terrain[r][c]

    new_row = 21
    new_col = 46
    for r in range(new_row, new_row + 4):
        for c in range(new_col, new_col + 2):
            matrix[r][c] = SOLDIER
    df_updated = pd.DataFrame(matrix)
    df_updated.to_csv(file_name, index=False, header=False)

def brute_force_key ():
    file = open('keywords.txt', 'r')
    clean_text = file.readlines()
    new_l = [i.strip() for i in clean_text]
    if SECRET in new_l:
        print("The key is on the list")
    else:
        print("The key is not on the list")

