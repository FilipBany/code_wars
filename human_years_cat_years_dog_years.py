def human_years_cat_years_dog_years(h):
    if h == 1:
        c = 15
        d = 15
    if h == 2:
        c = 15 + 9
        d = 15 + 9
    
    if h >= 3:
        c = 15 + 9 + 4 * (h - 2)
        d = 15 + 9 + 5 * (h - 2)
    
    return [h,c,d]
    
    human_years_cat_years_dog_years(6)
