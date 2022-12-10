"""Contains classes to construct variable."""

from manim import *

from .m_array import MArrayElement


class MVariable(MArrayElement):
    """A class that represents a variable.

    Parameters
    ----------
    value
        Specifies the value of the variable.
    index
        Specifies the index of the variable.
    label
        Specifies the label of the variable.
    mob_square_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Square` that represents the element body.
    mob_value_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Text` that represents the element value.
    mob_index_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Text` that represents the element index.

    Attributes
    ----------
    __value
        Specifies the value of the variable.
    __index
        Specifies the index of the variable.
    __label
        Specifies the label of the variable.
    """

    def __init__(
        self,
        value="",
        index="",
        label="",
        mob_value_args: dict = {},
        mob_index_args: dict = {},
        mob_label_args: dict = {},
        **kwargs
    ) -> None:
        """Initializes the class.

        Parameters
        ----------
        value
            Specifies the value of the variable.
        index
            Specifies the index of the variable.
        label
            Specifies the label of the variable.
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index.

        Attributes
        ----------
        __value
            Specifies the value of the variable.
        __index
            Specifies the index of the variable.
        __label
            Specifies the label of the variable.
        """

        self.__value = value
        self.__index = index
        self.__label = label

        mob_value_args["text"] = value
        mob_index_args["text"] = index
        mob_label_args["text"] = label

        super().__init__(
            mob_value_args=mob_value_args,
            mob_index_args=mob_index_args,
            mob_label_args=mob_label_args,
            **kwargs
        )

    def fetch_value(self):
        """Fetches :attr:`__value`.

        Returns
        -------
        Any
            Value of :class:`MVariable`.
        """

        return self.__value

    def fetch_index(self):
        """Fetches :attr:`__index`.

        Returns
        -------
        Any
            Index of :class:`MVariable`.
        """

        return self.__index

    def fetch_label(self):
        """Fetches :attr:`__label`.

        Returns
        -------
        Any
            Label of :class:`MVariable`.
        """

        return self.__label

    def update_value(self, value, mob_value_args: dict = {}) -> Text:
        """Updates :attr:`__value` and the :class:`manim.Text` that represents the element value.

        Parameters
        ----------
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element value.
        """

        self.__value = value
        mob_value_args["text"] = value
        return self.update_mob_value(mob_value_args)

    def update_index(self, index, mob_index_args: dict = {}) -> Text:
        """Updates :attr:`__index` and the :class:`manim.Text` that represents the element index.

        Parameters
        ----------
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element index.
        """

        self.__index = index
        mob_index_args["text"] = index
        return self.update_mob_index(mob_index_args)

    def update_label(self, label, mob_label_args: dict = {}) -> Text:
        """Updates :attr:`__label` and the :class:`manim.Text` that represents the element label.

        Parameters
        ----------
        mob_label_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element label.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element label.
        """

        self.__value = label
        mob_label_args["text"] = label
        return self.update_mob_label(mob_label_args)
