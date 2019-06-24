from collections.abc import Sequence


class Point(Sequence):
    def __init__(self, longitude: float, latitude: float):
        """
        :param latitude: Y axis
        :param longitude: X axis
        """
        self.latitude = latitude
        self.longitude = longitude

    def __len__(self) -> int:
        return 2

    def __getitem__(self, item: float) -> float:
        if item in [0, 'x']:
            return self.longitude
        elif item in [1, 'y']:
            return self.latitude
        else:
            raise IndexError('Point has indexes only for longitude (0 and "x") and latitude (1 and "y")')
