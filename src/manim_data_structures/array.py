"""Contains classes to construct an array."""

import numpy as np
from manim import *

from .m_enum import MArrayDirection


class MArrayElement(VGroup):
    """A class that represents an array element.

    Parameters
    ----------
    mob_square_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Square` that represents the element body.
    mob_value_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Text` that represents the element value.
    mob_index_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Text` that represents the element index.
    index_pos : :class:`np.ndarray`, default: `UP`
        Specifies the position of :attr:`__mob_index`
    index_gap : :class:`float`, default: `0.25`
        Specifies the distance between :attr:`__mob_square` and :attr:`__mob_index`
    next_to_mob : :class:`MArrayElement`, default: `None`
        Specifies placement for :attr:`__mob_square`
    next_to_dir : :class:`np.ndarray`, default: `RIGHT`
        Specifies direction of placement for :attr:`__mob_square`

    Attributes
    ----------
    __mob_square_props : :class:`dict`
        Default arguments passed to :class:`manim.Square` that represents the element body.
    __mob_value_props : :class:`dict`
        Default arguments passed to :class:`manim.Text` that represents the element value.
    __mob_index_props : :class:`dict`
        Default arguments passed to :class:`manim.Text` that represents the element index.
    __mob_square : :class:`manim.Square`
        :class:`manim.Mobject` that represents the element body.
    __mob_value : :class:`manim.Text`
        :class:`manim.Mobject` that represents the element index.
    __mob_index : :class:`manim.Text`
        :class:`manim.Mobject` that represents the element value.
    __index_pos : :class:`np.ndarray`
        Specifies the position of :attr:`__mob_index`
    __index_gap : :class:`float`
        Specifies the distance between :attr:`__mob_square` and :attr:`__mob_index`
    """

    def __init_props(self, index_pos: np.ndarray, index_gap: float) -> None:
        """Initializes the attributes for the class.

        Parameters
        ----------
        index_pos : :class:`np.ndarray`
            Specifies the position of :attr:`__mob_index`
        index_gap : :class:`float`
            Specifies the distance between :attr:`__mob_square` and :attr:`__mob_index`
        """

        self.__mob_square_props = {
            "color": BLUE_B,
            "fill_color": BLUE_D,
            "fill_opacity": 1,
            "side_length": 1,
        }
        self.__mob_value_props = {"text": "", "color": WHITE, "weight": BOLD}
        self.__mob_index_props = {"text": "", "color": BLUE_D, "font_size": 32}
        self.__index_pos = index_pos
        self.__index_gap = index_gap

    def __update_props(
        self,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
    ) -> None:
        """Updates the attributes of the class.

        Parameters
        ----------
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index.
        """

        self.__mob_square_props.update(mob_square_args)
        self.__mob_value_props.update(mob_value_args)
        self.__mob_index_props.update(mob_index_args)

        if type(self.__mob_value_props["text"]) != str:
            self.__mob_value_props["text"] = str(self.__mob_value_props["text"])

        if type(self.__mob_index_props["text"]) != str:
            self.__mob_index_props["text"] = str(self.__mob_index_props["text"])

    def __init_mobs(
        self,
        init_square: bool = False,
        init_value: bool = False,
        init_index: bool = False,
        next_to_mob: "MArrayElement" = None,
        next_to_dir: np.ndarray = RIGHT,
    ) -> None:
        """Initializes the :class:`Mobject`s for the class.

        Parameters
        ----------
        init_square : :class:`bool`, default: `False`
            Instantiates a :class:`manim.Sqaure` and adds it to :attr:`__mob_square`.
        init_value : :class:`bool`, default: `False`
            Instantiates a :class:`manim.Text` and adds it to :attr:`__mob_value`.
        init_index : :class:`bool`, default: `False`
            Instantiates a :class:`manim.Text` and adds it to :attr:`__mob_index`.
        next_to_mob : :class:`MArrayElement`, default: `None`
            Specifies placement for :attr:`__mob_square`
        next_to_dir : :class:`np.ndarray`, default: `RIGHT`
            Specifies direction of placement for :attr:`__mob_square`
        """

        if init_square:
            self.__mob_square = Square(**self.__mob_square_props)
            if next_to_mob is not None:
                self.__mob_square.next_to(
                    next_to_mob.fetch_mob_square(), next_to_dir, 0
                )
            self.add(self.__mob_square)

        if init_value:
            self.__mob_value = Text(**self.__mob_value_props)
            self.__mob_value.next_to(self.__mob_square, np.array([0, 0, 0]), 0)
            self.add(self.__mob_value)

        if init_index:
            self.__mob_index = Text(**self.__mob_index_props)
            self.__mob_index.next_to(
                self.__mob_square, self.__index_pos, self.__index_gap
            )
            self.add(self.__mob_index)

    def __init__(
        self,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
        index_pos: np.ndarray = UP,
        index_gap: float = 0.25,
        next_to_mob: "MArrayElement" = None,
        next_to_dir: np.ndarray = RIGHT,
        **kwargs
    ) -> None:
        """Initializes the class.

        Parameters
        ----------
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index.
        index_pos : :class:`np.ndarray`, default: `UP`
            Specifies the position of :attr:`__mob_index`
        index_gap : :class:`float`, default: `0.25`
            Specifies the distance between :attr:`__mob_square` and :attr:`__mob_index`
        next_to_mob : :class:`MArrayElement`, default: `None`
            Specifies placement for :attr:`__mob_square`
        next_to_dir : :class:`np.ndarray`, default: `RIGHT`
            Specifies direction of placement for :attr:`__mob_square`
        """

        super().__init__(**kwargs)

        # Initialize props
        self.__init_props(index_pos, index_gap)

        # Update props
        self.__update_props(mob_square_args, mob_value_args, mob_index_args)

        # Initialize mobjects
        self.__init_mobs(True, True, True, next_to_mob, next_to_dir)

    def fetch_mob_square(self) -> Square:
        """Fetches the :class:`manim.Square` that represents the element body.

        Returns
        -------
        :class:`manim.Square`
            Represents the element body.
        """

        return self.__mob_square

    def fetch_mob_value(self) -> Text:
        """Fetches the :class:`manim.Text` that represents the element value.

        Returns
        -------
        :class:`manim.Text`
            Represents the element value.
        """

        return self.__mob_value

    def fetch_mob_index(self) -> Text:
        """Fetches the :class:`manim.Text` that represents the element index.

        Returns
        -------
        :class:`manim.Text`
            Represents the element index.
        """

        return self.__mob_index

    def update_mob_value(self, mob_value_args: dict = {}) -> Text:
        """Re-intializes the :class:`manim.Text` that represents the element value.

        Parameters
        ----------
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element value.
        """

        self.__update_props(mob_value_args=mob_value_args)
        self.remove(self.__mob_value)
        self.__init_mobs(init_value=True)
        self.add(self.__mob_value)
        return self.__mob_value

    def update_mob_index(self, mob_index_args: dict = {}) -> Text:
        """Re-intializes the :class:`manim.Text` that represents the element index.

        Parameters
        ----------
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element index.
        """

        self.__update_props(mob_index_args=mob_index_args)
        self.remove(self.__mob_index)
        self.__init_mobs(init_index=True)
        self.add(self.__mob_index)
        return self.__mob_index

    def animate_mob_square(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the :meth:`manim.Square.animate` property of :class:`manim.Square` for the element body.

        Returns
        -------
        :class:`_AnimationBuilder`
            Value returned by :meth:`manim.Square.animate` property of :class:`manim.Square`.
        """

        return self.__mob_square.animate

    def animate_mob_value(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the :meth:`manim.Text.animate` property of :class:`manim.Text` for the element value.

        Returns
        -------
        :class:`_AnimationBuilder`
            Value returned by :meth:`manim.Text.animate` property of :class:`manim.Text`.
        """

        return self.__mob_value.animate

    def animate_mob_index(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the :meth:`manim.Text.animate` property of :class:`manim.Text` for the element index.

        Returns
        -------
        :class:`_AnimationBuilder`
            Value returned by :meth:`manim.Text.animate` property of :class:`manim.Text`.
        """

        return self.__mob_index.animate


class MArray(VGroup):
    """A class that represents an array.

    Parameters
    ----------
    arr : :class:`list`, default: `[]`
        Array to represent. Elements must be convertible to :class:`str`.
    index_offset : :class:`int`, default: `1`
        Difference between successive indices.
    index_start : :class:`int`, default: `0`
        Starting value of index.
    index_hex_display : :class:`bool`, default: `False`
        Displays indices in hex if `True` otherwise in decimal.
    hide_index : :class:`bool`, default: `False`
        Specifies whether to display indices or not.
    arr_dir : :class:`.m_enum.MArrayDirection`, default: :attr:`.m_enum.MArrayDirection.RIGHT`
        Specifies the growing direction of array.
    mob_square_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Square` that represents the element body of :class:`MArrayElement`.
    mob_value_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Text` that represents the element value of :class:`MArrayElement`.
    mob_index_args : :class:`dict`, default: `{}`
        Arguments for :class:`manim.Text` that represents the element index of :class:`MArrayElement`.
    **kwargs
        Forwarded to constructor of the parent.

    Attributes
    ----------
    __arr : :class:`list`
        Array to represent. Elements must be convertible to :class:`str`.
    __mob_arr : List[:class:`MArrayElement`]
        Array containing the manim objects.
    __index_offset : :class:`int`
        Difference between successive indices.
    __index_start : :class:`int`
        Starting value of index.
    __index_hex_display : :class:`bool`
        Displays indices in hex if `True` otherwise in decimal.
    __hide_index : :class:`bool`, default: `False`
        Specifies whether to display indices or not.
    __arr_dir : :class:`.m_enum.MArrayDirection`, default: :attr:`.m_enum.MArrayDirection.RIGHT`
        Specifies the growing direction of array.
    """

    __dir_map = [
        {"arr": UP, "index": RIGHT},
        {"arr": DOWN, "index": RIGHT},
        {"arr": RIGHT, "index": UP},
        {"arr": LEFT, "index": UP},
    ]
    """Maps :class:`.m_enum.MArrayDirection` to correct :class:`MArrayElement` placement."""

    def __calc_index(self, index: int) -> typing.Union[int, str]:
        """Calculates and returns the index based on attributes set at initialization.

        Parameters
        ----------
        index : :class:`int`
            Index of the :attr:`__arr` for which to compute the displayable index.

        Returns
        -------
        Union[:class:`int`, :class:`str`]
            Displayable index.
        """

        return (
            ""
            if self.__hide_index
            else (
                self.__index_start + self.__index_offset * index
                if self.__index_hex_display is False
                else hex(self.__index_start + self.__index_offset * index)
            )
        )

    def __calc_index_pos(self) -> np.ndarray:
        """Calculates and returns the index position based on attributes set at initialization.

        Returns
        -------
        :class:`np.ndarray`
            Represents the index position.
        """

        return (
            self.__dir_map[self.__arr_dir.value]["index"]
            if not self.__switch_index_pos
            else self.__dir_map[self.__arr_dir.value]["index"] * -1
        )

    def __append_elem(
        self,
        value,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
    ) -> None:
        """Creates a new :class:`MArrayElement` and appends it to :attr:`__mob_arr`.

        Parameters
        ----------
        value
            Value to append.
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body of :class:`MArrayElement`.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value of :class:`MArrayElement`.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index of :class:`MArrayElement`.
        """

        mob_value_args["text"] = value
        mob_index_args["text"] = self.__calc_index(len(self.__mob_arr))
        self.__mob_arr.append(
            MArrayElement(
                mob_square_args=mob_square_args,
                mob_value_args=mob_value_args,
                mob_index_args=mob_index_args,
                index_pos=self.__calc_index_pos(),
                next_to_mob=self.__mob_arr[-1] if len(self.__mob_arr) else None,
                next_to_dir=self.__dir_map[self.__arr_dir.value]["arr"],
            )
        )
        self.add(self.__mob_arr[-1])

    def __init__(
        self,
        arr: list = [],
        index_offset: int = 1,
        index_start: int = 0,
        index_hex_display: bool = False,
        hide_index: bool = False,
        arr_dir: MArrayDirection = MArrayDirection.RIGHT,
        switch_index_pos: bool = False,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
        **kwargs
    ) -> None:
        """Initializes the class.

        Parameters
        ----------
        arr : :class:`list`, default: `[]`
            Array to represent. Elements must be convertible to :class:`str`.
        index_offset : :class:`int`, default: `1`
            Difference between successive indices.
        index_start : :class:`int`, default: `0`
            Starting value of index.
        index_hex_display : :class:`bool`, default: `False`
            Displays indices in hex if `True` otherwise in decimal.
        hide_index : :class:`bool`, default: `False`
            Specifies whether to display indices or not.
        arr_dir : :class:`.m_enum.MArrayDirection`, default: :attr:`.m_enum.MArrayDirection.RIGHT`
            Specifies the growing direction of array.
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body of :class:`MArrayElement`.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value of :class:`MArrayElement`.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index of :class:`MArrayElement`.
        **kwargs
            Forwarded to constructor of the parent.
        """

        super().__init__(**kwargs)
        self.__arr = arr
        self.__mob_arr = []
        self.__index_offset = index_offset
        self.__index_start = index_start
        self.__index_hex_display = index_hex_display
        self.__hide_index = hide_index
        self.__arr_dir = arr_dir
        self.__switch_index_pos = switch_index_pos

        for v in arr:
            self.__append_elem(v, mob_square_args, mob_value_args, mob_index_args)

    def update_elem_value(self, index: int, value, mob_value_args: dict = {}) -> Text:
        """Updates the elements value.

        Parameters
        ----------
        index : :class:`int`
            Index of :attr:`__mob_arr` to update.
        value
            New value to be assigned.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value of :class:`MArrayElement`.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element value.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        self.__arr[index] = value
        mob_value_args["text"] = value
        return self.__mob_arr[index].update_mob_value(mob_value_args)

    def update_elem_index(self, index: int, value, mob_index_args: dict = {}) -> Text:
        """Updates the elements index.

        Parameters
        ----------
        index : :class:`int`
            Index of :attr:`__mob_arr` to update.
        value
            New value to be assigned.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index of :class:`MArrayElement`.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element index.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        mob_index_args["text"] = value
        return self.__mob_arr[index].update_mob_index(mob_index_args)

    def animate_elem(self, index: int) -> "_AnimationBuilder":  # type: ignore
        """Invokes the :meth:`MArrayElement.animate` property of :class:`MArrayElement` on specified index of :attr:`__mob_arr`.

        Parameters
        ----------
        index : :class:`int`
            Index of :attr:`__mob_arr` to animate.

        Returns
        -------
        :class:`_AnimationBuilder`
            Value returned by :meth:`MArrayElement.animate` property of :class:`MArrayElement`.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        return self.__mob_arr[index].animate

    def animate_elem_square(self, index: int) -> "_AnimationBuilder":  # type: ignore
        """Invokes the :meth:`manim.Square.animate` property of :class:`manim.Square` on specified index of :attr:`__mob_arr`.

        Parameters
        ----------
        index : :class:`int`
            Index of :attr:`__mob_arr` to animate.

        Returns
        -------
        :class:`_AnimationBuilder`
            Value returned by :meth:`manim.Square.animate` property of :class:`manim.Square`.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        return self.__mob_arr[index].animate_mob_square()

    def animate_elem_value(self, index: int) -> "_AnimationBuilder":  # type: ignore
        """Invokes the :meth:`manim.Text.animate` property of :class:`manim.Text` on specified index of :attr:`__mob_arr`.

        Parameters
        ----------
        index : :class:`int`
            Index of :attr:`__mob_arr` to animate.

        Returns
        -------
        :class:`_AnimationBuilder`
            Value returned by :meth:`manim.Text.animate` property of :class:`manim.Text`.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        return self.__mob_arr[index].animate_mob_value()

    def animate_elem_index(self, index: int) -> "_AnimationBuilder":  # type: ignore
        """Invokes the :meth:`manim.Text.animate` property of :class:`manim.Text` on specified index of :attr:`__mob_arr`.

        Parameters
        ----------
        index : :class:`int`
            Index of :attr:`__mob_arr` to animate.

        Returns
        -------
        :class:`_AnimationBuilder`
            Value returned by :meth:`manim.Text.animate` property of :class:`manim.Text`.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        return self.__mob_arr[index].animate_mob_index()

    def append_elem(
        self,
        value,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
    ) -> MArrayElement:
        """Appends the `value` to :attr:`__arr` and creates a new :class:`MArrayElement` and appends it to :attr:`__mob_arr`.

        Parameters
        ----------
        value
            Value to append.
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body of :class:`MArrayElement`.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value of :class:`MArrayElement`.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index of :class:`MArrayElement`.

        Returns
        -------
        :class:`MArrayElement`
            Represents the appended element.
        """
        self.__arr.append(value)
        self.__append_elem(value, mob_square_args, mob_value_args, mob_index_args)
        return self.__mob_arr[-1]

    def fetch_arr(self) -> list:
        """Fetches :attr:`__arr`.

        Returns
        -------
        :class:`list`
            Represents the array stored in :attr:`__arr`.
        """

        return self.__arr

    def fetch_mob_arr(self) -> typing.List[MArrayElement]:
        """Fetches :attr:`__mob_arr`.

        Returns
        -------
        List[:class:`MArrayElement`]
            Represents the array stored in :attr:`__mob_arr`.
        """

        return self.__mob_arr
