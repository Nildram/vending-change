"""
This module provides a means to calculate change of a specified
amount given a limited set of coins.

The exported class ChangeCalculator provides the API interface
for this module.
"""
from .change_calculator import (ChangeCalculator, Error,
                               NegativeChangeAmountError, NegativeCoinError,
                               NegativeCountError)