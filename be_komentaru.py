def davai_lentele(g):
    print(f'\n{g[0]}|{g[1]}|{g[2]}\n{g[3]}|{g[4]}|{g[5]}\n{g[6]}|{g[7]}|{g[8]}')


converter = {7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8}
grid = '789456123'
swap = {'X': 'O', 'O': 'X'}
player = 'X'
is_winner = False

while not grid.isalpha():
    davai_lentele(grid)
    key = input('                 ' + player + ': ')
    if grid[converter[int(key)]].isnumeric():
        grid = grid.replace(key, player)
        player = swap[player]
        t = []
        t[:0] = grid
        is_winner = (t[0] == t[1] == t[2]) or (t[3] == t[4] == t[5]) or (t[6] == t[7] == t[8]) or (
                     t[0] == t[3] == t[6]) or (t[1] == t[4] == t[7]) or (t[2] == t[5] == t[8]) or (
                     t[0] == t[4] == t[8]) or (t[2] == t[4] == t[6])
        if is_winner:
            break
    else:
        print(key + ' jau užbraukta! ')

davai_lentele(grid)
if is_winner:
    player = swap[player]
    print(f'\n{player} laimėjo!')
elif grid.isalpha():
    print(f'\nLaimėjo draugystė!')
