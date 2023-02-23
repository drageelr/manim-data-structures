from __future__ import annotations
from copy import deepcopy

import numpy as np
from manim import *

from .m_enum import MArrayDirection

class MArraySlidingWindow(VGroup):
    """A class that represents a sliding window

    Parameters
    ----------
    scene
        Specifies the scene where the object is to be rendered.
    arr
        Specifies the array to which the sliding window is to be attached.
    index
        Specifies the index of the element to which the sliding window is to be attached.
    size
        Specifies the number of elements the sliding window should enclose.
    label
        Specifies the value of the sliding window label.
    label_gap
        Specifies the distance between :attr:`__mob_label` and :attr:`__mob_window`.
    label_pos
        Specifies the position of the pointer w.r.t to :attr:`__mob_window`.
    mob_window_args
        Arguments for :class:`~manim.mobject.geometry.polygram.Rectangle` that represents the window.
    mob_label_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the window label.
    **kwargs
        Forwarded to constructor of the parent.

    Attributes
    ----------
    __scene : :class:`~manim.scene.scene.Scene`
        The scene where the object is to be rendered.
    __arr : :class:`~typing.List`\0[:class:`MArrayElement`]
        The array to which the sliding window is to be attached.
    __index : :class:`int`
        The index of the element to which the sliding window is to be attached.
    __size : :class:`int`
        The number of elements the sliding window should enclose.
    __label : :class:`str`
        The value of the sliding window label.
    __label_gap : :class:`float`
        The distance between :attr:`__mob_label` and :attr:`__mob_window`.
    __label_pos : :class:`.m_enum.MArrayDirection`
        The position of the pointer w.r.t to :attr:`__mob_window`.
    __mob_window_props : :class:`dict`
        Arguments for :class:`~manim.mobject.geometry.polygram.Rectangle` that represents the window.
    __mob_label_props : :class:`dict`
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the window label.
    __mob_window : :class:`~manim.mobject.geometry.polygram.Rectangle`
        Represents the window of the sliding window.
    __mob_label : :class:`~manim.mobject.text.text_mobject.Text`
        Represents the label of the sliding window.
    __updater_pos : :data:`typing.Callable`\0[[], None]
        The updater function that keeps the sliding window intact with the array.
    """

    __dir_map = [
        {"np": UP, "dir": MArrayDirection.UP},
        {"np": DOWN, "dir": MArrayDirection.DOWN},
        {"np": RIGHT, "dir": MArrayDirection.RIGHT},
        {"np": LEFT, "dir": MArrayDirection.LEFT},
    ]
    """Maps :class:`~.m_enum.MArrayDirection` to :class:`np.ndarray`."""

    def __calc_window_dim(self) -> typing.Tuple[float, float]:
        """Calculates dimensions of window mobject.

        Returns
        -------
        :class:`float`
            Height of :attr:`__mob_window`.
        :class:`float`
            Width of :attr:`__mob_window`.
        """

        height = self.__arr.fetch_mob_arr()[self.__index].fetch_mob_square().side_length
        width = self.__arr._MArray__sum_elem_len(
            self.__index, self.__index + self.__size - 1
        )

        if self.__arr.fetch_arr_dir() in (MArrayDirection.UP, MArrayDirection.DOWN):
            height, width = width, height

        return (height, width)

    def __calc_window_pos_np(self) -> typing.Tuple[np.ndarray, np.ndarray]:
        """Calculates position vector and align vector for the window mobject.

        Returns
        -------
        :class:`np.ndarray`
            Position vector for :attr:`__mob_window`
        :class:`np.ndarray`
            Align vector for :attr:`__mob_window`
        """

        point_np = (
            self.__arr.fetch_mob_arr()[self.__index].fetch_mob_square().get_left()
        )
        align_np = LEFT

        arr_dir = self.__arr.fetch_arr_dir()
        if arr_dir == MArrayDirection.LEFT:
            point_np = (
                self.__arr.fetch_mob_arr()[self.__index].fetch_mob_square().get_right()
            )
            align_np = RIGHT
        elif arr_dir == MArrayDirection.UP:
            point_np = (
                self.__arr.fetch_mob_arr()[self.__index].fetch_mob_square().get_bottom()
            )
            align_np = DOWN
        elif arr_dir == MArrayDirection.DOWN:
            point_np = (
                self.__arr.fetch_mob_arr()[self.__index].fetch_mob_square().get_top()
            )
            align_np = UP

        return (point_np, align_np)

    def __calc_label_pos_np(self) -> np.ndarray:
        """Calculates position vector for the label mobject.

        Returns
        -------
        :class:`np.ndarray`
            Position vector for :attr:`__mob_label`
        """

        arr_dir = self.__arr.fetch_arr_dir()
        # Label position is parallel to array growth direction
        if np.array_equal(
            self.__dir_map[self.__label_pos.value]["np"],
            self.__dir_map[arr_dir.value]["np"],
        ) or np.array_equal(
            self.__dir_map[self.__label_pos.value]["np"],
            -self.__dir_map[arr_dir.value]["np"],
        ):
            return self.__dir_map[(self.__label_pos.value + 2) % len(self.__dir_map)][
                "np"
            ]

        # Label position is perpendicular to array growth direction
        else:
            return self.__dir_map[self.__label_pos.value]["np"]

    def __pos_mobs(self, pos_window: bool = False, pos_label: bool = False) -> None:
        """Positions mobjects of the class.

        Parameters
        ----------
        pos_window
            If `True`, correctly positions :attr:`__mob_window`.
        pos_label
            If `True`, correctly positions :attr:`__mob_label`.
        """

        if pos_window:
            point_np, align_np = self.__calc_window_pos_np()
            self.__mob_window.move_to(point_np, align_np)

        if pos_label:
            self.__mob_label.next_to(
                self.__mob_window,
                self.__calc_label_pos_np(),
                self.__label_gap,
            )

    def __add_updater(self) -> None:
        """Attaches the position updater function with the pointer."""

        def updater_pos(mob: Mobject) -> None:
            self.__init_pos()

        self.__updater_pos = updater_pos

        self.add_updater(self.__updater_pos)

    def __remove_updater(self) -> None:
        """Removes the attached position updater function from the pointer."""

        self.remove_updater(self.__updater_pos)

    def __init_props(
        self,
        scene: Scene,
        arr: MArray,
        index: int,
        size: int,
        label: str,
        label_gap: float,
        label_pos: MArrayDirection,
    ) -> None:
        """Initializes the attributes for the class.

        Parameters
        ----------
        scene
            Specifies the scene where the object is to be rendered.
        arr
            Specifies the array to which the sliding window is to be attached.
        index
            Specifies the index of the element to which the sliding window is to be attached.
        size
            Specifies the number of elements the sliding window should enclose.
        label
            Specifies the value of the sliding window label.
        label_gap
            Specifies the distance between :attr:`__mob_label` and :attr:`__mob_window`.
        label_pos
            Specifies the position of the pointer w.r.t to :attr:`__mob_window`.
        """

        self.__mob_window_props: dict = {"color": RED_D, "stroke_width": 10}
        self.__mob_label_props: dict = {"text": label, "color": RED_A, "font_size": 38}
        self.__scene: Scene = scene
        self.__arr: MArray = arr
        if index >= len(self.__arr.fetch_mob_arr()) or index < 0:
            raise Exception("Index out of bounds!")
        self.__index: int = index
        if size < 1 or index + size > len(self.__arr.fetch_mob_arr()):
            raise Exception("Invalid window size!")
        self.__size: int = size
        self.__label: str = label
        self.__label_gap: float = label_gap
        self.__label_pos: MArrayDirection = label_pos

    def __update_props(
        self, mob_window_args: dict = {}, mob_label_args: dict = {}
    ) -> None:
        """Updates the attributes of the class.

        Parameters
        ----------
        mob_window_args
            Arguments for :class:`~manim.mobject.geometry.polygram.Rectangle` that represents the window.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the window label.
        """

        self.__mob_window_props.update(mob_window_args)
        self.__mob_label_props["text"] = self.__label
        self.__mob_label_props.update(mob_label_args)

        if type(self.__mob_label_props["text"]) != str:
            self.__mob_label_props["text"] = str(self.__mob_label_props["text"])

    def __init_mobs(self, init_window: bool = False, init_label: bool = False) -> None:
        """Initializes the mobjects for the class.

        Parameters
        ----------
        init_arrow
            If `True`, instantiates a :class:`~manim.mobject.geometry.polygram.Rectangle` and assigns it to :attr:`__mob_window`.
        init_label
            If `True`, instantiates a :class:`~manim.mobject.text.text_mobject.Text` and assigns it to :attr:`__mob_label`.
        """

        if init_window:
            height, width = self.__calc_window_dim()
            self.__mob_window = Rectangle(
                height=height, width=width, **self.__mob_window_props
            )
            self.__pos_mobs(pos_window=True)
            self.add(self.__mob_window)

        if init_label:
            self.__mob_label = Text(**self.__mob_label_props)
            self.__pos_mobs(pos_label=True)
            self.add(self.__mob_label)

    def __init_pos(self) -> None:
        """Initializes the position of the object"""

        self.__pos_mobs(True, True)

    def __deepcopy__(self, memo):
        """Deepcopy that excludes attributes specified in `exclude_list`."""

        exclude_list = ["_MArraySlidingWindow__scene", "_MArraySlidingWindow__arr"]

        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result
        for k, v in self.__dict__.items():
            if k not in exclude_list:
                setattr(result, k, deepcopy(v, memo))
        return result

    def __init__(
        self,
        scene: Scene,
        arr: MArray,
        index: int = 0,
        size: int = 1,
        label: str = "",
        label_gap: float = 0.5,
        label_pos: MArrayDirection = MArrayDirection.DOWN,
        mob_window_args: dict = {},
        mob_label_args: dict = {},
        **kwargs
    ) -> None:
        """Initializes the class.

        Parameters
        ----------
        scene
            Specifies the scene where the object is to be rendered.
        arr
            Specifies the array to which the sliding window is to be attached.
        index
            Specifies the index of the element to which the sliding window is to be attached.
        size
            Specifies the number of elements the sliding window should enclose.
        label
            Specifies the value of the sliding window label.
        label_gap
            Specifies the distance between :attr:`__mob_label` and :attr:`__mob_window`.
        label_pos
            Specifies the position of the pointer w.r.t to :attr:`__mob_window`.
        mob_window_args
            Arguments for :class:`~manim.mobject.geometry.polygram.Rectangle` that represents the window.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the window label.
        **kwargs
            Forwarded to constructor of the parent.
        """

        super().__init__(**kwargs)

        # Initialize props
        self.__init_props(scene, arr, index, size, label, label_gap, label_pos)

        # Update props
        self.__update_props(mob_window_args, mob_label_args)

        # Initialize mobjects
        self.__init_mobs(True, True)

        # Add updater
        self.__add_updater()

    def fetch_mob_window(self) -> Rectangle:
        """Fetches the window mobject of the sliding window.

        Returns
        -------
        :class:`~manim.mobject.geometry.polygram.Rectangle`
            :attr:`__mob_window`.
        """

        return self.__mob_window

    def fetch_mob_label(self) -> Text:
        """Fetches the label mobject of the sliding window.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            :attr:`__mob_label`.
        """

        return self.__mob_label

    def update_mob_label(
        self,
        label: str,
        mob_label_args: dict = {},
        update_anim: Animation = Write,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Updates the window label.

        Parameters
        ----------
        label
            New value to be assigned to the window label.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the window label.
        update_anim
            Animation to be applied to the updated window label.
        update_anim_args
            Arguments for update :class:`~manim.animation.animation.Animation`.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated :attr:`__mob_label`.
        """

        self.__label = label

        # Update props of mob_label
        self.__update_props(mob_label_args=mob_label_args)

        # Remove current mob_label
        self.remove(self.__mob_label)

        # Initialize new mob_label
        self.__init_mobs(init_label=True)

        # Add new mob_label to group
        self.add(self.__mob_label)

        # Animate change
        if play_anim:
            self.__scene.play(
                update_anim(self.__mob_label, **update_anim_args), **play_anim_args
            )

        return self.__mob_label

    def animate_mob_window(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over window mobject.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :attr:`__mob_window`.
        """

        return self.__mob_window.animate

    def animate_mob_label(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over label mobject.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :attr:`__mob_label`.
        """

        return self.__mob_label.animate

    def shift_to_elem(
        self, index: int, play_anim: bool = True, play_anim_args: dict = {}
    ) -> ApplyFunction:
        """Shifts sliding window to the specified element.

        Parameters
        ----------
        index
            Specifies the index of the element to which the sliding window is to be shifted.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.animation.transform.ApplyFunction`
            Shift animation.
        """

        if index >= len(self.__arr.fetch_mob_arr()) or index < 0:
            raise Exception("Index out of bounds!")

        if self.__size < 1 or index + self.__size > len(self.__arr.fetch_mob_arr()):
            raise Exception("Invalid window size!")

        self.__index = index
        return self.resize_window(self.__size, play_anim, play_anim_args)

    def attach_to_elem(self, index: int) -> None:
        """Attaches pointer to the specified element.

        Parameters
        ----------
        index
            Specifies the index of the element to which the sliding window is to be attached.
        """

        if index >= len(self.__arr.fetch_mob_arr()) or index < 0:
            raise Exception("Index out of bounds!")

        if self.__size < 1 or index + self.__size > len(self.__arr.fetch_mob_arr()):
            raise Exception("Invalid window size!")

        self.__index = index
        self.__init_pos()

    def resize_window(
        self, size: int, play_anim: bool = True, play_anim_args: dict = {}
    ) -> ApplyFunction:
        """Expands or shrinks the window according to the specified size.

        Parameters
        ----------
        size
            Specifies the number of elements the sliding window should enclose.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.animation.transform.ApplyFunction`
            Resize animation.
        """

        if size < 1 or self.__index + size > len(self.__arr.fetch_mob_arr()):
            raise Exception("Invalid window size!")

        self.__size = size

        # Variables for resize_and_shift method
        arr_dir = self.__arr.fetch_arr_dir()
        height, width = self.__calc_window_dim()
        window_pos_np, window_align_np = self.__calc_window_pos_np()
        label_pos_np = self.__calc_label_pos_np()

        def resize_and_shift(mob: MArraySlidingWindow) -> MArraySlidingWindow:
            """Resizes and shifts the sliding window

            Returns
            -------
            :class:`MArraySlidingWindow`
                Represents the modified mobject.
            """

            if arr_dir in (MArrayDirection.UP, MArrayDirection.DOWN):
                mob.__mob_window.stretch_to_fit_height(height)
            else:
                mob.__mob_window.stretch_to_fit_width(width)
            mob.__mob_window.move_to(window_pos_np, window_align_np)
            mob.__mob_label.next_to(mob.__mob_window, label_pos_np, mob.__label_gap)
            return mob

        resize_anim = ApplyFunction(
            resize_and_shift, self, suspend_mobject_updating=True
        )

        if play_anim:
            self.__scene.play(resize_anim, **play_anim_args)

        return resize_anim
