from manim import *

class MArrayElement(VGroup):
    def __init_props(self):
        self.__mob_square_props = {
            'color': BLUE_B,
            'fill_color': BLUE_D,
            'fill_opacity': 1,
            'side_length': 1
        }
        self.__mob_value_props = {
            'text': '',
            'color': WHITE,
            'weight': BOLD
        }
        self.__mob_index_props = {
            'text': '',
            'color': BLUE_D,
            'font_size': 32
        }

    def __update_props(self, mob_square_args = {}, mob_value_args = {}, mob_index_args = {}):
        self.__mob_square_props.update(mob_square_args)
        self.__mob_value_props.update(mob_value_args)
        self.__mob_index_props.update(mob_index_args)

        if type(self.__mob_value_props['text']) != str:
            self.__mob_value_props['text'] = str(self.__mob_value_props['text'])

        if type(self.__mob_index_props['text']) != str:
            self.__mob_index_props['text'] = str(self.__mob_index_props['text'])
        
    def __init_mobs(self, init_square = False, init_value = False, init_index = False):
        if init_square:
            self.__mob_square = Square(**self.__mob_square_props)
            self.add(self.__mob_square)
        
        if init_value:
            self.__mob_value = Text(**self.__mob_value_props)
            self.__mob_value.next_to(self.__mob_square, np.array([0, 0, 0]), 0)
            self.add(self.__mob_value)

        if init_index:
            self.__mob_index = Text(**self.__mob_index_props)
            self.__mob_index.next_to(self.__mob_square, UP, 0.25)
            self.add(self.__mob_index)

    def __init__(self, mob_square_args = {}, mob_value_args = {}, mob_index_args = {}, **kwargs):
        super().__init__(**kwargs)
        
        # Initialize props
        self.__init_props()
        
        # Update props
        self.__update_props(mob_square_args, mob_value_args, mob_index_args)
        
        # Initialize mobjects
        self.__init_mobs(True, True, True)

    def fetch_mob_square(self):
        return self.__mob_square

    def fetch_mob_text(self):
        return self.__mob_value

    def fetch_mob_index(self):
        return self.__mob_index

    def update_mob_value(self, mob_value_args = {}):
        self.__update_props(mob_value_args=mob_value_args)
        self.remove(self.__mob_value)
        self.__init_mobs(init_value=True)
        self.add(self.__mob_value)
        return self.__mob_value

    def update_mob_index(self, mob_index_args = {}):
        self.__update_props(mob_index_args=mob_index_args)
        self.remove(self.__mob_index)
        self.__init_mobs(init_index=True)
        self.add(self.__mob_index)
        return self.__mob_index

    def animate_mob_square(self):
        return self.__mob_square.animate

    def animate_mob_text(self):
        return self.__mob_value.animate

    def animate_mob_index(self):
        return self.__mob_index.animate

class MArray(VGroup):
    def __calc_index(self, index):
        return self.__index_start + self.__index_offset * index if self.__index_hex_display == False else hex(self.__index_start + self.__index_offset * index)

    def __append_elem(self, value, mob_square_args = {}, mob_value_args = {}, mob_index_args = {}):
        mob_value_args['text'] = value
        mob_index_args['text'] = self.__calc_index(len(self.__mob_arr))
        self.__mob_arr.append(MArrayElement(
            mob_square_args=mob_square_args,
            mob_value_args=mob_value_args,
            mob_index_args=mob_index_args
        ))
        if len(self.__mob_arr) > 1:
            self.__mob_arr[-1].next_to(self.__mob_arr[-2], RIGHT, 0)
        self.add(self.__mob_arr[-1])
        
    def __init__(self, arr = [], index_offset = 1, index_start = 0, index_hex_display = False, mob_square_args = {}, mob_value_args = {}, mob_index_args = {}, **kwargs):
        super().__init__(**kwargs)
        self.__arr = arr
        self.__mob_arr = []
        self.__index_offset = index_offset
        self.__index_start = index_start
        self.__index_hex_display = index_hex_display

        for v in arr:
            self.__append_elem(v, mob_square_args, mob_value_args, mob_index_args)

    def update_elem_value(self, index, value, mob_value_args = {}):
        if index < 0 or index > len(self.__mob_arr):
            raise Exception('Index out of bounds!')

        self.__arr[index] = value
        mob_value_args['text'] = value
        return self.__mob_arr[index].update_mob_value(mob_value_args)

    def update_elem_index(self, index, value, mob_index_args = {}):
        if index < 0 or index > len(self.__mob_arr):
            raise Exception('Index out of bounds!')

        mob_index_args['text'] = value
        return self.__mob_arr[index].update_mob_index(mob_index_args)

    def animate_elem(self, index):
        if index < 0 or index > len(self.__mob_arr):
            raise Exception('Index out of bounds!')

        return self.__mob_arr[index].animate

    def animate_elem_square(self, index):
        if index < 0 or index > len(self.__mob_arr):
            raise Exception('Index out of bounds!')

        return self.__mob_arr[index].animate_mob_square()

    def animate_elem_value(self, index):
        if index < 0 or index > len(self.__mob_arr):
            raise Exception('Index out of bounds!')

        return self.__mob_arr[index].animate_mob_text()

    def animate_elem_index(self, index):
        if index < 0 or index > len(self.__mob_arr):
            raise Exception('Index out of bounds!')

        return self.__mob_arr[index].animate_mob_index()

    def append_elem(self, value, mob_square_args = {}, mob_value_args = {}, mob_index_args = {}):
        self.__arr.append(value)
        self.__append_elem(value, mob_square_args, mob_value_args, mob_index_args)
        return self.__mob_arr[-1]

    def fetch_arr(self):
        return self.__arr

    def fetch_mob_arr(self):
        return self.__mob_arr