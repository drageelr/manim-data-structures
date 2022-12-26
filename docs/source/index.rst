.. Manim Data Structures documentation master file, created by
   sphinx-quickstart on Fri Nov 25 19:14:42 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Manim Data Structures
=====================

A plugin for Manim Community Edition that provides Manim objects for common data structures.

Installation
------------

Simply execute the following command to install the package:

.. code-block:: console

   $ pip install manim-data-structures

Usage
-----

To import the package in your script, add the following import statement:

.. code-block:: python

   from manim_data_structures import *

Variables
~~~~~~~~~

.. manim:: VarScene
    :save_last_frame:

    from manim_data_structures import *

    class VarScene(Scene):
        def construct(self):
            var = MVariable(self, 10, 0, 'Var')
            self.add(var)

Arrays
~~~~~~

.. manim:: ArrayScene
    :save_last_frame:

    from manim_data_structures import *

    class ArrayScene(Scene):
        def construct(self):
            arr = MArray(self, [1, 2, 3], label='Arr')
            self.add(arr)

Next Steps
----------

- Visit the :doc:`guides/index` section to learn how to use the library.
- Also check out the :doc:`reference/index` to view detailed documentation of the classes.


Index
-----

.. toctree::
   :maxdepth: 2

   example
   guides/index
   reference/index
