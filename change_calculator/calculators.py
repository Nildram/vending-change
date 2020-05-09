from change_calculator.change_algorithm import ChangeAlgorithm
from change_calculator.change_calculator import ChangeCalculator


class ChangeCalculatorFactory:

    def __init__(self, canonical_coin_system: bool):
        """Factory for creating new ChangeCalculator objects.

        Args:
            canonical_coin_system (bool): Set True if the coin system
                used is considered canonical, else False.
        """
        self.canonical_coin_system = canonical_coin_system

    def __call__(self):
        """Generate a new ChangeCalculator object.

        Returns:
            ChangeCalculator: New ChangeCalculator object.
        """
        return ChangeCalculator(ChangeAlgorithm.create(self.canonical_coin_system))


class Calculators:
    """Simple IoC container for new ChangeCalculator objects."""

    canonical = ChangeCalculatorFactory(canonical_coin_system=True)
    non_canonical = ChangeCalculatorFactory(canonical_coin_system=False)
