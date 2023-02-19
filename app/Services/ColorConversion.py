"""
This module provides a service to convert hex and rdga color codes.

"""

class ColorConversion:
    """
    ColorConversion converts hex and rgba codes.
    """

    @staticmethod
    def convert(color):
        """
        Converts color code (hex,rgba) to rgb
        :param color: color code (hex, rgba)
        :type color: str
        :return: rgb code as tuple
        """
        rgb_tuple = None
    
        if color.startswith("#"):
            # Convert hex to rgb
            hex_value = color.lstrip("#")
            if len(hex_value) == 3:
                hex_value = "".join([c * 2 for c in hex_value])
            rgb_tuple = tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))
        elif color.startswith("rgba"):
            # Convert rgba to rgb
            rgba_list = color[5:-1].split(",")
            rgba_tuple = tuple(map(int, rgba_list))
            
            r, g, b, a = rgba_tuple
            r = int((1 - a) * 255 + a * r)
            g = int((1 - a) * 255 + a * g)
            b = int((1 - a) * 255 + a * b)
            rgb_tuple = (r, g, b)
        
        return rgb_tuple

converter = ColorConversion()

print(converter.convert("#eee"))
