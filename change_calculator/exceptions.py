class Error(Exception):
    """Base class for all exceptions raised by this module."""


class NegativeCoinError(Error):
    """A coin with a negative value was found."""


class NegativeCountError(Error):
    """A coin count with a negative value was found."""


class NegativeChangeAmountError(Error):
    """The requested change amount was negative."""


class CalculationError(Error):
    """The amount requested could not be calculated from the coins provided."""


class ChangeAmountTooLargeError(Error):
    """The requested change amount was too large."""


class CoinTooLargeError(Error):
    """A coin with a value too large was found."""


class FloatTooLargeError(Error):
    """The total 'float' is too large."""
