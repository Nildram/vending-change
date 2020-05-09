"""
This module provides a means to calculate change of a specified
amount given a limited set of coins.

The exported class ChangeCalculator provides the API interface
for this module.
"""
from .change_calculator import ChangeCalculator
from .change_calculators import ChangeCalculators
from .exceptions import (CalculationError, Error, NegativeChangeAmountError,
                         NegativeCoinError, NegativeCountError)
