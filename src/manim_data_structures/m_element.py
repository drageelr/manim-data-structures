
from __future__ import annotations
from copy import deepcopy

import numpy as np
from manim import *

from .m_enum import MArrayElementComp

class MArrayElement(VGroup):
    """A class that represents an array element.

    Parameters
    ----------
    scene
        Specifies the scene where the object is to be rendered.
    mob_square_args
        Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the element body.
    mob_value_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
    mob_index_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
    mob_label_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element label.
    index_pos
        Specifies the position of :attr:`__mob_index` w.r.t :attr:`__mob_square`
    index_gap
        Specifies the distance between :attr:`__mob_index` and :attr:`__mob_square`.
    label_pos
        Specifies the position of :attr:`__mob_label` w.r.t :attr:`__mob_square`.
    label_gap
        Specifies the distance between :attr:`__mob_label` and :attr:`__mob_square`.
    next_to_mob
        Specifies the placement for :attr:`__mob_square` w.r.t another :class:`MArrayElement`.
    next_to_dir
        Specifies the direction of placement for :attr:`__mob_square` w.r.t another :class:`MArrayElement`.

    Attributes
    ----------
    __scene : :class:`~manim.scene.scene.Scene`
        The scene where the object is to be rendered.
    __mob_square_props : :class:`dict`
        Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the element body.
    __mob_value_props : :class:`dict`
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
    __mob_index_props : :class:`dict`
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
    __mob_label_props : :class:`dict`
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element label.
    __index_pos : :class:`np.ndarray`
        The position of :attr:`__mob_index` w.r.t :attr:`__mob_square`
    __index_gap : :class:`float`
        The distance between :attr:`__mob_index` and :attr:`__mob_square`.
    __label_pos : :class:`np.ndarray`
        The position of :attr:`__mob_label` w.r.t :attr:`__mob_square`.
    __label_gap : :class:`float`
        The distance between :attr:`__mob_label` and :attr:`__mob_square`.
    __mob_square : :class:`~manim.mobject.geometry.polygram.Square`
        Represents the body of the element.
    __mob_value : :class:`~manim.mobject.text.text_mobject.Text`
        Represents the value of the element.
    __mob_index : :class:`~manim.mobject.text.text_mobject.Text`
        Represents the index of the element.
    __mob_label : :class:`~manim.mobject.text.text_mobject.Text`
        Represents the label of the element.
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
        scene
            Specifies the scene where the object is to be rendered.
        index_pos
            Specifies the position of :attr:`__mob_index` w.r.t :attr:`__mob_square`
        index_gap
            Specifies the distance between :attr:`__mob_index` and :attr:`__mob_square`.
        label_pos
            Specifies the position of :attr:`__mob_label` w.r.t :attr:`__mob_square`.
        label_gap
            Specifies the distance between :attr:`__mob_label` and :attr:`__mob_square`.
        """

        self.__mob_square_props: dict = {
            "color": BLUE_B,
            "fill_color": BLUE_D,
            "fill_opacity": 1,
            "side_length": 1,
        }
        self.__mob_value_props: dict = {"text": "", "color": WHITE, "weight": BOLD}
        self.__mob_index_props: dict = {"text": "", "color": BLUE_D, "font_size": 32}
        self.__mob_label_props: dict = {"text": "", "color": BLUE_A, "font_size": 38}
        self.__scene: Scene = scene
        self.__index_pos: np.ndarray = index_pos
        self.__index_gap: float = index_gap
        self.__label_pos: np.ndarray = label_pos
        self.__label_gap: float = label_gap

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
        mob_square_args
            Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the element body.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element label.
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
        """Initializes the mobjects for the class.

        Parameters
        ----------
        init_square
            If `True`, instantiates a :class:`~manim.mobject.geometry.polygram.Square` and assigns it to :attr:`__mob_square`.
        init_value
            If `True`, instantiates a :class:`~manim.mobject.text.text_mobject.Text` and assigns it to :attr:`__mob_value`.
        init_index
            If `True`, instantiates a :class:`~manim.mobject.text.text_mobject.Text` and assigns it to :attr:`__mob_index`.
        init_label
            If `True`, instantiates a :class:`~manim.mobject.text.text_mobject.Text` and assigns it to :attr:`__mob_label`.
        next_to_mob
            Specifies placement for :attr:`__mob_square` w.r.t another :class:`MArrayElement`.
        next_to_dir
            Specifies direction of placement for :attr:`__mob_square` w.r.t another :class:`MArrayElement`.
        """

        if init_square:
            self.__mob_square: Square = Square(**self.__mob_square_props)
            if next_to_mob is not None:
                self.__mob_square.next_to(
                    next_to_mob.fetch_mob_square(), next_to_dir, 0
                )
            self.add(self.__mob_square)

        if init_value:
            self.__mob_value: Text = Text(**self.__mob_value_props)
            self.__mob_value.next_to(self.__mob_square, np.array([0, 0, 0]), 0)
            self.add(self.__mob_value)

        if init_index:
            self.__mob_index: Text = Text(**self.__mob_index_props)
            self.__mob_index.next_to(
                self.__mob_square, self.__index_pos, self.__index_gap
            )
            self.add(self.__mob_index)

        if init_label:
            self.__mob_label: Text = Text(**self.__mob_label_props)
            self.__mob_label.next_to(
                self.__mob_square, self.__label_pos, self.__label_gap
            )
            self.add(self.__mob_label)

    def __deepcopy__(self, memo):
        """Deepcopy that excludes attributes specified in `exclude_list`."""

        exclude_list = ["_MArrayElement__scene"]

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
        scene
            Specifies the scene where the object is to be rendered.
        mob_square_args
            Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the element body.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element label.
        index_pos
            Specifies the position of :attr:`__mob_index` w.r.t :attr:`__mob_square`
        index_gap
            Specifies the distance between :attr:`__mob_index` and :attr:`__mob_square`.
        label_pos
            Specifies the position of :attr:`__mob_label` w.r.t :attr:`__mob_square`.
        label_gap
            Specifies the distance between :attr:`__mob_label` and :attr:`__mob_square`.
        next_to_mob
            Specifies the placement for :attr:`__mob_square` w.r.t another :class:`MArrayElement`.
        next_to_dir
            Specifies the direction of placement for :attr:`__mob_square` w.r.t another :class:`MArrayElement`.
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
        """Fetches the square mobject.

        Returns
        -------
        :class:`~manim.mobject.geometry.polygram.Square`
            :attr:`__mob_square`.
        """

        return self.__mob_square

    def fetch_mob_value(self) -> Text:
        """Fetches the value mobject.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            :attr:`__mob_value`.
        """

        return self.__mob_value

    def fetch_mob_index(self) -> Text:
        """Fetches the index mobject.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            :attr:`__mob_index`.
        """

        return self.__mob_index

    def fetch_mob_label(self) -> Text:
        """Fetches the label mobject.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            :attr:`__mob_label`.
        """

        return self.__mob_label

    def fetch_mob(self, mob_target: MArrayElementComp) -> Mobject:
        """Fetches the mobject based on the specified enum.

        Parameters
        ----------
        mob_target
            Specifies the :class:`~manim.mobject.mobject.Mobject` to fetch.

        Returns
        -------
        :class:`~manim.mobject.mobject.Mobject`
            Mobject of the class.
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
        update_anim: Animation = Write,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Re-intializes the value mobject.

        Parameters
        ----------
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element value.
        update_anim
            Animation to be applied to the updated :attr:`__mob_value`.
        update_anim_args
            Arguments for update :class:`~manim.animation.animation.Animation`.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated :attr:`__mob_value`.
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
            self.__scene.play(
                update_anim(self.__mob_value, **update_anim_args), **play_anim_args
            )

        return self.__mob_value

    def update_mob_index(
        self,
        mob_index_args: dict = {},
        update_anim: Animation = Write,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Re-intializes the index mobject.

        Parameters
        ----------
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element index.
        update_anim
            Animation to be applied to the updated :attr:`__mob_index`.
        update_anim_args
            Arguments for update :class:`~manim.animation.animation.Animation`.
        play_anim
            If `True`, plays the animation(s).
        play_anim_args
            Arguments for :py:meth:`Scene.play() <manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated :attr:`__mob_index`.
        """

        # Update props of mob_index
        self.__update_props(mob_index_args=mob_index_args)

        # Remove current mob_index
        self.remove(self.__mob_index)

        # Initialize new mob_index
        self.__init_mobs(init_index=True)

        # Add new mob_index to group
        self.add(self.__mob_index)

        # Animate change
        if play_anim:
            self.__scene.play(
                update_anim(self.__mob_index, **update_anim_args), **play_anim_args
            )

        return self.__mob_index

    def update_mob_label(
        self,
        mob_label_args: dict = {},
        update_anim: Animation = Write,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Re-intializes the label mobject.

        Parameters
        ----------
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the element label.
        update_anim
            Animation to be applied to the updated :attr:`__mob_label`.
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

    def animate_mob_square(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over square mobject.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :attr:`__mob_square`.
        """

        return self.__mob_square.animate

    def animate_mob_value(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over value mobject.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :attr:`__mob_value`.
        """

        return self.__mob_value.animate

    def animate_mob_index(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over index mobject.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :attr:`__mob_index`.
        """

        return self.__mob_index.animate

    def animate_mob_label(self) -> "_AnimationBuilder":  # type: ignore
        """Invokes the animate property over label mobject.

        Returns
        -------
        :class:`_AnimationBuilder`
            Animate property of :attr:`__mob_label`.
        """

        return self.__mob_label.animate
