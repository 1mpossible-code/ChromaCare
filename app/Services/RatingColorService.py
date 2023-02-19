class RatingColorService:
    @staticmethod
    def rate(rgb):
        """
        Rates how suitable a color is for red-green color-blind people, on a scale of 1 to 10.

        Parameters:
            rgb (tuple[int, int, int]): A tuple of three integers (r, g, b) representing the red, green, and blue values
                of the color, respectively. Each value should be between 0 and 255.

        Returns:
            int: A rating from 1 to 10 indicating how suitable the color is for red-green color-blind people.
                 A rating of 1 indicates that the color is very difficult for people with red-green color blindness
                 to distinguish from other colors, while a rating of 10 indicates that the color is easy to
                 distinguish for these individuals.
        """
        r, g, b = rgb
        # Calculate the color contrast between red and green, as perceived by red-green color-blind people
        if r + g + b == 0:
            return 10
        contrast = abs(r - g) / (r + g + b)
        # Rate the color on a scale of 1 to 10, based on its contrast between red and green
        if contrast < 0.05:
            return 10
        elif contrast < 0.1:
            return 9
        elif contrast < 0.2:
            return 8
        elif contrast < 0.3:
            return 7
        elif contrast < 0.4:
            return 6
        elif contrast < 0.5:
            return 5
        elif contrast < 0.6:
            return 4
        elif contrast < 0.7:
            return 3
        elif contrast < 0.8:
            return 2
        else:
            return 1
