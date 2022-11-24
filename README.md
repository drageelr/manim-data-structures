# Manim Data Structures
A plugin that contains common data structures to create Manimations.

## Installation
To install, simply run the following command:
```
pip install manim-data-structures
```

## Importing
Simply use the following line of code to import the package:
```python
from manim_data_structures import *
```

## Usage
### Code
```python
class MainScene(Scene):
    def construct(self):
        # Create an array
        arr = MArray([8, 7, 6, 5, 4])
        self.play(Create(arr))

        # Animate array
        self.play(arr.animate.shift(UP * 2.5 + LEFT * 5))

        # Animate array element
        self.play(arr.animate_elem(3).shift(DOWN * 0.5))

        # Animate array element mobjects
        self.play(arr.animate_elem_square(0).set_fill(BLACK), arr.animate_elem_value(0).rotate(PI / 2).set_fill(RED), arr.animate_elem_index(0).rotate(PI / 2))

        # Display array with hex values
        arr2 = MArray([0, 2, 4, 6, 8], index_hex_display=True, index_offset=4)
        self.play(Create(arr2))
        self.play(arr2.animate.shift(DOWN * 2.5 + LEFT * 5))

        # Create customized array
        arr3 = MArray([1, 1, 2], mob_square_args={'color': GRAY_A, 'fill_color': RED_E, 'side_length': 0.5}, mob_value_args={'color': GOLD_A, 'font_size': 28}, mob_index_args={'color': RED_E, 'font_size': 22})
        self.play(Create(arr3))

        # Append element
        self.play(Write(arr2.append_elem(10)))

        # Append customized element
        self.play(Write(arr2.append_elem(12, mob_square_args={'fill_color': BLACK})))

        # Update value of element
        self.play(Write(arr2.update_elem_value(3, 0, mob_value_args={'color': RED})), arr2.animate_elem_square(3).set_fill(WHITE))

        self.wait()
```

### Output


https://user-images.githubusercontent.com/56049229/203757924-6f3aed6d-e870-468f-a269-a572350355b1.mp4

