"""Contains classes to construct an array."""

import numpy as np
from manim import *

from .m_enum import MArrayDirection, MArrayElementComp


class MArrayElement(VGroup):
    """A class that represents an array element.

    Parameters
    ----------
    scene : :class:`manim.Scene`
        The scene where the object should exist.
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
    label_pos : :class:`np.ndarray`, default: `LEFT`
        Specifies the position of :attr:`__mob_label`
    label_gap : :class:`float`, default: `0.5`
        Specifies the distance between :attr:`__mob_square` and :attr:`__mob_label`
    next_to_mob : :class:`MArrayElement`, default: `None`
        Specifies placement for :attr:`__mob_square`
    next_to_dir : :class:`np.ndarray`, default: `RIGHT`
        Specifies direction of placement for :attr:`__mob_square`

    Attributes
    ----------
    __scene : :class:`manim.Scene`
        The scene where the object should exist.
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
    __label_pos : :class:`np.ndarray`, default: `LEFT`
        Specifies the position of :attr:`__mob_label`
    __label_gap : :class:`float`, default: `0.5`
        Specifies the distance between :attr:`__mob_square` and :attr:`__mob_label`
    """

    def __init_props(
        self,
        scene: Scene,
        index_pos: np.ndarray,
        index_gap: float,
        label_pos: np.ndarray,
        label_gap: float,
    ) -> None:
        """Initializes the attributes for the class.

        Parameters
        ----------
        index_pos : :class:`np.ndarray`
            Specifies the position of :attr:`__mob_index`
        index_gap : :class:`float`
            Specifies the distance between :attr:`__mob_square` and :attr:`__mob_index`
        label_pos : :class:`np.ndarray`
            Specifies the position of :attr:`__mob_label`
        label_gap : :class:`float`
            Specifies the distance between :attr:`__mob_square` and :attr:`__mob_label`
        """

        self.__mob_square_props = {
            "color": BLUE_B,
            "fill_color": BLUE_D,
            "fill_opacity": 1,
            "side_length": 1,
        }
        self.__mob_value_props = {"text": "", "color": WHITE, "weight": BOLD}
        self.__mob_index_props = {"text": "", "color": BLUE_D, "font_size": 32}
        self.__mob_label_props = {"text": "", "color": BLUE_A, "font_size": 38}
        self.__scene = scene
        self.__index_pos = index_pos
        self.__index_gap = index_gap
        self.__label_pos = label_pos
        self.__label_gap = label_gap

    def __update_props(
        self,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
        mob_label_args: dict = {},
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
        mob_label_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element label.
        """

        self.__mob_square_props.update(mob_square_args)
        self.__mob_value_props.update(mob_value_args)
        self.__mob_index_props.update(mob_index_args)
        self.__mob_label_props.update(mob_label_args)

        if type(self.__mob_value_props["text"]) != str:
            self.__mob_value_props["text"] = str(self.__mob_value_props["text"])

        if type(self.__mob_index_props["text"]) != str:
            self.__mob_index_props["text"] = str(self.__mob_index_props["text"])

        if type(self.__mob_label_props["text"]) != str:
            self.__mob_label_props["text"] = str(self.__mob_label_props["text"])

    def __init_mobs(
        self,
        init_square: bool = False,
        init_value: bool = False,
        init_index: bool = False,
        init_label: bool = False,
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
        init_label : :class:`bool`, default: `False`
            Instantiates a :class:`manim.Text` and adds it to :attr:`__mob_label`.
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

        if init_label:
            self.__mob_label = Text(**self.__mob_label_props)
            self.__mob_label.next_to(
                self.__mob_square, self.__label_pos, self.__label_gap
            )
            self.add(self.__mob_label)

    def __init__(
        self,
        scene: Scene,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
        mob_label_args: dict = {},
        index_pos: np.ndarray = UP,
        index_gap: float = 0.25,
        label_pos: np.ndarray = LEFT,
        label_gap: float = 0.5,
        next_to_mob: "MArrayElement" = None,
        next_to_dir: np.ndarray = RIGHT,
        **kwargs
    ) -> None:
        """Initializes the class.

        Parameters
        ----------
        scene : :class:`manim.Scene`
            The scene where the object should exist.
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index.
        mob_label_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element label.
        index_pos : :class:`np.ndarray`, default: `UP`
            Specifies the position of :attr:`__mob_index`.
        index_gap : :class:`float`, default: `0.25`
            Specifies the distance between :attr:`__mob_square` and :attr:`__mob_index`.
        label_pos : :class:`np.ndarray`, default: `LEFT`
            Specifies the position of :attr:`__mob_label`.
        label_gap : :class:`float`, default: `0.5`
            Specifies the distance between :attr:`__mob_square` and :attr:`__mob_label`
        next_to_mob : :class:`MArrayElement`, default: `None`
            Specifies placement for :attr:`__mob_square`.
        next_to_dir : :class:`np.ndarray`, default: `RIGHT`
            Specifies direction of placement for :attr:`__mob_square`.
        """

        super().__init__(**kwargs)

        # Initialize props
        self.__init_props(scene, index_pos, index_gap, label_pos, label_gap)

        # Update props
        self.__update_props(
            mob_square_args, mob_value_args, mob_index_args, mob_label_args
        )

        # Initialize mobjects
        self.__init_mobs(True, True, True, True, next_to_mob, next_to_dir)

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

    def fetch_mob_label(self) -> Text:
        """Fetches the :class:`manim.Text` that represents the element label.

        Returns
        -------
        :class:`manim.Text`
            Represents the element label.
        """

        return self.__mob_label

    def fetch_mob(self, mob_target: MArrayElementComp) -> Mobject:
        """Fetches :class:`manim.Mobject` based on enum :class:`m_enum.MArrayElementComp`.

        Parameters
        ----------
        mob_target : :class:`m_enum.MArrayElementComp`
            Specifies the component of :class:`MArrayElement` to fetch.

        Returns
        -------
        :class:`manim.Mobject`
            Represents the component of :class:`MArrayElement`.
        """

        if mob_target == MArrayElementComp.BODY:
            return self.fetch_mob_square()
        elif mob_target == MArrayElementComp.VALUE:
            return self.fetch_mob_value()
        elif mob_target == MArrayElementComp.INDEX:
            return self.fetch_mob_index()
        elif mob_target == MArrayElementComp.LABEL:
            return self.fetch_mob_label()
        else:
            return self

    def update_mob_value(
        self,
        mob_value_args: dict = {},
        update_anim: Animation = Indicate,
        update_anim_args: dict = {},
        play_anim: bool = True,
    ) -> Text:
        """Re-intializes the :class:`manim.Text` that represents the element value.

        Parameters
        ----------
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value.
        update_anim : :class:`manim.Animation`, default `{manim.Indicate}`
            Animation to be applied to the updated :class:`manim.Text`.
        update_anim_args : :class:`dict`, default: `{}`
            Arguments for update :class:`manim.Animation`.
        play_anim : :class:`bool`, default: `True`
            Specifies whether to play the update :class:`manim.Animation`.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element value.
        """

        # Update props of mob_value
        self.__update_props(mob_value_args=mob_value_args)

        # Remove current mob_value
        self.remove(self.__mob_value)

        # Initialize new mob_value
        self.__init_mobs(init_value=True)

        # Add new mob_value to group
        self.add(self.__mob_value)

        # Animate change
        if play_anim:
            self.__scene.play(update_anim(self.__mob_value, **update_anim_args))

        return self.__mob_value

    def update_mob_index(
        self,
        mob_index_args: dict = {},
        update_anim: Animation = Indicate,
        update_anim_args: dict = {},
        play_anim: bool = True,
    ) -> Text:
        """Re-intializes the :class:`manim.Text` that represents the element index.

        Parameters
        ----------
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index.
        update_anim : :class:`manim.Animation`, default `{manim.Indicate}`
            Animation to be applied to the updated :class:`manim.Text`.
        update_anim_args : :class:`dict`, default: `{}`
            Arguments for update :class:`manim.Animation`.
        play_anim : :class:`bool`, default: `True`
            Specifies whether to play the update :class:`manim.Animation`.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element index.
        """

        # Update props of mob_index
        self.__update_props(mob_index_args=mob_index_args)

        # Remove current mob_index
        self.remove(self.__mob_index)

        # Initialize new mob_index
        self.__init_mobs(init_value=True)

        # Add new mob_index to group
        self.add(self.__mob_index)

        # Animate change
        if play_anim:
            self.__scene.play(update_anim(self.__mob_index, **update_anim_args))

        return self.__mob_index

    def update_mob_label(
        self,
        mob_label_args: dict = {},
        update_anim: Animation = Indicate,
        update_anim_args: dict = {},
        play_anim: bool = True,
    ) -> Text:
        """Re-intializes the :class:`manim.Text` that represents the element label.

        Parameters
        ----------
        mob_label_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element label.
        update_anim : :class:`manim.Animation`, default `{manim.Indicate}`
            Animation to be applied to the updated :class:`manim.Text`.
        update_anim_args : :class:`dict`, default: `{}`
            Arguments for update :class:`manim.Animation`.
        play_anim : :class:`bool`, default: `True`
            Specifies whether to play the update :class:`manim.Animation`.

        Returns
        -------
        :class:`manim.Text`
            Represents the updated element label.
        """

        # Update props of mob_label
        self.__update_props(mob_label_args=mob_label_args)

        # Remove current mob_label
        self.remove(self.__mob_label)

        # Initialize new mob_label
        self.__init_mobs(init_value=True)

        # Add new mob_label to group
        self.add(self.__mob_label)

        # Animate change
        if play_anim:
            self.__scene.play(update_anim(self.__mob_label, **update_anim_args))

        return self.__mob_label

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

    def animate_mob_label(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the :meth:`manim.Text.animate` property of :class:`manim.Text` for the element label.

        Returns
        -------
        :class:`_AnimationBuilder`
            Value returned by :meth:`manim.Text.animate` property of :class:`manim.Text`.
        """

        return self.__mob_label.animate


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
    __mob_arr_label_props
    """

    __dir_map = [
        {"arr": UP, "index": RIGHT},
        {"arr": DOWN, "index": RIGHT},
        {"arr": RIGHT, "index": UP},
        {"arr": LEFT, "index": UP},
    ]
    """Maps :class:`.m_enum.MArrayDirection` to correct :class:`MArrayElement` placement."""

    def __init_props(self) -> None:
        """Initializes the attributes for the class."""

        self.__mob_arr_label_props = {"text": "", "color": BLUE_A, "font_size": 38}

    def __update_props(
        self,
        label: str = "",
        mob_arr_label_args: dict = {},
    ) -> None:
        """Updates the attributes of the class.

        Parameters
        ----------
        label : :class:`str`, default `''`
            Specifies the textual value for :attr:`__mob_arr_label`
        mob_arr_label_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the array label.
        """

        self.__mob_arr_label_props["text"] = label
        self.__mob_arr_label_props.update(mob_arr_label_args)

        if type(self.__mob_arr_label_props["text"]) != str:
            self.__mob_arr_label_props["text"] = str(self.__mob_arr_label_props["text"])

    def __sum_elem_len(self, index_start: int, index_end: int) -> int:
        """Sums the length of :class:`manim.Square` elements between the specified bound.

        Parameters
        ----------
        index_start : :class:`int`
            Starting index of the bound (inclusive).
        index_end : :class:`int`
            Ending index of the bound (inclusive).

        Returns
        -------
        :class:`int`
            Total length of the elements.
        """

        if (
            index_start < 0
            or index_end < 0
            or index_start > len(self.__mob_arr)
            or index_end > len(self.__mob_arr)
        ):
            raise Exception("Index out of bounds!")

        total_len = 0
        for i in range(index_start, index_end + 1):
            total_len += self.__mob_arr[i].fetch_mob_square().side_length
        return total_len

    def __calc_label_pos_and_mob(self) -> typing.Tuple[Square, np.ndarray]:
        """Calculates the position of the label relative to :class:`MArrayElement` 's :class:`manim.Square` and returns them.

        Returns
        -------
        :class:`Manim.Square`
            Represents the :class:`manim.Mobject` next to which the label is positioned.
        :class:`np.ndarray`
            Represents the relative label's position.
        """

        # Label position is parallel to array growth direction
        if np.array_equal(
            self.__dir_map[self.__arr_label_pos.value]["arr"],
            self.__dir_map[self.__arr_dir.value]["arr"],
        ):
            return (
                self.__mob_arr[-1].fetch_mob_square(),
                self.__dir_map[self.__arr_label_pos.value]["arr"],
            )
        elif np.array_equal(
            self.__dir_map[self.__arr_label_pos.value]["arr"],
            -self.__dir_map[self.__arr_dir.value]["arr"],
        ):
            return (
                self.__mob_arr[0].fetch_mob_square(),
                self.__dir_map[self.__arr_label_pos.value]["arr"],
            )

        # Label position is perpendicular to array growth direction
        else:
            middle_index = len_before = len_after = 0
            if len(self.__mob_arr) > 1:
                middle_index = int(len(self.__mob_arr) / 2)
                len_before = self.__sum_elem_len(0, middle_index - 1)
                len_after = self.__sum_elem_len(
                    middle_index + 1, len(self.__mob_arr) - 1
                )
            return (
                self.__mob_arr[middle_index].fetch_mob_square(),
                self.__dir_map[self.__arr_label_pos.value]["arr"]
                + self.__dir_map[self.__arr_dir.value]["arr"]
                * ((len_after - len_before) / 2),
            )

    def __init_mobs(
        self,
        init_arr_label: bool = False,
    ) -> None:
        """Initializes the :class:`Mobject`s for the class.

        Parameters
        ----------
        init_arr_label : :class:`bool`, default: `False`
            Instantiates a :class:`manim.Text` and adds it to :attr:`__mob_arr_label`.
        """

        if init_arr_label:
            self.__mob_arr_label = Text(**self.__mob_arr_label_props)
            if len(self.__mob_arr):
                (next_to_mob, label_pos) = self.__calc_label_pos_and_mob()
                self.__mob_arr_label.next_to(
                    next_to_mob, label_pos, self.__arr_label_gap
                )
            self.add(self.__mob_arr_label)

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

    def __calc_label_shift_factor(self, mob: MArrayElement) -> float:
        """Calculates how much to shift the :attr:`__mob_arr_label` after insertion/removal of an :class:`MArrayElement`.

        Parameters
        ----------
        mob : :class:`MArrayElement`
            The element that has been inserted or removed.

        Returns
        -------
        :class:`int`
            Factor by which to shift the :attr:`__mob_arr_label`.
        """

        if np.array_equal(
            self.__dir_map[self.__arr_label_pos.value]["arr"],
            self.__dir_map[self.__arr_dir.value]["arr"],
        ):
            return mob.fetch_mob_square().side_length
        elif not np.array_equal(
            self.__dir_map[self.__arr_label_pos.value]["arr"],
            -self.__dir_map[self.__arr_dir.value]["arr"],
        ):
            return mob.fetch_mob_square().side_length / 2
        return 0

    def __append_elem(
        self,
        value,
        shift_label: bool = True,
        append_anim: Animation = Write,
        append_anim_args: dict = {},
        append_anim_target: MArrayElementComp = None,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
    ) -> typing.List[Animation]:
        """Creates a new :class:`MArrayElement` and appends it to :attr:`__mob_arr`.

        Parameters
        ----------
        value
            Value to append.
        shift_label: :class:`bool`, default: `True`
            Specifies whether to shift the :class:`__mob_arr_label` or not.
        append_anim : :class:`manim.Animation`, default: :class:`manim.Write`
            Specifies the :class:`manim.Animation` to be played on the :class:`MArrayElement` being appended.
        append_anim_args : :class:`dict`, default: `{}`
            Arguments for append :class:`manim.Animation`.
        append_anim_target : :class:`.m_enum.MArrayElementComp`, default: `None`
            Specifies the :class:`manim.Mobject` of the :class:`MArrayElement` on which the append :class:`manim.Animation` is to be played.
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body of :class:`MArrayElement`.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value of :class:`MArrayElement`.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index of :class:`MArrayElement`.

        Returns
        -------
        List[:class:`manim.Animation`]
            List of animations for appending.
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

        anim_list = [
            append_anim(
                self.__mob_arr[-1].fetch_mob(append_anim_target), **append_anim_args
            )
        ]

        if shift_label:
            label_shift_factor = self.__calc_label_shift_factor(self.__mob_arr[-1])
            anim_list.append(
                ApplyMethod(
                    self.__mob_arr_label.shift,
                    self.__dir_map[self.__arr_dir.value]["arr"] * label_shift_factor,
                )
            )

        return anim_list

    def __remove_elem(
        self,
        index: int,
        removal_anim: Animation = FadeOut,
        update_anim: Animation = Write,
        removal_anim_args: dict = {},
        update_anim_args: dict = {},
        removal_anim_target: MArrayElementComp = None,
        update_anim_target: MArrayElementComp = MArrayElementComp.INDEX,
    ) -> typing.Tuple[Succession, typing.Callable[[], typing.List[Animation]]]:
        """Removes the :class:`MArrayElement` from :attr:`__mob_arr` at the specified index.

        Parameters
        ----------
        index : :class:`int`
            Index of :class:`MArrayElement` to remove.
        removal_anim : :class:`manim.Animation`, default: :class:`manim.FadeOut`
            Specifies the :class:`manim.Animation` to be played on the :class:`MArrayElement` being removed.
        update_anim : :class:`manim.Animation`, default: :class:`manim.Write`
            Specifies the :class:`manim.Animation` to be played on the :class:`MArrayElement`(s) after the removed element.
        removal_anim_args : :class:`dict`, default: `{}`
            Arguments for removal :class:`manim.Animation`.
        update_anim_args : :class:`dict`, default: `{}`
            Arguments for update :class:`manim.Animation`.
        removal_anim_target : :class:`.m_enum.MArrayElementComp`, default: `None`
            Specifies the :class:`manim.Mobject` of the :class:`MArrayElement` on which the removal :class:`manim.Animation` is to be played.
        update_anim_target : :class:`.m_enum.MArrayElementComp`, default: :attr:`.m_enum.MArrayElementComp.INDEX`
            Specifies the :class:`manim.Mobject` of the :class:`MArrayElement` on which the update :class:`manim.Animation` is to be played.

        Returns
        -------
        :class:`manim.Succession`
            Contains :class:`manim.Animations` played for removal and shifting of :class:`MArrayElement`.
        Callable[[], List[:class:`manim.Animation`]]
            Method that updates the indices of :class:`MArrayElement`(s) that occur after the removal and returns a list of update :class:`manim.Animation`(s).
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        self.remove(self.__mob_arr[index])
        removed_mob = self.__mob_arr[index]
        self.__mob_arr = self.__mob_arr[0:index] + self.__mob_arr[index + 1 :]

        anims_shift = []
        for i in range(index, len(self.__mob_arr)):
            anims_shift.append(
                ApplyMethod(
                    self.__mob_arr[i].shift,
                    -(
                        self.__dir_map[self.__arr_dir.value]["arr"]
                        * removed_mob.fetch_mob_square().side_length
                    ),
                )
            )

        label_shift_factor = self.__calc_label_shift_factor(removed_mob)

        if label_shift_factor != 0:
            anims_shift.append(
                ApplyMethod(
                    self.__mob_arr_label.shift,
                    -self.__dir_map[self.__arr_dir.value]["arr"] * label_shift_factor,
                )
            )

        def update_indices() -> typing.List[Animation]:
            """Updates the indices of :class:`MArrayElement`(s) that occur after the removal.

            Returns
            -------
            List[:class:`manim.Animation`]
                Represents :class:`Animation` for indices update.
            """

            anims_index = []
            for i in range(index, len(self.__mob_arr)):
                self.__mob_arr[i].update_mob_index(
                    mob_index_args={"text": self.__calc_index(i)}
                )
                anims_index.append(
                    update_anim(
                        (self.__mob_arr[i].fetch_mob(update_anim_target)),
                        **update_anim_args
                    )
                )

            return anims_index

        return (
            Succession(
                removal_anim(
                    removed_mob.fetch_mob(removal_anim_target), **removal_anim_args
                ),
                AnimationGroup(*anims_shift),
            ),
            update_indices,
        )

    def __init__(
        self,
        arr: list = [],
        label="",
        index_offset: int = 1,
        index_start: int = 0,
        index_hex_display: bool = False,
        hide_index: bool = False,
        arr_dir: MArrayDirection = MArrayDirection.RIGHT,
        switch_index_pos: bool = False,
        arr_label_pos: MArrayDirection = MArrayDirection.LEFT,
        arr_label_gap: float = 0.5,
        mob_arr_label_args: dict = {},
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
        arr_label_pos : :class:`.enum.MArrayDirection`, default: :attr:`.m_enum.MArrayDirection.LEFT`
            Specifies the position of :attr:`__mob_arr_label`.
        arr_label_gap : :class:`float`, default: `0.5`
            Specifies the distance between :attr:`__mob_arr` and :attr:`__mob_arr_label`.
        mob_arr_label_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the label for :class:`MArray`.
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
        self.__arr_label_pos = arr_label_pos
        self.__arr_label_gap = arr_label_gap

        self.__init_props()
        self.__update_props(label=label, mob_arr_label_args=mob_arr_label_args)

        for v in arr:
            self.__append_elem(
                v,
                False,
                mob_square_args=mob_square_args,
                mob_value_args=mob_value_args,
                mob_index_args=mob_index_args,
            )

        self.__init_mobs(True)

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
        append_anim: Animation = Write,
        append_anim_args: dict = {},
        append_anim_target: MArrayElementComp = None,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
    ) -> typing.List[Animation]:
        """Appends the `value` to :attr:`__arr` and creates a new :class:`MArrayElement` and appends it to :attr:`__mob_arr`.

        Parameters
        ----------
        value
            Value to append.
        append_anim : :class:`manim.Animation`, default: :class:`manim.Write`
            Specifies the :class:`manim.Animation` to be played on the :class:`MArrayElement` being appended.
        append_anim_args : :class:`dict`, default: `{}`
            Arguments for append :class:`manim.Animation`.
        append_anim_target : :class:`.m_enum.MArrayElementComp`, default: `None`
            Specifies the :class:`manim.Mobject` of the :class:`MArrayElement` on which the append :class:`manim.Animation` is to be played.
        mob_square_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Square` that represents the element body of :class:`MArrayElement`.
        mob_value_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element value of :class:`MArrayElement`.
        mob_index_args : :class:`dict`, default: `{}`
            Arguments for :class:`manim.Text` that represents the element index of :class:`MArrayElement`.
        shift_label: :class:`bool`, default: `True`
            Specifies whether to shift the :class:`__mob_arr_label` or not.

        Returns
        -------
        List[:class:`manim.Animation`]
            List of animations for appending.
        """

        self.__arr.append(value)
        return self.__append_elem(
            value,
            mob_square_args=mob_square_args,
            mob_value_args=mob_value_args,
            mob_index_args=mob_index_args,
            append_anim=append_anim,
            append_anim_args=append_anim_args,
            append_anim_target=append_anim_target,
        )

    def remove_elem(
        self,
        index,
        removal_anim: Animation = FadeOut,
        update_anim: Animation = Write,
        removal_anim_args: dict = {},
        update_anim_args: dict = {},
        removal_anim_target: MArrayElementComp = None,
        update_anim_target: MArrayElementComp = MArrayElementComp.INDEX,
    ) -> typing.Tuple[Succession, typing.Callable[[], typing.List[Animation]]]:
        """Removes the element from :attr:`__arr` and removes :class:`MArrayElement` from :attr:`__mob_arr` at the specified index.

        Parameters
        ----------
        index : :class:`int`
            Index of :class:`MArrayElement` to remove.
        removal_anim : :class:`manim.Animation`, default: :class:`manim.FadeOut`
            Specifies the :class:`manim.Animation` to be played on the :class:`MArrayElement` being removed.
        update_anim : :class:`manim.Animation`, default: :class:`manim.Write`
            Specifies the :class:`manim.Animation` to be played on the :class:`MArrayElement`(s) after the removed element.
        removal_anim_args : :class:`dict`, default: `{}`
            Arguments for removal :class:`manim.Animation`.
        update_anim_args : :class:`dict`, default: `{}`
            Arguments for update :class:`manim.Animation`.
        removal_anim_target : :class:`.m_enum.MArrayElementComp`, default: `None`
            Specifies the :class:`manim.Mobject` of the :class:`MArrayElement` on which the removal :class:`manim.Animation` is to be played.
        update_anim_target : :class:`.m_enum.MArrayElementComp`, default: :attr:`.m_enum.MArrayElementComp.INDEX`
            Specifies the :class:`manim.Mobject` of the :class:`MArrayElement` on which the update :class:`manim.Animation` is to be played.

        Returns
        -------
        :class:`manim.Succession`
            Contains :class:`manim.Animations` played for removal and shifting of :class:`MArrayElement`.
        Callable[[], List[:class:`manim.Animation`]]
            Method that updates the indices of :class:`MArrayElement`(s) that occur after the removal and returns a list of update :class:`manim.Animation`(s).
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        self.__arr = self.__arr[0:index] + self.__arr[index + 1 :]

        return self.__remove_elem(
            index,
            removal_anim,
            update_anim,
            removal_anim_args,
            update_anim_args,
            removal_anim_target,
            update_anim_target,
        )

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

    def fetch_arr_label(self) -> Text:
        """Fetches the :class:`manim.Text` that represents the array label.

        Returns
        -------
        :class:`manim.Text`
            Represents the array label.
        """

        return self.__mob_arr_label
