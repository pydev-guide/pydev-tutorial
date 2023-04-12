from dataclasses import dataclass
from enum import Enum
from typing import Union


class SwallowSpecies(str, Enum):
    AFRICAN = 'african'
    EUROPEAN = 'european'


class Swallow:

    def __init__(self, species: str, cargo_weight: float = 0) -> None:
        if cargo_weight < 0:
            raise ValueError('Cargo weight cannot be negative')
        
        if species.upper() != 'AFRICAN' and species.upper() != 'EUROPEAN':
            raise ValueError('Species must be either "AFRICAN" or "EUROPEAN"')

        self.species = SwallowSpecies[species.upper()]
        self._cargo_weight = cargo_weight

    @property
    def cargo_weight(self):
        return self._cargo_weight
    
    @cargo_weight.setter
    def cargo_weight(self, value):
        if value < 0:
            raise ValueError('Cargo weight cannot be negative')
        self._cargo_weight = value

    def get_speed(self):
        if self.cargo_weight >= 0.45:
            # the swallow is going backward, one pound is too heavy
            return - 60. / (1 + self._cargo_weight)
        return 60. / (1 + self._cargo_weight)
    
    def is_migratory(self):
        return self.species == SwallowSpecies.EUROPEAN