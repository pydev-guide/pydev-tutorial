import pytest
from pydev_tutorial.swallow import Swallow

# Naive tests
def test_migratory():
    """Test that the European swallow is migratory, while the African swallow is not.
    """
    european_swallow = Swallow(species='european')
    assert european_swallow.is_migratory()

    african_swallow = Swallow(species='african')
    assert not african_swallow.is_migratory()


def test_unladen_velocity():
    """Test that unladen swallows fly at 60 km/h."""
    european_swallow = Swallow(species='european', cargo_weight=0)
    assert european_swallow.get_speed() == 60.0

    african_swallow = Swallow(species='african')
    assert african_swallow.get_speed() == 60.0


# Improve tests using @pytest.mark.parametrize
@pytest.mark.parametrize('species', ['european', 'african'])
@pytest.mark.parametrize('cargo_weight', [0, 0.1, 0.2, 0.3, 0.4])
def test_swallow_velocity(species, cargo_weight):
    """Test that the velocity of the swallow is correct."""
    swallow = Swallow(species=species)
    swallow.cargo_weight = cargo_weight

    # Can you tell why this test is not good?
    assert swallow.get_speed() == pytest.approx(60.0 / (1 + cargo_weight))


@pytest.mark.parametrize('species, is_migratory', [('european', True), ('african', False)])
def test_swallow_migration(species, is_migratory):
    """Test that the European swallow is migratory, while the African swallow is not.
    """
    swallow = Swallow(species=species)
    assert swallow.is_migratory() == is_migratory


# Test for errors
def test_swallow_negative_cargo_weight():
    """Test that the cargo weight cannot be negative."""
    european_swallow = Swallow(species='european')
    with pytest.raises(ValueError):
        european_swallow.cargo_weight = -1


# Add fixtures to be able to reuse cases
# fixtures can be shared across multiple test files by placing them in a conftest.py file
@pytest.fixture
def unhappy_european_swallow():
    """Return an unhappy European swallow.
    
    An unhappy European swallow is one that is carrying more than 0.45 kg.
    
    Returns
    -------
    Swallow
        An unhappy European swallow."""
    return Swallow(species='european', cargo_weight=0.45)


def test_swallow_going_home(unhappy_european_swallow):
    """Test that unhappy European swallows are going home."""
    assert unhappy_european_swallow.get_speed() < 0