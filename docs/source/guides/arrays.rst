.. include:: ../refsub.rst

Animating Arrays
================

Manim Array - MArray
--------------------

The most basic data structure this package provides is the |MArray| (short for Manim Array 😄). To create a |MArray| simply create an instance by passing a python |list|.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3])
            self.play(Create(arr))
            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3])
            self.play(Create(arr))
            self.wait(1)

Animating MArray
~~~~~~~~~~~~~~~~

To animate the |MArray|, simply invoke the |Mobject.animate| property as shown below:

.. code-block:: python
    :linenos:

    self.play(arr.animate.shift(UP * 2 + LEFT * 5))

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3])
            self.play(Create(arr))
            self.play(arr.animate.shift(UP * 2 + LEFT * 5))
            self.wait(1)

Moreover, you can also use the |MArray.animate_elem| method to animate a single element of the |MArray| as well:

.. code-block:: python
    :linenos:

    self.play(arr.animate_elem(1).shift(DOWN))

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3])
            self.play(Create(arr))
            self.play(arr.animate_elem(1).shift(DOWN))
            self.wait(1)

Lastly, you can also animate the body, value and the index of any element using the |MArray.animate_elem_body|, |MArray.animate_elem_value| and |MArray.animate_elem_index| respectively.

.. code-block:: python
    :linenos:

    self.play(
        arr.animate_elem_body(1).set_fill(BLACK),
        arr.animate_elem_value(1).set_fill(RED),
        arr.animate_elem_index(1).rotate(PI / 2)
    )

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3])
            self.play(Create(arr))
            self.play(
                arr.animate_elem_body(1).set_fill(BLACK),
                arr.animate_elem_value(1).set_fill(RED),
                arr.animate_elem_index(1).rotate(PI / 2)
            )
            self.wait(1)

Customizing MArray
~~~~~~~~~~~~~~~~~~

The |MArray| also allows you to alter the way your array looks. While creating your array pass arguments to |Square| (used to represent the element body) and |Text| (used to represent the element value and index) mobjects.

.. code-block:: python
    :linenos:

    arr = MArray(
        self,
        [1, 2, 3],
        mob_elem_body_args={'fill_color': RED_D},
        mob_elem_value_args={'color': BLACK},
        mob_elem_index_args={'color': GOLD_A}
    )

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(
                self,
                [1, 2, 3],
                mob_elem_body_args={'fill_color': RED_D},
                mob_elem_value_args={'color': BLACK},
                mob_elem_index_args={'color': GOLD_A}
            )
            self.play(Create(arr))
            self.wait(1)

Growth Direction
^^^^^^^^^^^^^^^^

Furthermore, you can also create |MArray| that grows in different directions (e.g. up, down, right and left etc.).

To do this, simply pass your preferred direction enum from |MArrayDirection| as the ``arr_dir`` argument to the constructor. The code snippet below generates four different arrays in each direction.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr_up = MArray(self, [1, 2], arr_dir=MArrayDirection.UP)
            arr_right = MArray(self, [3, 4], arr_dir=MArrayDirection.RIGHT)
            arr_down = MArray(self, [5, 6], arr_dir=MArrayDirection.DOWN)
            arr_left = MArray(self, [7, 8], arr_dir=MArrayDirection.LEFT)

            self.play(Create(arr_up))
            self.play(arr_up.animate.shift(UP * 2))
            self.play(Create(arr_right))
            self.play(arr_right.animate.shift(RIGHT * 2))
            self.play(Create(arr_down))
            self.play(arr_down.animate.shift(DOWN * 2))
            self.play(Create(arr_left))
            self.play(arr_left.animate.shift(LEFT * 2))

            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr_up = MArray(self, [1, 2], arr_dir=MArrayDirection.UP)
            arr_right = MArray(self, [3, 4], arr_dir=MArrayDirection.RIGHT)
            arr_down = MArray(self, [5, 6], arr_dir=MArrayDirection.DOWN)
            arr_left = MArray(self, [7, 8], arr_dir=MArrayDirection.LEFT)

            self.play(Create(arr_up))
            self.play(arr_up.animate.shift(UP * 2))
            self.play(Create(arr_right))
            self.play(arr_right.animate.shift(RIGHT * 2))
            self.play(Create(arr_down))
            self.play(arr_down.animate.shift(DOWN * 2))
            self.play(Create(arr_left))
            self.play(arr_left.animate.shift(LEFT * 2))

            self.wait(1)

Array Label
^^^^^^^^^^^

For an |MArray|, you can also a label with the array via specifying the ``label`` argument.

Similar to how we specify the growth direction using |MArrayDirection| enum, we can dictate the position of the label.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr_label_left = MArray(self, [1, 2, 3], label='Arr')
            arr_label_right = MArray(self, [1, 2, 3], label='Arr', arr_label_pos=MArrayDirection.RIGHT)
            arr_label_down = MArray(self, [1, 2, 3], label='Arr', arr_label_pos=MArrayDirection.DOWN)
            arr_label_up = MArray(self, [1, 2, 3], label='Arr', arr_label_pos=MArrayDirection.UP, arr_label_gap=0.75)

            self.play(Create(arr_label_left))
            self.play(arr_label_left.animate.shift(UP * 2 + LEFT * 4))
            self.play(Create(arr_label_right))
            self.play(arr_label_right.animate.shift(DOWN * 2 + LEFT * 4))
            self.play(Create(arr_label_down))
            self.play(arr_label_down.animate.shift(UP * 2 + RIGHT))
            self.play(Create(arr_label_up))
            self.play(arr_label_up.animate.shift(DOWN * 2 + RIGHT))

            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr_label_left = MArray(self, [1, 2, 3], label='Arr')
            arr_label_right = MArray(self, [1, 2, 3], label='Arr', arr_label_pos=MArrayDirection.RIGHT)
            arr_label_down = MArray(self, [1, 2, 3], label='Arr', arr_label_pos=MArrayDirection.DOWN)
            arr_label_up = MArray(self, [1, 2, 3], label='Arr', arr_label_pos=MArrayDirection.UP, arr_label_gap=0.75)

            self.play(Create(arr_label_left))
            self.play(arr_label_left.animate.shift(UP * 2 + LEFT * 4))
            self.play(Create(arr_label_right))
            self.play(arr_label_right.animate.shift(DOWN * 2 + LEFT * 4))
            self.play(Create(arr_label_down))
            self.play(arr_label_down.animate.shift(UP * 2 + RIGHT))
            self.play(Create(arr_label_up))
            self.play(arr_label_up.animate.shift(DOWN * 2 + RIGHT))

            self.wait(1)

.. note::

    The ``arr_label_gap`` argument specifies the distance between the |MArrayElement| 's |Square| and the array label itself.

Hex Indices
^^^^^^^^^^^

Lets say you want to show a 4-byte integer array with its addresses. You can simply achieve this by using ``index_hex_display`` and ``index_offset`` arguments of the |MArray| constructor.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(
                self,
                [1, 2, 3, 4],
                index_hex_display=True,
                index_offset=4
            )
            self.play(Create(arr))
            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(
                self,
                [1, 2, 3, 4],
                index_hex_display=True,
                index_offset=4
            )
            self.play(Create(arr))
            self.wait(1)

Hide Indices
^^^^^^^^^^^^

Or if you don't want to show the indices at all, simply pass ``True`` as the ``hide_index`` argument to the constructor

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(
                self,
                [1, 2, 3, 4],
                hide_index=True
            )
            self.play(Create(arr))
            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(
                self,
                [1, 2, 3, 4],
                hide_index=True
            )
            self.play(Create(arr))
            self.wait(1)

Misc Functions
~~~~~~~~~~~~~~

The |MArray| provides some auxiliary methods which this secion will discuss.

Append Element
^^^^^^^^^^^^^^

For an existing array, you can also append an element simply by invoking the |MArray.append_elem| method.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3], label='Array', arr_label_pos=MArrayDirection.DOWN)
            self.add(arr)
            self.wait(1)
            arr.append_elem(4)
            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3], label='Array', arr_label_pos=MArrayDirection.DOWN)
            self.add(arr)
            self.wait(1)
            arr.append_elem(4)
            self.wait(1)

.. note::

    You can also pass ``mob_elem_*_args`` to this method to customize the inserted element.

Moreover, you can also specify the animation that is played for the inserted element via the ``append_anim`` argument. The code snippet below passes the |GrowFromCenter| animation to the |MArray.append_elem| method:

.. code-block:: python
    :linenos:

    arr.append_elem(4, append_anim=GrowFromCenter)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3], label='Array', arr_label_pos=MArrayDirection.DOWN)
            self.add(arr)
            self.wait(1)
            arr.append_elem(4, append_anim=GrowFromCenter)
            self.wait(1)

.. note::

    You can also specify arguments to the passed animation via the ``append_anim_args`` parameter and also set the target of the animation using the ``append_anim_target`` parameter that takes in |MArrayElementComp| enum.

Did you notice that in both snippets, we didn't pass any animation to our |Scene| but the append animation still played? This is thanks to the ``self`` that we pass as the first argument to our |MArray| constructor, which is basically a reference to the current |Scene|.

However, if you'd like to play the animation yourself, we have got you covered! The |MArrayElement| method returns a list of |Animation| that you can pass to the |Scene.play| method as follows:

.. code-block:: python
    :linenos:

    self.play(*arr.append_elem(4, play_anim=False))

Remove Element
^^^^^^^^^^^^^^

To remove an element simply invoke the |MArray.remove_elem| method with the index of element you wish to remove.

.. code-block:: python
    :linenos:

    arr.remove_elem(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3], label='Array', arr_label_pos=MArrayDirection.DOWN)
            self.add(arr)
            self.wait(1)
            arr.remove_elem(1)
            self.wait(1)

Similar to how you were able to pass the append animation to the |MArray.append_elem| function, you can specify two animations for the |MArray.remove_elem| method:

1. Element removal animation via the ``removal_anim`` parameter.
2. Indices update animation via the ``update_anim`` parameter.

The code snippet below provides an example:

.. code-block:: python
    :linenos:

    arr.remove_elem(1, removal_anim=ShowPassingFlash , update_anim=Write)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3], label='Array', arr_label_pos=MArrayDirection.DOWN)
            self.add(arr)
            self.wait(1)
            arr.remove_elem(1, removal_anim=ShowPassingFlash , update_anim=Write)
            self.wait(1)

.. note::

    You can also specify arguments to the passed animation via the ``*_anim_args`` parameter and also set the target of the animation using the ``*_anim_target`` parameter.

Lastly, as the |MArray.append_elem| returns a list of |Animation|, the |MArray.remove_elem| returns two objects; a removal animation and a function that udpates the indices of the remaining elements and returns their animations. Hence, you can animate this as follows:

.. code-block:: python
    :linenos:

    (remove_anim, update_indices) = arr.remove_elem(1, removal_anim=ShowPassingFlash , update_anim=Write, play_anim=False)
    self.play(remove_anim) # Play removal animation first
    self.play(*update_indices(play_anim=False)) # Then play the update_indices animation

Swap Element
^^^^^^^^^^^^

To implement many of the sorting algorithms, you can leverage the |MArray.swap_elems| method as shown below:

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3, 4, 5])
            arr.center()
            self.add(arr)
            arr.swap_elems(1, 3)
            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3, 4, 5])
            arr.center()
            self.add(arr)
            arr.swap_elems(1, 3)
            self.wait(1)

Additionally, if you want the swap animation to depict swapping of the element body, you can simply do so by passing true as the third argument to the method:

.. code-block:: python
    :linenos:

    arr.swap_elems(1, 3, True)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3, 4, 5])
            arr.center()
            self.add(arr)
            arr.swap_elems(1, 3, True)
            self.wait(1)

Update Element
^^^^^^^^^^^^^^

You can also update the value and the index of an existing array using the |MArray.update_elem_value| and |MArray.update_elem_index| methods respectively.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3])
            self.add(arr)
            self.wait(1)
            arr.update_elem_value(1, 20)
            arr.update_elem_index(1, -2)
            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3])
            self.add(arr)
            self.wait(1)
            arr.update_elem_value(1, 20)
            arr.update_elem_index(1, -2)
            self.wait(1)

.. note::

    You can also pass ``mob_elem_value_args`` and ``mob_elem_index_args`` to respective methods to customize the updated element mobject.

Using MArrayPointer
~~~~~~~~~~~~~~~~~~~

Thus far, if you had been hoping for a pointer to associate with your array, then your prayers have been answered. The |MArrayPointer| allows you to attach a pointer with your array. The following snippet demonstrates its capabilities:

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3, 4, 5], label='Array')
            arr.shift(UP + LEFT * 2)
            self.add(arr)

            pointer = MArrayPointer(self, arr, 2, 'P')
            self.play(Create(pointer))
            self.wait(1)
            pointer.shift_to_elem(4)
            self.wait(1)
            pointer.shift_to_elem(0)
            self.wait(1)
            pointer.attach_to_elem(2)

            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3, 4, 5], label='Array')
            arr.shift(UP + LEFT * 2)
            self.add(arr)

            pointer = MArrayPointer(self, arr, 2, 'P')
            self.play(Create(pointer))
            self.wait(1)
            pointer.shift_to_elem(4)
            self.wait(1)
            pointer.shift_to_elem(0)
            self.wait(1)
            pointer.attach_to_elem(2)

            self.wait(1)

Using MArraySlidingWindow
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to the |MArrayPointer|, we also have the |MArraySlidingWindow| that allows you to attach a sliding window with your array. The following snippet demonstrates its capabilities:

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3, 4, 5], label='Array')
            arr.shift(UP + LEFT * 2)
            self.add(arr)

            window = MArraySlidingWindow(self, arr, 1, 1, 'W')
            self.play(Create(window))
            self.wait(1)
            window.shift_to_elem(2)
            self.wait(1)
            window.resize_window(3)
            self.wait(1)
            window.shift_to_elem(0)
            self.wait(1)
            window.resize_window(1)
            self.wait(1)
            window.attach_to_elem(2)

            self.wait(1)

.. raw:: html

    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low

    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3, 4, 5], label='Array')
            arr.shift(UP + LEFT * 2)
            self.add(arr)

            window = MArraySlidingWindow(self, arr, 1, 1, 'W')
            self.play(Create(window))
            self.wait(1)
            window.shift_to_elem(2)
            self.wait(1)
            window.resize_window(3)
            self.wait(1)
            window.shift_to_elem(0)
            self.wait(1)
            window.resize_window(1)
            self.wait(1)
            window.attach_to_elem(2)

            self.wait(1)

With this we conclude this guide. We hope you found it useful! ✌️
