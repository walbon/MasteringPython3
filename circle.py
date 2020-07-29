import math
class Circle(object):
    def __init__(self,radius=1):
        self._radius = radius
        self._diameter = radius*2
        self._area = math.pi*(radius**2)

    def __repr__(self):
        return f"Circle({self._radius})"

    def get_radius(self):
        return self._radius

    def set_radius(self,value):
        if isinstance(value,int):
            if not value > 0:
                raise ValueError("Radius cannot be negative")
            else:
                self._radius = value
                self._diameter = value*2
                self._area = math.pi*(value**2)
        else:
            raise ValueError("shiiii")
    radius = property(get_radius,set_radius)

    def get_diameter(self):
        return self._diameter
    def set_diameter(self,value):
        if isinstance(value,int):
            if not value > 0:
                raise ValueError("Diameter cannot be negative")
            else:
                self._radius = value/2
                self._diameter = value
                self._area = math.pi*((value/2)**2)
        else:
            raise ValueError("can't set attribute")
    diameter = property(get_diameter,set_diameter)

    def get_area(self):
        return self._area
    area = property(get_area)
