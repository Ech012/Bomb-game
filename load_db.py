import pandas
import copy

#saving the data of the matrix
def save_data_game(game_matrix, matrix_with_bombs, matrix_with_bushes, level):

    db = pandas.DataFrame(game_matrix)
    bombs = pandas.DataFrame(matrix_with_bombs)
    bushes = pandas.DataFrame(matrix_with_bushes)

    db.insert(0, 'key', [f"row {i}" for i in range(len(game_matrix))])

    db.to_csv(f"data_{level}.csv", index=False, header=False)
    bombs.to_csv(f"bombs_{level}.csv", index=False, header=False)
    bushes.to_csv(f"bushes_{level}.csv", index=False, header=False)



#returng a matrix of the wanted level
def load_data_game(level):
    df = pandas.read_csv(f"data_{level}.csv", header=None)
    bombs = pandas.read_csv(f"bombs_{level}.csv", header=None)
    bushes = pandas.read_csv(f"bushes_{level}.csv", header=None)
    matrix = df.values.tolist()
    bombs = bombs.values.tolist()
    bushes = bushes.values.tolist()
    for i in range(len(matrix)):
        matrix[i].pop(0)

    return matrix, bombs, bushes



