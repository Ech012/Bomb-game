import pandas
import copy

#saving the data of the matrix
def save_data(matrix, level):

    db = pandas.DataFrame(matrix)
    print(len(matrix))
    db.insert(0, 'key', [f"row {i}" for i in range(len(matrix))])

    db.to_csv(f"data_{level}.csv", index=False, header=False)
    return db


#returng a matrix of the wanted level
def load_data(level):
    df = pandas.read_csv(f"data_{level}.csv", header=None)

    matrix = df.values.tolist()
    matrix_copy = copy.deepcopy(matrix)
    for i in range(len(matrix_copy)):
        matrix[i].pop(0)

    return matrix
