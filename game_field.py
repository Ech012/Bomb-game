import consts

matricx_game = []
x =

for row in range(25):
    for col in range(50):
        matricx_game.append(consts.EMPTY_BLOCK)

for row in range (21,23):
    for col in range (46,49):
        matricx_game[row][col] = consts.FLAG

for row in range(25):
    for col in range(50):
        matricx_game[row][col] = randon



