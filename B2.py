def ar_atlaidi(cena, atlaide=10):
    return cena * (1 - atlaide/100)

print(ar_atlaidi(200))
print(ar_atlaidi(200, 25))
