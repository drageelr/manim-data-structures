"""Contains enums used throughout the package."""

from enum import Enum


class MArrayElementComp(Enum):
    """Refers to individual component :class:`~manim.mobject.mobject.Mobject`\0s of :class:`~.m_array.MArrayElement`."""

    BODY = 0
    """:class:`~manim.mobject.geometry.polygram.Square` that represents the body."""

    VALUE = 1
    """:class:`~manim.mobject.text.text_mobject.Text` that represents the value."""

    INDEX = 2
    """:class:`~manim.mobject.text.text_mobject.Text` that represents the index."""

    LABEL = 3
    """:class:`~manim.mobject.text.text_mobject.Text` that represents the label."""


class MArrayDirection(Enum):
    """Serves as the direction for :class:`~.m_array.MArray`."""

    UP = 0
    """Upward direction."""

    DOWN = 1
    """Downward direction."""

    RIGHT = 2
    """Rightward direction."""

    LEFT = 3
    """Leftward direction."""
