class Error(Exception):
    """Base class for all exceptions raised by this module."""


class InvalidCoinError(Error):
    """A coin with a negative value was found."""


class InvalidCountError(Error):
    """A coin count with a negative value was found."""


class InvalidChangeAmountError(Error):
    """The requested change amount was negative."""


class CalculationError(Error):
    """The amount requested could not be calculated from the coins provided."""


class FloatTooLargeError(Error):
    """The total 'float' is too large."""
