from manim import *
import sys
sys.path.append('../src/')
from manim_data_structures import *


class MyScene(Scene):
    def construct(self):
        arr = MArray(self, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        arr.shift(LEFT * 4 + UP * 2)
        tar_val = MVariable(self, 3, label="target value")
        tar_val.shift(DOWN * 2)
        l = MArrayPointer(self, arr, 0, label="left")
        r = MArrayPointer(self, arr, 9, label="right")

        self.play(Create(arr))
        self.play(Create(tar_val))
        self.play(Create(l))
        self.play(Create(r))

        mid = MArrayPointer(self, arr, (l + r) // 2, label="mid")
        self.play(Create(mid))

        # find first larger or equal to target value
        while (l <= r):
            anims = []
            if (tar_val > mid):
                anims.append(l.shift_to_elem(mid + 1, play_anim=False))
            else:
                anims.append(r.shift_to_elem(mid - 1, play_anim=False))
            anims.append(mid.shift_to_elem((l + r) // 2, play_anim=False))
            self.play(AnimationGroup(*anims))
            self.wait(1)
            
