from abstractPokemone import AbstractPokemon

class Attacker(AbstractPokemon):
    def __init__(self, current_stat, level, name):
        super.__init__(self,current_stat, level, name)