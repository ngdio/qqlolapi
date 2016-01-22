class Top:
    id = 1
    name = "Top"

class Jungle:
    id = 5
    name = "Jungle"

class Mid:
    id = 2
    name = "Mid"

class ADC:
    id = 3
    name = "ADC"

class Support:
    id = 4
    name = "Support"

ROLES = [Top, Jungle, Mid, ADC, Support]
ROLES_BY_ID = {x.id: x for x in ROLES}