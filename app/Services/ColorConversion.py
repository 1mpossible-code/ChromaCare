"""
This module provides a service to convert hex and rdga color codes.

"""


class ColorConversion:
    """
    ColorConversion coverts hex and rgba codes.
    """

    @staticmethod
    def convert(color):
        """
        Converts color code (hex, rgba, rgb) to rgb
        :param color: color code (hex, rgba, rgb)
        :type color: str
        :return: rgb code as tuple
        """
        rgb_tuple = None

        if color.startswith("#"):
            # Convert hex to rgb
            hex_value = color.lstrip("#")
            if len(hex_value) == 3:
                hex_value = "".join([x * 2 for x in hex_value])
            rgb_tuple = tuple(int(hex_value[i:i + 2], 16) for i in (0, 2, 4))
        elif color.startswith("rgba"):
            # Convert rgba to rgb
            rgba_list = color[5:-1].split(",")
            rgba_tuple = tuple(map(float, rgba_list))

            r, g, b, a = rgba_tuple
            r = int((1 - a) * 255 + a * r)
            g = int((1 - a) * 255 + a * g)
            b = int((1 - a) * 255 + a * b)
            rgb_tuple = (r, g, b)
        elif color.startswith("rgb"):
            # Convert rgb to tuple
            rgb_list = color[4:-1].split(",")
            rgb_tuple = tuple(map(int, rgb_list))

        return rgb_tuple
