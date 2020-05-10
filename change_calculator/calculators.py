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
    """Simple IoC container for creating new ChangeCalculator objects.

    There are two types of ChangeCalculator that can be created:

    canonical: Most efficient for canonical coin systems, but is
        not recommended for non-canonical coin systems as it may
        fail to calculate change for certain combinations of coins
        and amount.
    non_canonical: Recommended for non-canonical coin systems.
    """

    canonical = ChangeCalculatorFactory(canonical_coin_system=True)
    non_canonical = ChangeCalculatorFactory(canonical_coin_system=False)
