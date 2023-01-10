.. include:: ./refsub.rst

Example Gallery
===============

Bubble Sort Using MArray
------------------------

The code snippet below sorts the array ``[8, 11, 2, 10, 5, 9, 3]`` using the bubble sort algorithm.

.. manim:: BubbleSortExample
    :quality: low

    from manim_data_structures import *

    class BubbleSortExample(Scene):
        def bubbleSort(self, arr: MArray):
            val_arr = arr.fetch_arr()
            n = len(val_arr)

            for i in range(n):

                for j in range(0, n-i-1):

                    if val_arr[j] > val_arr[j+1]:
                        self.play(
                            arr.animate_elem_body(j).set(fill_color=RED_D),
                            arr.animate_elem_body(j+1).set(fill_color=RED_D)
                        )
                        arr.swap_elems(j, j+1, True)
                        self.play(
                            arr.animate_elem_body(j).set(fill_color=BLUE_D),
                            arr.animate_elem_body(j+1).set(fill_color=BLUE_D)
                        )
                    else:
                        self.play(
                            arr.animate_elem_body(j).set(fill_color=GREEN_D),
                            arr.animate_elem_body(j+1).set(fill_color=GREEN_D)
                        )
                        self.play(
                            arr.animate_elem_body(j).set(fill_color=BLUE_D),
                            arr.animate_elem_body(j+1).set(fill_color=BLUE_D)
                        )
                        pass

        def construct(self):
            arr = MArray(self, [8, 11, 2, 10, 5, 9, 3], label='Array')
            arr.center()
            self.add(arr)
            self.bubbleSort(arr)
            self.wait(1)

Find Pair Sum in Sorted MArray
------------------------------

The code snippet below uses the famous two pointer technique to find the pair sum ``17`` in the sorted array ``[2, 3, 5, 8, 9, 10, 11]``.

.. manim:: PairSumExample
    :quality: low

    from manim_data_structures import *

    class PairSumExample(Scene):
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
                    self.play(pair_sum.fetch_mob_body().animate.set(fill_color=GREEN))
                    return True
                elif(pair_sum.fetch_value() < val):
                    p_i.shift_to_elem(p_i.fetch_index() + 1)
                else:
                    p_j.shift_to_elem(p_j.fetch_index() - 1)

            self.play(pair_sum.fetch_mob_body().aniamte.set(fill_color=RED))
            return False

        def construct(self):
            arr = MArray(self, [2, 3, 5, 8, 9, 10, 11], label='Array')
            arr.center()
            arr.shift(UP)
            self.add(arr)
            self.isPairSumAnim(arr, 7, 17)
            self.wait(1)

Maxmimum Sum of K Consecutive Integers in MArray
------------------------------------------------

The code snippet below uses the sliding window technique to find the maximum sum of ``k = 4`` consecutive elements in the array ``[1, 4, 2, 10, 2, 3, 1, 0, 20]``

.. manim:: KMaxSumExample
    :quality: low

    from manim_data_structures import *

    class KMaxSumExample(Scene):
        def maxSumAnim(self, marr: MArray, k):
            arr = marr.fetch_arr()
            n = len(arr)

            window = MArraySlidingWindow(self, marr, 0, k, 'Window')
            var_window_sum = MVariable(self, sum(arr[:k]), label='Window Sum')
            var_max_sum = MVariable(self, var_window_sum.fetch_value(), label='Max Sum')
            var_window_sum.shift(DOWN)
            var_max_sum.shift(DOWN * 2.5)

            self.play(Create(window))
            self.play(Create(var_window_sum), Create(var_max_sum))

            for i in range(n - k):
                window.shift_to_elem(i + 1)
                var_window_sum.update_value(var_window_sum.fetch_value() - arr[i] + arr[i + k])
                if var_window_sum.fetch_value() > var_max_sum.fetch_value():
                    var_max_sum.update_value(var_window_sum.fetch_value())


            self.play(var_max_sum.fetch_mob_body().animate.set(fill_color=GREEN))
            return var_max_sum.fetch_value()

        def construct(self):
            arr = MArray(self, [1, 4, 2, 10, 2, 3, 1, 0, 20], label='Array')
            arr.center()
            arr.shift(UP * 1.5)
            self.add(arr)
            self.maxSumAnim(arr, 4)
            self.wait(1)
