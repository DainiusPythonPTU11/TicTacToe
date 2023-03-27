def davai_lentele(g):                                   # Su davai greičiau veikia. Juokauju :)
    print(f'\n{g[0]}|{g[1]}|{g[2]}\n{g[3]}|{g[4]}|{g[5]}\n{g[6]}|{g[7]}|{g[8]}')


# Naudojama įvestam skaičiui konvertuoti į eilės numerį stringe grid.
converter = {7: 0, 8: 1, 9: 2, 4: 3, 5: 4, 6: 5, 1: 6, 2: 7, 3: 8}

# Čia įvedamus skaičius perrašome raidėmis (X/O).
grid = '789456123'

# Naudojama žaidėjo pakeitimui
swap = {'X': 'O', 'O': 'X'}

player = 'X'

is_winner = False



while not grid.isalpha():                               # Tikrina, ar visas grid dar nėra užpildytas raidėmis (X/O).
    davai_lentele(grid)
    key = input('                 ' + player + ': ')

    if grid[converter[int(key)]].isnumeric():           # Tikrina, ar šioje grid vietoje yra įrašytas skaičius.
        grid = grid.replace(key, player)                # Jei taip, į grid vietoje skaičiaus įrašo žaidėjo raidę (X/O).
        player = swap[player]                           # Pakeičia žaidėją.

        t = []
        t[:0] = grid                                    # Aptinka 3 vienodus simbolius:
        is_winner = (t[0] == t[1] == t[2]) or (t[3] == t[4] == t[5]) or (t[6] == t[7] == t[8]) or (    # eilutėse,
                     t[0] == t[3] == t[6]) or (t[1] == t[4] == t[7]) or (t[2] == t[5] == t[8]) or (    # stulpeliuose,
                     t[0] == t[4] == t[8]) or (t[2] == t[4] == t[6])                                   # arba įstrižainėse.
        if is_winner:
            break                                       # Jei aptinka, turime laimėtoją ir ciklą nutraukiame.
    else:
        print(key + ' jau užbraukta! ')                 # Jei anksčiau į grid buvo įrašyta raidė, spausdina pranešimą.

davai_lentele(grid)                                     # Atspausdina paskutinį lentelės variantą.

if is_winner:
    player = swap[player]
    print(f'\n{player} laimėjo!')
elif grid.isalpha():                                    # Jei laimėtojo nėra, o visa lentelė užpildyta raidėmis (X/O).
    print(f'\nLaimėjo draugystė!')
