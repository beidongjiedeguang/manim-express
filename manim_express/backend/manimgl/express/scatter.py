import numpy as np
from manimlib import *
from .coordinate_sys import SciAxes, SciAxes3D
from itertools import product
from sparrow.decorators.core import MetaSingleton


class Scatter:
    def __init__(self):
        self._color_choice_list = [
            GREEN_C, BLUE_C, RED_C, YELLOW_C, ORANGE, GOLD_C, MAROON_C, TEAL_C
        ]
        self.ax_width = FRAME_WIDTH - 2
        self.ax_height = FRAME_HEIGHT - 2

    @staticmethod
    def get_min_max(a: np.ndarray, a_range):
        if a_range is None:
            amin, amax = a.min(), a.max()
        else:
            amin, amax = a_range
        a_shift = (amax - amin) / 7
        amin -= a_shift
        amax += a_shift
        return amin, amax

    def from_dotcloud(self, x: np.ndarray, y: np.ndarray, size=0.05, color=BLUE,
                      x_range=None, y_range=None,
                      ax=None, ax_width=None, ax_height=None):

        if ax_width is None:
            ax_width = self.ax_width
        if ax_height is None:
            ax_height = self.ax_height

        assert len(x) == len(y)
        x, y = np.array(x), np.array(y)

        x_range = self.get_min_max(x, x_range)
        y_range = self.get_min_max(y, y_range)
        if ax is None:
            ax = SciAxes(x_range=x_range, y_range=y_range, width=ax_width, height=ax_height)
        points = [ax.c2p(i, j) for i, j in zip(x, y)]
        image_obj = DotCloud(points, radius=size, opacity=0.8).set_color(color)  # .set_color_by_rgba_func(rgba_func)
        image_obj.flip(RIGHT).move_to(ORIGIN)
        return ax, image_obj

    def from_dot_cloud_3d(self, x: np.ndarray, y: np.ndarray, z: np.ndarray,
                          size=0.05, color=BLUE,
                          x_range=None, y_range=None, z_range=None,
                          ax=None, ax_width=None, ax_height=None):
        if ax_width is None:
            ax_width = self.ax_width
        if ax_height is None:
            ax_height = self.ax_height

        assert len(x) == len(y)
        assert len(x) == len(z)
        x, y, z = np.array(x), np.array(y), np.array(z)
        x_range = self.get_min_max(x, x_range)
        y_range = self.get_min_max(y, y_range)
        z_range = self.get_min_max(z, z_range)
        if ax is None:
            ax = ThreeDAxes(x_range=x_range, y_range=y_range, z_range=z_range,
                            width=ax_width, height=ax_height)
            labels = VGroup(
                ax.get_x_axis_label("x"),
                ax.get_y_axis_label("y"),
                ax.get_axis_label("z", ax.get_z_axis(),
                                  edge=OUT,
                                  direction=DOWN).rotate(90 * DEGREES, RIGHT),
            )
            ax.add(labels)
        points = [ax.c2p(i, j, k) for i, j, k in zip(x, y, z)]
        scatters = DotCloud(points, radius=size).set_color(color)
        return ax, scatters

    def from_vobj(self):
        pass


def image_arr_obj(arr, style=0, scale_factor=None):
    """
    ??????DotCloud (shader???????????????) ????????????, ???????????????????????????, ???????????????????????????
    """

    def rgb2gray(R, G, B):
        return 0.2989 * R + 0.5870 * G + 0.1140 * B

    row, col = arr.shape[:2]
    if scale_factor is None:
        scale_factor = max(6 / min(row, col), 0.007)
    xy = np.array(list(product(np.arange(col), np.arange(row))))

    if len(arr[0, 0]) >= 3 and style == 0:
        points = [(*i * scale_factor, 2 * rgb2gray(*arr[i[0], i[1]][:3])) for i in xy]
    else:
        points = [(*i * scale_factor, 0) for i in xy]

    color_dim = len(arr[0, 0])

    def rgba_func(point):
        """??????set_color_by_rgba_func??????????????????point??????, ?????????
        ??????DotCloud???????????????????????????????????????, ?????????????????????index???????????????, ?????????????????????????????????????????????????????????,
         ????????????????????????????????????????????????points??????????????????.
        ?????????????????????scale_factor?????????????????????.
        """
        x, y = round(point[0] / scale_factor), round(point[1] / scale_factor)
        if color_dim == 3:
            return [*arr[y, x], 1]
        else:  # dim=4
            return arr[y, x]

    image_obj = DotCloud(points, radius=scale_factor / 2).set_color_by_rgba_func(rgba_func)
    image_obj.flip(RIGHT).move_to(ORIGIN)
    return image_obj


def imobj_square(img: np.ndarray):
    """
    ????????????, ??????Square???img??????????????????????????????
    """
    height, width = img.shape[:2]
    if np.any(img > 1):
        img = img / 255
    pixel_array = VGroup(*[
        Square(fill_color=rgb_to_hex(img[i, j]), fill_opacity=1)
        for i in range(height)
        for j in range(width)
    ])
    pixel_array.arrange_in_grid(height, width, buff=0)
    pixel_array.set_height(6)
    pixel_array.set_stroke(WHITE, 0)
    return pixel_array
