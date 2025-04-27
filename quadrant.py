def quadrant(x, y):
    if x > 0 and y > 0:
        return 1  # I ćwiartka
    elif x < 0 and y > 0:
        return 2  # II ćwiartka
    elif x < 0 and y < 0:
        return 3  # III ćwiartka
    elif x > 0 and y < 0:
        return 4  # IV ćwiartka
    else:
        return 0  # Punkt leży na osi (x=0 lub y=0)
print(quadrant(-4, 8))
