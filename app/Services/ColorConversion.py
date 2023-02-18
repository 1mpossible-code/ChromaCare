"""
This module provides a service to convert hex and rdga color codes.

"""

class ColorConversion:
    """
    ColorConversion coverts hex and rgba codes.
    """
    @staticmethod
    def hex_to_rgb(hex_code):
        """
        Converts hex to rgb
        :param string hex_code: hex code of color as string
        :return: returns rgb code as a tuple
        """
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))

    @staticmethod
    def hex_to_rgba(hex_code, alpha):
        """
        Converts hex to rgba
        :param string hex_code: hex color code as string
        :param float alpha: a value of rgba as float
        :return: returns rgba code as a tuple
        """
        hex_code = hex_code.lstrip('#')
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4)) + (alpha,)

    @staticmethod
    def rgba_to_rgb(rgba_code):
        """
        Converts rgba to rgb.
        :param string rgba_code: the rgba color code as string
        :return: a tuple representing the rgb color values
        """
        rgba_values = rgba_code[5:-1]
        r, g, b, _ = [int(value) for value in rgba_values.split(',')]
        return (r, g, b)
