"""Contains classes to construct variable."""

from manim import *

from .m_array import MArrayElement


class MVariable(MArrayElement):
    """A class that represents a variable.

    Parameters
    ----------
    scene
        Specifies the scene where the object is to be rendered.
    value
        Specifies the value of the variable.
    index
        Specifies the index of the variable.
    label
        Specifies the label of the variable.
    mob_square_args
        Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the variable body.
    mob_value_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the variable value.
    mob_index_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the variable index.
    mob_label_args
        Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the variable label.
    **kwargs
        Forwarded to constructor of the parent.

    Attributes
    ----------
    __value : Any
        The value of the variable.
    __index : Union[:class:`str`, :class:`int`]
        The value of the index.
    __label : :class:`str`
        The value of the label.
    """

    def __init__(
        self,
        scene: Scene,
        value: Any = "",
        index: typing.Union[str, int] = "",
        label: str = "",
        mob_square_args: dict = {},
        mob_value_args: dict = {},
        mob_index_args: dict = {},
        mob_label_args: dict = {},
        **kwargs
    ) -> None:
        """Initializes the class.

        Parameters
        ----------
        scene
            Specifies the scene where the object is to be rendered.
        value
            Specifies the value of the variable.
        index
            Specifies the index of the variable.
        label
            Specifies the label of the variable.
        mob_square_args
            Arguments for :class:`~manim.mobject.geometry.polygram.Square` that represents the variable body.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the variable value.
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the variable index.
        mob_label_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the variable label.
        **kwargs
            Forwarded to constructor of the parent.
        """

        self.__value: Any = value
        self.__index: typing.Union[str, int] = index
        self.__label: str = label

        mob_value_args["text"] = value
        mob_index_args["text"] = index
        mob_label_args["text"] = label

        super().__init__(
            scene=scene,
            mob_square_args=mob_square_args,
            mob_value_args=mob_value_args,
            mob_index_args=mob_index_args,
            mob_label_args=mob_label_args,
            **kwargs
        )

    def fetch_value(self) -> Any:
        """Fetches the value of the variable.

        Returns
        -------
        Any
            :attr:`__value`.
        """

        return self.__value

    def fetch_index(self) -> typing.Union[str, int]:
        """Fetches the index of the variable.

        Returns
        -------
        Union[:class:`str`, :class:`int`]
            :attr:`__index`.
        """

        return self.__index

    def fetch_label(self) -> str:
        """Fetches the label of the variable.

        Returns
        -------
        :class:`str`
            :attr:`__label`.
        """

        return self.__label

    def update_value(
        self,
        value: Any,
        mob_value_args: dict = {},
        update_anim: Animation = Indicate,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Updates the value of the variable.

        Parameters
        ----------
        value
            New value to be assigned to the variable.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the variable value.
        update_anim
            Animation to be applied to the updated :class:`~manim.mobject.text.text_mobject.Text`.
        update_anim_args
            Arguments for the update :class:`~manim.animation.animation.Animation`.
        play_anim
            Specifies whether to play the :class:`~manim.animation.animation.Animation`.
        play_anim_args
            Arguments for :meth:`Scene.play <~manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated :attr:`__value`.
        """

        self.__value = value
        mob_value_args["text"] = value
        return self.update_mob_value(
            mob_value_args, update_anim, update_anim_args, play_anim, play_anim_args
        )

    def update_index(
        self,
        index: typing.Union[str, int],
        mob_index_args: dict = {},
        update_anim: Animation = Indicate,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Updates the index of the variable.

        Parameters
        ----------
        index
            New index to be assigned to the variable.
        mob_index_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the variable index.
        update_anim
            Animation to be applied to the updated :class:`~manim.mobject.text.text_mobject.Text`.
        update_anim_args
            Arguments for the update :class:`~manim.animation.animation.Animation`.
        play_anim
            Specifies whether to play the :class:`~manim.animation.animation.Animation`.
        play_anim_args
            Arguments for :meth:`Scene.play <~manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated :attr:`__index`.
        """

        self.__index = index
        mob_index_args["text"] = index
        return self.update_mob_index(
            mob_index_args, update_anim, update_anim_args, play_anim, play_anim_args
        )

    def update_label(
        self,
        label: str,
        mob_label_args: dict = {},
        update_anim: Animation = Indicate,
        update_anim_args: dict = {},
        play_anim: bool = True,
        play_anim_args: dict = {},
    ) -> Text:
        """Updates the label of the variable.

        Parameters
        ----------
        label
            New label to be assigned to the variable.
        mob_value_args
            Arguments for :class:`~manim.mobject.text.text_mobject.Text` that represents the label value.
        update_anim
            Animation to be applied to the updated :class:`~manim.mobject.text.text_mobject.Text`.
        update_anim_args
            Arguments for the update :class:`~manim.animation.animation.Animation`.
        play_anim
            Specifies whether to play the :class:`~manim.animation.animation.Animation`.
        play_anim_args
            Arguments for :meth:`Scene.play <~manim.scene.scene.Scene.play>`.

        Returns
        -------
        :class:`~manim.mobject.text.text_mobject.Text`
            Updated :attr:`__label`.
        """

        self.__value = label
        mob_label_args["text"] = label
        return self.update_mob_label(
            mob_label_args, update_anim, update_anim_args, play_anim, play_anim_args
        )
