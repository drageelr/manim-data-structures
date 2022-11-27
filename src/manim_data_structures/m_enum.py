"""Contains enums used throughout the package."""

from enum import Enum


class MArrayDirection(Enum):
    """Specifies the growth direction of the :class:`MArray`."""

    UP = 0
    """Upward direction."""

    DOWN = 1
    """Downward direction."""

    RIGHT = 2
    """Rightward direction."""

    LEFT = 3
    """Leftward direction."""
