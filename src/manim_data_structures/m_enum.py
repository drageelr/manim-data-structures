"""Contains enums used throughout the package."""

from enum import Enum


class MArrayElementComp(Enum):
    """Refers to the individual component :class:`manim.Mobject` of :class:`MArrayElement`."""

    BODY = 0
    """Body :class:`manim.Square`"""

    VALUE = 1
    """Value :class:`manim.Text`"""

    INDEX = 2
    """Index :class:`manim.Text`"""

    LABEL = 3
    """Label :class:`manim.Text`"""


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
