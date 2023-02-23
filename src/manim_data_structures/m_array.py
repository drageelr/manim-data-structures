"""Contains classes to construct an array."""

from __future__ import annotations
from copy import deepcopy

import numpy as np
from manim import *

from .m_element import MArrayElement
from .m_enum import MArrayDirection, MArrayElementComp

class MArray(VGroup):
    """A class that represents an array.

    Parameters
    ----------
    scene
        Specifies the scene where the object is to be rendered.
    arr
        Specifies the array to represent.
    label
        Specifies the value of the array label.
    index_offset
        Specifies the difference between successive displayable indices.
    index_start
        Specifies the starting value of displayable index.
    index_hex_display
        If `True`, displays indices in hex.
    hide_index
        If `True`, doesn't display indices.
    arr_dir
        Specifies the growth direction of the array.
    arr_label_pos
        Specifies the position of :attr:`__mob_arr_label` w.r.t :attr:`__mob_arr`.
    arr_label_gap
        Specifies the distance between :attr:`__mob_arr_label` and :attr:`__mob_arr`.
    mob_arr_label_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the array label.
    mob_square_args
        Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the element body.
    mob_value_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
    mob_index_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
    **kwargs
        Forwarded to constructor of the parent.

    Attributes
    ----------
    __scene : :class:`~manim.scene.scene.Scene`
        The scene where the object is to be rendered.
    __arr : :class:`list`
        The array to represent.
    __label : :class:`str`
        The value of the array label.
    __index_offset : :class:`int`
        The difference between successive displayable indices.
    __index_start : :class:`int`
        The starting value of displayable index.
    __index_hex_display : :class:`bool`
        If `True`, displays indices in hex.
    __hide_index : :class:`bool`
        If `True`, doesn't display indices.
    __arr_dir : :class:`~.m_enum.MArrayDirection`
        The growth direction of the array.
    __arr_label_pos : :class:`~.m_enum.MArrayDirection`
        The position of :attr:`__mob_arr_label` w.r.t :attr:`__mob_arr`.
    __arr_label_gap : :class:`float`
        The distance between :attr:`__mob_arr_label` and :attr:`__mob_arr`.
    __mob_arr_label_props : :class:`dict`
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the array label.
    __mob_arr : :class:`~typing.List`\0[:class:`MArrayElement`]
        Represents the array.
    __mob_arr_label : :class:`~manim.mobject.text.text_mobject.Text`
        Represents the array label.
    """

    __dir_map = [
        {"arr": UP, "index": RIGHT},
        {"arr": DOWN, "index": RIGHT},
        {"arr": RIGHT, "index": UP},
        {"arr": LEFT, "index": UP},
    ]
    """Maps :class:`~.m_enum.MArrayDirection` to :class:`np.ndarray`."""

    def __sum_elem_len(self, index_start: int, index_end: int) -> int:
        """Sums the side_length of all elements' square mobject present in the array between the specified range.

        Parameters
        ----------
        index_start
            Starting index of the range (inclusive).
        index_end
            Ending index of the range (inclusive).

        Returns
        -------
        :class:`int`
            Sum of `side_length`\0s of all :class:`~manim.mobject.geometry.polygram.Square` present inside :attr:`__mob_arr` in the specified range.
        """

        if (
            index_start < 0 or
            index_end < 0 or
            index_start > len(self.__mob_arr) or
            index_end > len(self.__mob_arr)
        ):
            raise Exception("Index out of bounds!")

        total_len = 0
        for i in range(index_start, index_end + 1):
            total_len += self.__mob_arr[i].fetch_mob_square().side_length
        return total_len

    def __calc_label_pos_and_mob(self) -> typing.Tuple[Square, np.ndarray]:
        """Calculates the position of the array label relative to one of the element's square mobjects.

        Returns
        -------
        :class:`~manim.mobject.geometry.polygram.Square`
            Square mobject next to which the array label is positioned.
        :class:`np.ndarray`
            The relative position of the array label.
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
                odd_indices = len(self.__mob_arr) % 2 == 1
                middle_index = int(len(self.__mob_arr) / 2)
                len_before = self.__sum_elem_len(0, middle_index - 1)
                len_after = self.__sum_elem_len(
                    middle_index + 1 if odd_indices else middle_index,
                    len(self.__mob_arr) - 1,
                )
            return (
                self.__mob_arr[middle_index].fetch_mob_square(),
                self.__dir_map[self.__arr_label_pos.value]["arr"]
                + self.__dir_map[self.__arr_dir.value]["arr"]
                * ((len_after - len_before) / 2),
            )

    def __calc_index(self, index: int) -> typing.Union[int, str]:
        """Calculates the displayable index of the specified element based on attributes set at initialization.

        Parameters
        ----------
        index
            Specifies the index of the element for which to compute the displayable index.

        Returns
        -------
        :data:`~typing.Union`\0[:class:`int`, :class:`str`]
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
        """Calculates the index position of all elements based on attributes set at initialization.

        Returns
        -------
        :class:`np.ndarray`
            Index position.
        """

        return (
            self.__dir_map[self.__arr_dir.value]["index"]
            if not self.__switch_index_pos
            else self.__dir_map[self.__arr_dir.value]["index"] * -1
        )

    def __calc_label_shift_factor(self, mob: MArrayElement) -> float:
        """Calculates how much to shift the array label after insertion/removal of an element.

        Parameters
        ----------
        mob
            Specifies the element that is inserted/removed.

        Returns
        -------
        :class:`float`
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
        """Creates and inserts a new element in the array.

        Parameters
        ----------
        value
            Specifies the value of the new element.
        shift_label
            If `True`, shifts the :attr:`__mob_arr_label` to center of the array.
        append_anim
            Animation to be applied to the new element.
        append_anim_args
            Arguments for append :class:`~manim.animation.animation.Animation`.
        append_anim_target
            Specifies the target :class:`~manim.mobject.mobject.Mobject` of the :class:`MArrayElement` on which the append :class:`~manim.animation.animation.Animation` is to be played.
        mob_square_args
            Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the element body.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.

        Returns
        -------
        :data:`typing.List`\0[:class:`~manim.animation.animation.Animation`]
            List of append animations.
        """

        mob_value_args["text"] = value
        mob_index_args["text"] = self.__calc_index(len(self.__mob_arr))
        self.__mob_arr.append(
            MArrayElement(
                scene=self.__scene,
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
        update_anim: Animation = Indicate,
        removal_anim_args: dict = {},
        update_anim_args: dict = {},
        removal_anim_target: MArrayElementComp = None,
        update_anim_target: MArrayElementComp = MArrayElementComp.INDEX,
    ) -> typing.Tuple[Succession, typing.Callable[[bool], typing.List[Animation]]]:
        """Removes the element from the array at the specified index.

        Parameters
        ----------
        index
            Specifies the index of the element to remove.
        removal_anim
            Animation to be applied to the element being removed.
        update_anim
            Animation to be applied on remaining elements.
        removal_anim_args
            Arguments for removal :class:`~manim.animation.animation.Animation`.
        update_anim_args
            Arguments for update :class:`~manim.animation.animation.Animation`.
        removal_anim_target
            Specifies the target :class:`~manim.mobject.mobject.Mobject` of the :class:`MArrayElement` on which the removal :class:`~manim.animation.animation.Animation` is to be played.
        update_anim_target
            Specifies the target :class:`~manim.mobject.mobject.Mobject` of the :class:`MArrayElement` on which the update :class:`~manim.animation.animation.Animation` is to be played.

        Returns
        -------
        :class:`~manim.animation.composition.Succession`
            Contains :class:`~manim.animation.animation.Animation` played for removal and shifting of element(s).
        :data:`~typing.Callable`\0[[:class:`bool`], :class:`~typing.List`\0[:class:`~manim.animation.animation.Animation`]]
            Method that updates the indices of element(s) after the removed element and returns a list of update :class:`~manim.animation.animation.Animation`\0(s).
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

        def update_indices(
            play_anim: bool = True, play_anim_args: dict = {}
        ) -> typing.List[Animation]:
            """Updates the indices of :class:`MArrayElement`(s) that occur after the removal.

            Parameters
            ----------
            play_anim : :class:`bool`, default: `True`
                Specifies whether to play the update :class:`manim.Animation`.
            play_anim_args : :class:`dict, default: `{}`
                Arguments for :meth:`manim.Scene.play`.

            Returns
            -------
            List[:class:`manim.Animation`]
                Represents :class:`Animation` for indices update.
            """

            anims_index = []
            for i in range(index, len(self.__mob_arr)):
                self.__mob_arr[i].update_mob_index(
                    mob_index_args={"text": self.__calc_index(i)}, play_anim=False
                )
                anims_index.append(
                    update_anim(
                        (self.__mob_arr[i].fetch_mob(update_anim_target)),
                        **update_anim_args
                    )
                )

            if play_anim:
                self.__scene.play(*anims_index, **play_anim_args)

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

    def __init_props(
        self,
        scene: Scene,
        arr: list,
        label: str,
        index_offset: int,
        index_start: int,
        index_hex_display: bool,
        hide_index: bool,
        arr_dir: MArrayDirection,
        switch_index_pos: bool,
        arr_label_pos: MArrayDirection,
        arr_label_gap: float,
    ) -> None:
        """Initializes the attributes for the class.

        Parameters
        ----------
        scene
            Specifies the scene where the object is to be rendered.
        arr
            Specifies the array to represent.
        label
            Specifies the value of the array label.
        index_offset
            Specifies the difference between successive displayable indices.
        index_start
            Specifies the starting value of displayable index.
        index_hex_display
            If `True`, displays indices in hex.
        hide_index
            If `True`, doesn't display indices.
        arr_dir
            Specifies the growth direction of the array.
        arr_label_pos
            Specifies the position of :attr:`__mob_arr_label` w.r.t :attr:`__mob_arr`.
        arr_label_gap
            Specifies the distance between :attr:`__mob_arr_label` and :attr:`__mob_arr`.
        """

        self.__mob_arr_label_props: dict = {
            "text": "",
            "color": BLUE_A,
            "font_size": 38,
        }
        self.__scene: Scene = scene
        self.__arr: typing.List[Any] = arr
        self.__label: str = label
        self.__mob_arr: typing.List[MArrayElement] = []
        self.__index_offset: int = index_offset
        self.__index_start: int = index_start
        self.__index_hex_display: bool = index_hex_display
        self.__hide_index: int = hide_index
        self.__arr_dir: MArrayDirection = arr_dir
        self.__switch_index_pos: bool = switch_index_pos
        self.__arr_label_pos: MArrayDirection = arr_label_pos
        self.__arr_label_gap: float = arr_label_gap

    def __update_props(
        self,
        mob_arr_label_args: dict = {},
    ) -> None:
        """Updates the attributes of the class.

        Parameters
        ----------
        mob_arr_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the array label.
        """

        self.__mob_arr_label_props["text"] = self.__label
        self.__mob_arr_label_props.update(mob_arr_label_args)

        if type(self.__mob_arr_label_props["text"]) != str:
            self.__mob_arr_label_props["text"] = str(self.__mob_arr_label_props["text"])

    def __init_mobs(
        self,
        init_arr_label: bool = False,
    ) -> None:
        """Initializes the mobjects for the class.

        Parameters
        ----------
        init_arr_label
            If `True`, instantiates a :class:`~manim.mobject.text.text_mobject.Text` and assigns it to :attr:`__mob_arr_label`.
        """

        if init_arr_label:
            self.__mob_arr_label = Text(**self.__mob_arr_label_props)
            if len(self.__mob_arr):
                (next_to_mob, label_pos) = self.__calc_label_pos_and_mob()
                self.__mob_arr_label.next_to(
                    next_to_mob, label_pos, self.__arr_label_gap
                )
                if len(self.__mob_arr) % 2 == 0:
                    self.__mob_arr_label.shift(
                        -self.__dir_map[self.__arr_dir.value]["arr"]
                        * (next_to_mob.side_length / 2)
                    )
            self.add(self.__mob_arr_label)

    def __deepcopy__(self, memo):
        """Deepcopy that excludes attributes specified in `exclude_list`."""

        exclude_list = ["_MArray__scene"]

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
        arr: list = [],
        label: str = "",
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
        scene
            Specifies the scene where the object is to be rendered.
        arr
            Specifies the array to represent.
        label
            Specifies the value of the array label.
        index_offset
            Specifies the difference between successive displayable indices.
        index_start
            Specifies the starting value of displayable index.
        index_hex_display
            If `True`, displays indices in hex.
        hide_index
            If `True`, doesn't display indices.
        arr_dir
            Specifies the growth direction of the array.
        arr_label_pos
            Specifies the position of :attr:`__mob_arr_label` w.r.t :attr:`__mob_arr`.
        arr_label_gap
            Specifies the distance between :attr:`__mob_arr_label` and :attr:`__mob_arr`.
        mob_arr_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the array label.
        mob_square_args
            Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the element body.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
        **kwargs
            Forwarded to constructor of the parent.
        """

        super().__init__(**kwargs)

        # Initialize props
        self.__init_props(
            scene,
            arr,
            label,
            index_offset,
            index_start,
            index_hex_display,
            hide_index,
            arr_dir,
            switch_index_pos,
            arr_label_pos,
            arr_label_gap,
        )

        # Update props
        self.__update_props(mob_arr_label_args)

        # Append elements to __mob_arr
        for v in arr:
            self.__append_elem(
                v,
                False,
                mob_square_args=mob_square_args,
                mob_value_args=mob_value_args,
                mob_index_args=mob_index_args,
            )

        # Initialize other mobjects (e.g. __arr_label)
        self.__init_mobs(True)

    def fetch_arr(self) -> list:
        """Fetches the original array.

        Returns
        -------
        :class:`list`
            :attr:`__arr`.
        """

        return self.__arr

    def fetch_mob_arr(self) -> typing.List[MArrayElement]:
        """Fetches the mobject array.

        Returns
        -------
        :class:`~typing.List`
            :attr:`__mob_arr`.
        """

        return self.__mob_arr

    def fetch_mob_arr_label(self) -> Text:
        """Fetches the label mobject of the array.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            :attr:`__mob_arr_label`.
        """

        return self.__mob_arr_label

    def fetch_arr_dir(self) -> MArrayDirection:
        """Fetches the growth direction enum of the array.

        Returns
        -------
        :class:`~.m_enum.MArrayDirection`
            :attr:`__arr_dir`.
        """

        return self.__arr_dir

    def update_elem_value(
        self,
        index: int,
        value,
        mob_value_args: dict = {},
        update_anim: Animation = Write,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Updates the elements value.

        Parameters
        ----------
        index
            Specifies the index of element whose value to update.
        value
            New value to be assigned to the element.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
        update_anim
            Animation to be applied to the updated element.
        update_anim_args
            Arguments for update :class:`~manim.animation.animation.Animation`.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated element's value mobject.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        self.__arr[index] = value
        mob_value_args["text"] = value
        return self.__mob_arr[index].update_mob_value(
            mob_value_args, update_anim, update_anim_args, play_anim, play_anim_args
        )

    def update_elem_index(
        self,
        index: int,
        value,
        mob_index_args: dict = {},
        update_anim: Animation = Write,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Updates the elements index.

        Parameters
        ----------
        index
            Specifies the index of element whose index to update.
        value
            New value to be assigned to the index of the element.
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
        update_anim
            Animation to be applied to the updated element.
        update_anim_args
            Arguments for update :class:`~manim.animation.animation.Animation`.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated element's index mobject.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        mob_index_args["text"] = value
        return self.__mob_arr[index].update_mob_index(
            mob_index_args, update_anim, update_anim_args, play_anim, play_anim_args
        )

    def update_mob_arr_label(
        self,
        label: str,
        mob_arr_label_args: dict = {},
        update_anim: Animation = Write,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Updates the array label.

        Parameters
        ----------
        label
            New value to be assigned to the array label.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the array label.
        update_anim
            Animation to be applied to the updated array label.
        update_anim_args
            Arguments for update :class:`~manim.animation.animation.Animation`.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated :attr:`__mob_arr_label`.
        """

        self.__label = label

        # Update props of mob_label
        self.__update_props(mob_arr_label_args=mob_arr_label_args)

        # Remove current mob_label
        self.remove(self.__mob_arr_label)

        # Initialize new mob_label
        self.__init_mobs(init_arr_label=True)

        # Add new mob_label to group
        self.add(self.__mob_arr_label)

        # Animate change
        if play_anim:
            self.__scene.play(
                update_anim(self.__mob_arr_label, **update_anim_args), **play_anim_args
            )

        return self.__mob_arr_label

    def animate_elem(self, index: int) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over element mobject specified.

        Parameters
        ----------
        index
            Specifies the index of the element to animate.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :class:`MArrayElement`.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        return self.__mob_arr[index].animate

    def animate_elem_square(self, index: int) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over square mobject of the specified element.

        Parameters
        ----------
        index
            Specifies the index of the element who's square mobject to animate.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :class:`~manim.mobject.geometry.polygram.Square`.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        return self.__mob_arr[index].animate_mob_square()

    def animate_elem_value(self, index: int) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over value mobject of the specified element.

        Parameters
        ----------
        index
            Specifies the index of the element who's value mobject animate.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :class:`~manim.mobject.text.text_mobject.Text`.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        return self.__mob_arr[index].animate_mob_value()

    def animate_elem_index(self, index: int) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over index mobject of the specified element.

        Parameters
        ----------
        index
            Specifies the index of the element who's index mobject animate.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :class:`~manim.mobject.text.text_mobject.Text`.
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        return self.__mob_arr[index].animate_mob_index()

    def append_elem(
        self,
        value: Any,
        append_anim: Animation = Write,
        append_anim_args: dict = {},
        append_anim_target: MArrayElementComp = None,
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> typing.List[Animation]:
        """Creates and inserts a new element in the array.

        Parameters
        ----------
        value
            Specifies the value of the new element.
        append_anim
            Animation to be applied to the new element.
        append_anim_args
            Arguments for append :class:`~manim.animation.animation.Animation`.
        append_anim_target
            Specifies the target :class:`~manim.mobject.mobject.Mobject` of the :class:`MArrayElement` on which the append :class:`~manim.animation.animation.Animation` is to be played.
        mob_square_args
            Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the element body.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`typing.List`\0[:class:`~manim.animation.animation.Animation`]
            List of append animations.
        """

        self.__arr.append(value)

        anim_list = self.__append_elem(
            value,
            mob_square_args=mob_square_args,
            mob_value_args=mob_value_args,
            mob_index_args=mob_index_args,
            append_anim=append_anim,
            append_anim_args=append_anim_args,
            append_anim_target=append_anim_target,
        )

        if play_anim:
            self.__scene.play(*anim_list, **play_anim_args)

        return anim_list

    def remove_elem(
        self,
        index: int,
        removal_anim: Animation = FadeOut,
        update_anim: Animation = Indicate,
        removal_anim_args: dict = {},
        update_anim_args: dict = {},
        removal_anim_target: MArrayElementComp = None,
        update_anim_target: MArrayElementComp = MArrayElementComp.INDEX,
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> typing.Tuple[Succession, typing.Callable[[bool], typing.List[Animation]]]:
        """Removes the element from the array at the specified index.

        Parameters
        ----------
        index
            Specifies the index of the element to remove.
        removal_anim
            Animation to be applied to the element being removed.
        update_anim
            Animation to be applied on remaining elements.
        removal_anim_args
            Arguments for removal :class:`~manim.animation.animation.Animation`.
        update_anim_args
            Arguments for update :class:`~manim.animation.animation.Animation`.
        removal_anim_target
            Specifies the target :class:`~manim.mobject.mobject.Mobject` of the :class:`MArrayElement` on which the removal :class:`~manim.animation.animation.Animation` is to be played.
        update_anim_target
            Specifies the target :class:`~manim.mobject.mobject.Mobject` of the :class:`MArrayElement` on which the update :class:`~manim.animation.animation.Animation` is to be played.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.animation.composition.Succession`
            Contains :class:`~manim.animation.animation.Animation` played for removal and shifting of element(s).
        :data:`~typing.Callable`\0[[:class:`bool`], :class:`~typing.List`\0[:class:`~manim.animation.animation.Animation`]]
            Method that updates the indices of element(s) after the removed element and returns a list of update :class:`~manim.animation.animation.Animation`\0(s).
        """

        if index < 0 or index > len(self.__mob_arr):
            raise Exception("Index out of bounds!")

        self.__arr = self.__arr[0:index] + self.__arr[index + 1 :]

        (remove_anim, update_indices) = self.__remove_elem(
            index,
            removal_anim,
            update_anim,
            removal_anim_args,
            update_anim_args,
            removal_anim_target,
            update_anim_target,
        )

        if play_anim:
            self.__scene.play(remove_anim, **play_anim_args)
            update_indices(play_anim_args=play_anim_args)

        return (remove_anim, update_indices)
