from __future__ import annotations
from copy import deepcopy

import numpy as np
from manim import *

from .m_enum import MArrayDirection


class MArrayPointer(VGroup):
    """A class that represents a pointer.

    Parameters
    ----------
    scene
        Specifies the scene where the object is to be rendered.
    arr
        Specifies the array to which the pointer is to be attached.
    index
        Specifies the index of the element to which the pointer is to be attached.
    label
        Specifies the value of the pointer label.
    arrow_len
        Specifies the length of :attr:`__mob_arrow`.
    arrow_gap
        Specifies the distance between :attr:`__mob_arrow` and :attr:`__arr`.
    label_gap
        Specifies the distance between :attr:`__mob_arrow` and :attr:`__mob_label`.
    pointer_pos
        Specifies the position of the pointer w.r.t to :attr:`__arr`.
    mob_arrow_args
        Arguments for :class:`~manim.mobject.geometry.line.Arrow` that represents the pointer arrow.
    mob_label_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the pointer label.
    **kwargs
        Forwarded to constructor of the parent.

    Attributes
    ----------
    __scene : :class:`~manim.scene.scene.Scene`
        The scene where the object is to be rendered.
    __arr : :class:`~typing.List`\0[:class:`MArrayElement`]
        The array to which the pointer is attached to.
    __index : :class:`int`
        The index of the element to which the pointer is attached to.
    __label : :class:`str`
        The value of the pointer label.
    __arrow_len : :class:`float`
        The length of :attr:`__mob_arrow`.
    __arrow_gap : :class:`float`
        The distance between :attr:`__mob_arrow` and :attr:`__arr`.
    __label_gap : :class:`float`
        The distance between :attr:`__mob_arrow` and :attr:`__mob_label`.
    __pointer_pos : :class:`.m_enum.MArrayDirection`
        The position of the pointer w.r.t to :attr:`__arr`.
    __mob_arrow_props : :class:`dict`
        Arguments for :class:`~manim.mobject.geometry.line.Arrow` that represents the pointer arrow.
    __mob_label_props : :class:`dict`
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the pointer label.
    __mob_arrow : :class:`~manim.mobject.geometry.line.Arrow`
        Represents the arrow of the element.
    __mob_label : :class:`~manim.mobject.text.text_mobject.Text`
        Represents the label of the element.
    __updater_pos : :data:`typing.Callable`\0[[], None]
        The updater function that keeps the pointer intact with the array.
    """

    __dir_map = [
        {"np": UP, "dir": MArrayDirection.UP},
        {"np": DOWN, "dir": MArrayDirection.DOWN},
        {"np": RIGHT, "dir": MArrayDirection.RIGHT},
        {"np": LEFT, "dir": MArrayDirection.LEFT},
    ]
    """Maps :class:`~.m_enum.MArrayDirection` to :class:`np.ndarray`."""

    def __calc_arrow_pos(self) -> np.ndarray:
        """Calculates direction vector for the arrow mobject.

        Returns
        -------
        :class:`np.ndarray`
            Position vector for :attr:`__mob_arrow`.
        """

        arr_dir_np = self.__dir_map[self.__arr.fetch_arr_dir().value]["np"]
        arrow_pos_np = np.copy(self.__dir_map[self.__pointer_pos.value]["np"])

        # If array's direction and pointer's direction are not perpendicular to each other
        if np.dot(arr_dir_np, arrow_pos_np):
            # swap the x and y values of arrow_pos_np
            arrow_pos_np[0], arrow_pos_np[1] = arrow_pos_np[1], arrow_pos_np[0]
            # update the __pointer_pos accordingly
            self.__pointer_pos = self.__dir_map[
                (self.__pointer_pos.value + 2) % len(self.__dir_map)
            ]["dir"]

        return arrow_pos_np

    def __add_updater(self) -> None:
        """Attaches the position updater function with the pointer."""

        def updater_pos(mob: Mobject) -> None:
            self.__init_pos()

        self.__updater_pos = updater_pos

        self.add_updater(self.__updater_pos)

    def __remove_updater(self) -> None:
        """Removes the attached position updater function from the pointer."""

        self.remove_updater(self.__updater_pos)

    def __calc_shift_np(self, new_index: int) -> np.ndarray:
        """Calculates how much the pointer should shift by to point to the new index.

        Parameters
        ----------
        new_index
            Specifies the prospective index of element to which the pointer is to be attached.

        Returns
        -------
        :class:`np.ndarray`
            A vector that represents how much the pointer should shift.
        """

        to_lesser_index = False
        index_start = self.__index
        index_end = new_index
        if index_start > index_end:
            index_start, index_end = index_end, index_start
            to_lesser_index = True

        return (
            (
                self.__arr._MArray__sum_elem_len(index_start, index_end)
                - (
                    self.__arr.fetch_mob_arr()[self.__index]
                    .fetch_mob_square()
                    .side_length
                )
            )
            * self.__dir_map[self.__arr.fetch_arr_dir().value]["np"]
            * (-1 if to_lesser_index else 1)
        )

    def __init_props(
        self,
        scene: Scene,
        arr: MArray,
        index: int,
        label: str,
        arrow_len: float,
        arrow_gap: float,
        label_gap: float,
        pointer_pos: MArrayDirection,
    ) -> None:
        """Initializes the attributes for the class.

        Parameters
        ----------
        scene
            Specifies the scene where the object is to be rendered.
        arr
            Specifies the array to which the pointer is to be attached.
        index
            Specifies the index of the element to which the pointer is to be attached.
        label
            Specifies the value of the pointer label.
        arrow_len
            Specifies the length of :attr:`__mob_arrow`.
        arrow_gap
            Specifies the distance between :attr:`__mob_arrow` and :attr:`__arr`.
        label_gap
            Specifies the distance between :attr:`__mob_arrow` and :attr:`__mob_label`.
        pointer_pos
            Specifies the position of the pointer w.r.t to :attr:`__arr`.
        """

        self.__mob_arrow_props: dict = {"color": GOLD_D}
        self.__mob_label_props: dict = {"text": label, "color": GOLD_A, "font_size": 38}
        self.__scene: Scene = scene
        self.__arr: MArray = arr
        if index >= len(self.__arr.fetch_mob_arr()) or index < 0:
            raise Exception("Index out of bounds!")
        self.__index: int = index
        self.__label: str = label
        self.__arrow_len: float = arrow_len
        self.__arrow_gap: float = arrow_gap
        self.__label_gap: float = label_gap
        self.__pointer_pos: MArrayDirection = pointer_pos

    def __update_props(
        self, mob_arrow_args: dict = {}, mob_label_args: dict = {}
    ) -> None:
        """Updates the attributes of the class.

        Parameters
        ----------
        mob_arrow_args
            Arguments for :class:`~manim.mobject.geometry.line.Arrow` that represents the pointer arrow.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the pointer label.
        """

        self.__mob_arrow_props.update(mob_arrow_args)
        self.__mob_label_props["text"] = self.__label
        self.__mob_label_props.update(mob_label_args)

        if type(self.__mob_label_props["text"]) != str:
            self.__mob_label_props["text"] = str(self.__mob_label_props["text"])

    def __init_mobs(self, init_arrow: bool = False, init_label: bool = False) -> None:
        """Initializes the mobjects for the class.

        Parameters
        ----------
        init_arrow
            If `True`, instantiates a :class:`~manim.mobject.geometry.line.Arrow` and assigns it to :attr:`__mob_arrow`.
        init_label
            If `True`, instantiates a :class:`~manim.mobject.text.text_mobject.Text` and assigns it to :attr:`__mob_label`.
        """

        if init_arrow:
            arrow_pos_np = self.__calc_arrow_pos()
            self.__mob_arrow = Arrow(
                start=(-arrow_pos_np + (arrow_pos_np * self.__arrow_len)),
                end=-arrow_pos_np,
                **self.__mob_arrow_props
            )
            self.__mob_arrow.next_to(
                self.__arr.fetch_mob_arr()[self.__index].fetch_mob_square(),
                arrow_pos_np,
                self.__arrow_gap,
            )
            self.add(self.__mob_arrow)

        if init_label:
            self.__mob_label = Text(**self.__mob_label_props)
            self.__mob_label.next_to(
                self.__mob_arrow,
                self.__dir_map[self.__pointer_pos.value]["np"],
                self.__label_gap,
            )
            self.add(self.__mob_label)

    def __init_pos(self) -> None:
        """Initializes the position of the object"""

        arrow_pos_np = self.__calc_arrow_pos()
        self.next_to(
            self.__arr.fetch_mob_arr()[self.__index].fetch_mob_square(),
            arrow_pos_np,
            self.__arrow_gap,
        )

    def __deepcopy__(self, memo):
        """Deepcopy that excludes attributes specified in `exclude_list`."""

        exclude_list = ["_MArrayPointer__scene", "_MArrayPointer__arr"]

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
        label: str = "",
        arrow_len: float = 1,
        arrow_gap: float = 0.25,
        label_gap: float = 0.25,
        pointer_pos: MArrayDirection = MArrayDirection.DOWN,
        mob_arrow_args: dict = {},
        mob_label_args: dict = {},
        **kwargs
    ) -> None:
        """Initializes the class.

        Parameters
        ----------
        scene
            Specifies the scene where the object is to be rendered.
        arr
            Specifies the array to which the pointer is to be attached.
        index
            Specifies the index of the element to which the pointer is to be attached.
        label
            Specifies the value of the pointer label.
        arrow_len
            Specifies the length of :attr:`__mob_arrow`.
        arrow_gap
            Specifies the distance between :attr:`__mob_arrow` and :attr:`__arr`.
        label_gap
            Specifies the distance between :attr:`__mob_arrow` and :attr:`__mob_label`.
        pointer_pos
            Specifies the position of the pointer w.r.t to :attr:`__arr`.
        mob_arrow_args
            Arguments for :class:`~manim.mobject.geometry.line.Arrow` that represents the pointer arrow.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the pointer label.
        **kwargs
            Forwarded to constructor of the parent.
        """

        super().__init__(**kwargs)

        # Initialize props
        self.__init_props(
            scene, arr, index, label, arrow_len, arrow_gap, label_gap, pointer_pos
        )

        # Update props
        self.__update_props(mob_arrow_args, mob_label_args)

        # Initialize mobjects
        self.__init_mobs(True, True)

        # Add updater
        self.__add_updater()

    def fetch_mob_arrow(self) -> Arrow:
        """Fetches the arrow mobject of the pointer.

        Returns
        -------
        :class:`~manim.mobject.geometry.line.Arrow`
            :attr:`__mob_arrow`.
        """

        return self.__mob_arrow

    def fetch_mob_label(self) -> Text:
        """Fetches the label mobject of the pointer.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            :attr:`__mob_label`.
        """

        return self.__mob_label

    def fetch_index(self) -> int:
        """Fetches the index that the pointer is attached to.

        Returns
        -------
        :class:`int`
            :attr:`__index`.
        """

        return self.__index

    def update_mob_label(
        self,
        label: str,
        mob_label_args: dict = {},
        update_anim: Animation = Write,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Updates the pointer label.

        Parameters
        ----------
        label
            New value to be assigned to the pointer label.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the pointer label.
        update_anim
            Animation to be applied to the updated pointer label.
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

    def animate_mob_arrow(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over arrow mobject.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :attr:`__mob_arrow`.
        """

        return self.__mob_arrow.animate

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
    ) -> ApplyMethod:
        """Shifts pointer to the specified element.

        Parameters
        ----------
        index
            Specifies the index of the element to which the pointer is to be shifted.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.animation.transform.ApplyMethod`
            Shift animation.
        """

        if index < 0 or index > len(self.__arr.fetch_mob_arr()):
            raise Exception("Index out of bounds!")

        shift_anim = ApplyMethod(
            self.shift, self.__calc_shift_np(index), suspend_mobject_updating=True
        )
        self.__index = index

        if play_anim:
            self.__scene.play(shift_anim, **play_anim_args)

        return shift_anim

    def attach_to_elem(self, index: int) -> None:
        """Attaches pointer to the specified element.

        Parameters
        ----------
        index
            Specifies the index of the element to which the pointer is to be attached.
        """

        if index < 0 or index > len(self.__arr.fetch_mob_arr()):
            raise Exception("Index out of bounds!")

        self.__index = index
        self.__init_pos()

    def __lt__(self, other: MArrayPointer | int | MVariable) -> bool:
        """Checks if the pointer is less than the other pointer.

        Parameters
        ----------
        other
            The other pointer.

        Returns
        -------
        :class:`bool`
            `True` if the pointer's pointing index in the `MArray` is less than the other pointer, `False` otherwise.
        """
        from .m_variable import MVariable
        if isinstance(other, MArrayPointer):
            return self.__index < other.fetch_index()
        elif isinstance(other, MVariable):
            return self.__index < other.fetch_value()
        else:
            return self.__index < other

    def __le__(self, other: MArrayPointer | int | MVariable) -> bool:
        """Checks if the pointer is less than or equal to the other pointer.

        Parameters
        ----------
        other
            The other pointer.

        Returns
        -------
        :class:`bool`
            `True` if the pointer's pointing index in the `MArray` is less than or equal to the other pointer, `False` otherwise.
        """
        from .m_variable import MVariable
        if isinstance(other, MArrayPointer):
            return self.__index <= other.fetch_index()
        elif isinstance(other, MVariable):
            return self.__index <= other.fetch_value()
        else:
            return self.__index <= other

    def __gt__(self, other: MArrayPointer | int | MVariable) -> bool:
        """Checks if the pointer is greater than the other pointer.

        Parameters
        ----------
        other
            The other pointer.

        Returns
        -------
        :class:`bool`
            `True` if the pointer's pointing index in the `MArray` is greater than the other pointer, `False` otherwise.
        """
        from .m_variable import MVariable
        if isinstance(other, MArrayPointer):
            return self.__index > other.fetch_index()
        elif isinstance(other, MVariable):
            return self.__index > other.fetch_value()
        else:
            return self.__index > other

    def __ge__(self, other: MArrayPointer | int | MVariable) -> bool:
        """Checks if the pointer is greater than or equal to the other pointer.

        Parameters
        ----------
        other
            The other pointer.

        Returns
        -------
        :class:`bool`
            `True` if the pointer's pointing index in the `MArray` is greater than or equal to the other pointer, `False` otherwise.
        """
        from .m_variable import MVariable
        if isinstance(other, MArrayPointer):
            return self.__index >= other.fetch_index()
        elif isinstance(other, MVariable):
            return self.__index >= other.fetch_value()
        else:
            return self.__index >= other

    def __eq__(self, other: MArrayPointer | int | MVariable) -> bool:
        """Checks if the pointer is equal to the other pointer.

        Parameters
        ----------
        other
            The other pointer.

        Returns
        -------
        :class:`bool`
            `True` if the pointer's pointing index in the `MArray` is equal to the other pointer, `False` otherwise.
        """
        from .m_variable import MVariable
        if isinstance(other, MArrayPointer):
            return self.__index == other.fetch_index()
        elif isinstance(other, MVariable):
            return self.__index == other.fetch_value()
        else:
            return self.__index == other

    def __ne__(self, other: MArrayPointer | int | MVariable) -> bool:
        """Checks if the pointer is not equal to the other pointer.

        Parameters
        ----------
        other
            The other pointer.

        Returns
        -------
        :class:`bool`
            `True` if the pointer's pointing index in the `MArray` is not equal to the other pointer, `False` otherwise.
        """
        from .m_variable import MVariable
        return not self.__eq__(other)

    def __add__(self, other: MArrayPointer | int | MVariable) -> int:
        """
        return the addition of the index of the current pointer and the index of the other pointer if other is another pointer.
        return the addition of the index of the current pointer and the integer if other is an integer.
        return the addition of the index of the current pointer and the value of the other variable if other is a MVariable.

        Parameters
        ----------
        other
            The value to be added.

        Returns
        -------
        :class:`MArrayPointer`
            The pointer after adding the value.
        """
        from .m_variable import MVariable # do this because of circular import
        if isinstance(other, MArrayPointer):
            return self.__index + other.fetch_index()
        elif isinstance(other, MVariable):
            return self.__index + other.fetch_value()
        else:
            return self.__index + other
    def __sub__(self, other: MArrayPointer | int | MVariable) -> int:
        """
        return the subtraction of the index of the current pointer and the index of the other pointer if other is another pointer.
        return the subtraction of the index of the current pointer and the integer if other is an integer.
        return the subtraction of the index of the current pointer and the value of the other variable if other is a MVariable.
        ----------
        other
            The value to be subtracted.

        Returns
        -------
        :class:`MArrayPointer`
            The pointer after subtracting the value.
        """
        from .m_variable import MVariable
        if isinstance(other, MArrayPointer):
            return self.__index - other.fetch_index()
        elif isinstance(other, MVariable):
            return self.__index - other.fetch_value()
        else:
            return self.__index - other

    def __key(self) -> tuple:
        # return the tuple of all attributues, used for hashing
        return (self.__scene, self.__arr, self.__index, self.__label, self.__arrow_len, self.__arrow_gap, self.__label_gap,
            self.__pointer_pos, self.__updater_pos 
                )
    # def __hash__(self) -> int:
    #     return id(self)
