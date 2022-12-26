Example Gallery
===============

.. currentmodule:: manim_data_structures.m_array

Find Pair Sum In Sorted MArray
------------------------------

The code snippet below uses the famous two pointer technique to find the pair sum ``17`` in the sorted array ``[2, 3, 5, 8, 9, 10, 11]``.

.. manim:: MainScene
    :quality: low

    from manim_data_structures import *

    class MainScene(Scene):
        def isPairSumAnim(self, arr, n, val):
            p_i = MArrayPointer(self, arr, 0, 'i', mob_arrow_args={'color': GREEN}, mob_label_args={'color': GREEN})
            p_j = MArrayPointer(self, arr, n - 1, 'j', mob_arrow_args={'color': YELLOW}, mob_label_args={'color': YELLOW})
            pair_sum = MVariable(self, 0, label='Sum')
            pair_sum.shift(DOWN * 2)

            self.play(Create(pair_sum))
            self.play(Create(p_i), Create(p_j))

            while (p_i.fetch_index() < p_j.fetch_index()):
                pair_sum.update_value(arr.fetch_arr()[p_i.fetch_index()] + arr.fetch_arr()[p_j.fetch_index()])

                if (pair_sum.fetch_value() == val):
                    pair_sum.fetch_mob_square().set(fill_color=GREEN)
                    return True
                elif(pair_sum.fetch_value() < val):
                    p_i.shift_to_elem(p_i.fetch_index() + 1)
                else:
                    p_j.shift_to_elem(p_j.fetch_index() - 1)

            pair_sum.fetch_mob_square().set(fill_color=RED)
            return False

        def construct(self):
            arr = MArray(self, [2, 3, 5, 8, 9, 10, 11], label='Array')
            arr.shift(UP + LEFT * 2)
            self.add(arr)
            self.isPairSumAnim(arr, 7, 17)
            self.wait(1)
