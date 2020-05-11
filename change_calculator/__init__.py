"""
This module provides a means to calculate change of a specified
amount given a limited set of coins.

The exported class ChangeCalculator provides the API interface
for this module.
"""
from .calculators import Calculators
from .change_calculator import ChangeCalculator
from .exceptions import (CalculationError, Error, FloatTooLargeError,
                         InvalidChangeAmountError, InvalidCoinError,
                         InvalidCountError)
