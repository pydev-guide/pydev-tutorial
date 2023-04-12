from enum import Enum


class SwallowSpecies(str, Enum):
    """Swallow species.

    The species of the swallow. Must be either "african" or "european".

    Attributes
    ----------
    AFRICAN : str
        African swallow.
    EUROPEAN : str
        European swallow.
    """

    AFRICAN = "african"  # non-migratory
    EUROPEAN = "european"  # migratory


class Swallow:
    """Swallow class.

    A bird that can carry cargo and migrate (if European). Note that the
    swallow will be unhappy and go home if it needs to carry more than
    1 pound (about 0.45 kg).

    The cargo cannot have negative weights.

    Parameters
    ----------
    species : str
        The species of the swallow. Must be either "african" or "european".
    cargo_weight : float, optional
        The weight in kg of the cargo carried by the swallow, by default 0.
    """

    def __init__(self, species: str, cargo_weight: float = 0) -> None:
        if cargo_weight < 0:
            raise ValueError("Cargo weight cannot be negative")

        if species.upper() != "AFRICAN" and species.upper() != "EUROPEAN":
            raise ValueError('Species must be either "african" or "european"')

        self.species = SwallowSpecies[species.upper()]
        self._cargo_weight = cargo_weight

    @property
    def cargo_weight(self) -> float:
        """Get the cargo weight.

        Returns
        -------
        float
            The weight of the cargo carried by the swallow.
        """
        return self._cargo_weight

    @cargo_weight.setter
    def cargo_weight(self, value: float) -> None:
        """Set the cargo weight in kg.

        Parameters
        ----------
        value : float
            The weight of the cargo carried by the swallow. Must be positive.

        Raises
        ------
        ValueError
            If the cargo weight is negative.
        """
        if value < 0:
            raise ValueError("Cargo weight cannot be negative")
        self._cargo_weight = value

    def get_speed(self) -> float:
        """Get the velocity of the swallow.

        Note that the velocity becomes negative if the swallow has to carry more
        than one pound (about 0.45 kg).

        Returns
        -------
        float
            The velocity of the swallow in km/h.
        """
        if self.cargo_weight >= 0.45:
            # the swallow is going backward, one pound is too heavy
            return -60.0 / (1 + self._cargo_weight)
        return 60.0 / (1 + self._cargo_weight)

    def is_migratory(self) -> bool:
        """Check if the swallow is migratory.

        European swallows are migratory, while African swallows are not.

        Returns
        -------
        bool
            True if the swallow is migratory, False otherwise.
        """
        return self.species == SwallowSpecies.EUROPEAN
