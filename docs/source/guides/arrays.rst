Animating Arrays
================

.. currentmodule:: manim_data_structures.array

Manim Array - MArray
--------------------

The most basic data structure this package provides is the :py:class:`MArray` (short for Manim Array 😄). To create a :py:class:`MArray` simply create an instance by passing a python :py:class:`list`.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray([1, 2, 3])
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
            arr = MArray([1, 2, 3])
            self.play(Create(arr))
            self.wait(1)

Animating MArray
~~~~~~~~~~~~~~~~

To animate the :py:class:`MArray`, simply invoke the ``animate`` property as shown below:

.. code-block:: python
    
    self.play(arr.animate.shift(UP * 2 + LEFT * 5))

.. raw:: html
    
    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low
    
    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray([1, 2, 3])
            self.play(Create(arr))
            self.play(arr.animate.shift(UP * 2 + LEFT * 5))
            self.wait(1)

Moreover, you can also use the :py:func:`MArray.animate_elem` method to animate a single element of the :py:class:`MArray` as well:

.. code-block:: python

    self.play(arr.animate_elem(1).shift(DOWN))

.. raw:: html
    
    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low
    
    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray([1, 2, 3])
            self.play(Create(arr))
            self.play(arr.animate_elem(1).shift(DOWN))
            self.wait(1)

Lastly, you can also animate the body, value and the index of any element using the :py:func:`MArray.animate_elem_square`, :py:func:`MArray.animate_elem_value` and :py:func:`MArray.animate_elem_index` respectively.

.. code-block:: python

    self.play(
        arr.animate_elem_square(1).set_fill(BLACK),
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
            arr = MArray([1, 2, 3])
            self.play(Create(arr))
            self.play(
                arr.animate_elem_square(1).set_fill(BLACK),
                arr.animate_elem_value(1).set_fill(RED),
                arr.animate_elem_index(1).rotate(PI / 2)
            )
            self.wait(1)

Customizing MArray
~~~~~~~~~~~~~~~~~~

The :py:class:`MArray` also allows you to alter the way your array looks. While creating your array pass arguments to ``Square`` (used to represent the element body) and ``Text`` (used to represent the element value and index) mobjects.

.. code-block:: python

    arr = MArray(
        [1, 2, 3],
        mob_square_args={'fill_color': RED_D},
        mob_value_args={'color': BLACK},
        mob_index_args={'color': GOLD_A}
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
                [1, 2, 3],
                mob_square_args={'fill_color': RED_D},
                mob_value_args={'color': BLACK},
                mob_index_args={'color': GOLD_A}
            )
            self.play(Create(arr))
            self.wait(1)

Growth Direction
^^^^^^^^^^^^^^^^

Furthermore, you can also create :py:class:`MArray` that grows in different directions (e.g. up, down, right and left etc.).

.. currentmodule:: manim_data_structures.m_enum

To do this, simply pass your preferred direction enum from :py:class:`MArrayDirection` as the ``arr_dir`` argument to the constructor. The code snippet below generates four different arrays in each direction.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr_up = MArray([1, 2], arr_dir=MArrayDirection.UP)
            arr_right = MArray([3, 4], arr_dir=MArrayDirection.RIGHT)
            arr_down = MArray([5, 6], arr_dir=MArrayDirection.DOWN)
            arr_left = MArray([7, 8], arr_dir=MArrayDirection.LEFT)

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
            arr_up = MArray([1, 2], arr_dir=MArrayDirection.UP)
            arr_right = MArray([3, 4], arr_dir=MArrayDirection.RIGHT)
            arr_down = MArray([5, 6], arr_dir=MArrayDirection.DOWN)
            arr_left = MArray([7, 8], arr_dir=MArrayDirection.LEFT)

            self.play(Create(arr_up))
            self.play(arr_up.animate.shift(UP * 2))
            self.play(Create(arr_right))
            self.play(arr_right.animate.shift(RIGHT * 2))
            self.play(Create(arr_down))
            self.play(arr_down.animate.shift(DOWN * 2))
            self.play(Create(arr_left))
            self.play(arr_left.animate.shift(LEFT * 2))

            self.wait(1)

.. currentmodule:: manim_data_structures.array

Hex Indices
^^^^^^^^^^^

Lets say you want to show a 4-byte integer array with its addresses. You can simply achieve this by using ``index_hex_display`` and ``index_offset`` arguments of the :py:class:`MArray` constructor.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(
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
                [1, 2, 3, 4],
                index_hex_display=True,
                index_offset=4
            )
            self.play(Create(arr))
            self.wait(1)

Hide Indices
^^^^^^^^^^^^^^^

Or if you don't want to show the indices at all, simply pass ``True`` as the ``hide_index`` argument to the constructor

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray(
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
                [1, 2, 3, 4],
                hide_index=True
            )
            self.play(Create(arr))
            self.wait(1)

Misc Functions
~~~~~~~~~~~~~~

The :py:class:`MArray` provides some auxiliary methods which this secion will discuss.

Append Element
^^^^^^^^^^^^^^

For an existing array, you can also append an element simply by invoking the :py:func:`MArray.append_elem` method.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray([1, 2, 3])
            self.add(arr)
            self.wait(1)
            self.play(Write(arr.append_elem(4)))
            self.wait(1)

.. raw:: html
    
    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low
    
    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray([1, 2, 3])
            self.add(arr)
            self.wait(1)
            self.play(Write(arr.append_elem(4)))
            self.wait(1)

.. note::

    You can also pass ``mob_*_args`` to this method to customize the inserted element.

Update Element
^^^^^^^^^^^^^^

You can also update the value and the index of an existing array using the :py:class:`MArray.update_elem_value` and :py:class:`MArray.update_elem_index` methods respectively.

.. code-block:: python
    :linenos:

    class MyScene(Scene):
        def construct(self):
            arr = MArray([1, 2, 3])
            self.add(arr)
            self.wait(1)
            self.play(
                Write(arr.update_elem_value(1, 20)),
                Write(arr.update_elem_index(1, -2))
            )
            self.wait(1)

.. raw:: html
    
    <div>

.. manim:: MyScene
    :hide_source:
    :quality: low
    
    from manim_data_structures import *

    class MyScene(Scene):
        def construct(self):
            arr = MArray([1, 2, 3])
            self.add(arr)
            self.wait(1)
            self.play(
                Write(arr.update_elem_value(1, 20)),
                Write(arr.update_elem_index(1, -2))
            )
            self.wait(1)

.. note::

    You can also pass ``mob_value_args`` and ``mob_index_args`` to respective methods to customize the updated element mobject.

With this we conclude this guide. We hope you found it useful! ✌️