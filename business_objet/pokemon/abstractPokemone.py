from abc import ABC
class AbstractPokemon(ABC):
    def __init__(self, current_stat, level,name):
        self._current_stat=current_stat
        self._level=level
        self._name=name
        