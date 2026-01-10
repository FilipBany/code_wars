def points(games):
    wynik = 0
    for g in games:
        if g[0] > g[2]: wynik += 3
        if g[0] == g[2]: wynik += 1
    return wynik
