class Point:
  definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
  
  def __init__(self, x: float=0, y: float=0):
    self.x = x
    self.y = y

  def move(self, new_x: float, new_y: float):
    self.x = new_x
    self.y = new_y

  def reset(self):
    self.x = 0
    self.y = 0

  def compute_distance(self, point: "Point")-> float:
    distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
    return distance

first_point = Point(x=1, y=1)
second_point = Point(x=2, y=2)

print(first_point.compute_distance(second_point))

class Line:
    def __init__(self, startp: "Point", endp: "Point"):
        self.startp = startp
        self.endp = endp

    def compute_length(self) -> float:
        return self.startp.compute_distance(self.endp)
    
    def compute_slope(self) -> float:
        if self.startp.x == self.endp.x:
            return "undefined"
        else:
            return (self.endp.y - self.startp.y) / (self.endp.x - self.startp.x)
    
    def compute_horizontal_cross(self, y: float) -> "Point":
        if self.startp.y == self.endp.y:
            return None
        else:
            slope = self.compute_slope()
            x = (y - self.startp.y) / slope + self.startp.x
            return Point(x, y)
        
    def compute_vertical_cross(self, x: float) -> "Point":
        if self.startp.x == self.endp.x:
            return None
        else:
            slope = self.compute_slope()
            y = slope * (x - self.startp.x) + self.startp.y
            return Point(x, y)
        
line = Line(startp=(0,1), endp=(1,0))
        
class Rectangle:
    def __init__(self, method: str, *args):
        
        if method == "bottom_left":
            bottom_left, width, height = args

            self.width = width
            self.height = height
            self.b_left = bottom_left
            self.t_right = Point(self.b_left.x + width, self.b_left.y + height)
            self.center = Point(self.b_left.x + (width / 2), self.b_left.y + (height / 2))

        elif method == "center":
            center, width, height = args

            self.width = width
            self.height = height
            self.center = center
            self.b_left = Point(self.center.x - (width / 2), self.center.y - (height / 2))
            self.t_right = Point(self.b_left.x + width, self.b_left.y + height)

        elif method == "corners":
            bottom_left, upper_right = args
            
            self.b_left = bottom_left
            self.t_right = upper_right
            self.width = self.t_right.x - self.b_left.x
            self.height = self.t_right.y - self.b_left.y
            self.center = Point(self.b_left.x + (self.width / 2), self.b_left.y + (self.height / 2))

        elif method == "4_lines":
            line1, line2, line3, line4 = args
            self.b_left = line1.startp
            self.t_right = line3.endp
            self.width = line1.compute_length()
            self.height = line2.compute_length()
            self.center = Point(self.b_left.x + (self.width / 2), self.b_left.y + (self.height / 2))
            if line1.compute_slope() != line3.compute_slope():
                raise ValueError("Lines do not form a rectangle.")
            if line2.compute_slope() != line4.compute_slope():
                raise ValueError("Lines do not form a rectangle.")
        else:
            raise ValueError("Invalid method. Use 'bottom_left', 'center', 'corners' or '4_lines'.")

    def compute_area(self) -> float:
        return self.width * self.height

    def compute_perimeter(self) -> float:
        return (self.width * 2) + (self.height * 2)

    def compute_interference_point(self, point: "Point") -> bool:
        val_x: bool = self.b_left.x <= point.x <= self.t_right.x
        val_y: bool = self.b_left.y <= point.y <= self.t_right.y
        return val_x and val_y
        if val_x and val_y:
            return True
        else:
            return False
    
rectangle_1 = Rectangle("bottom_left", Point(0, 0), 2, 3)
rectangle_2 = Rectangle("center", Point(1, 1), 2, 3)
rectangle_3 = Rectangle("corners", Point(0, 0), Point(2, 3))
rectangle_4 = Rectangle("4_lines", Line(Point(0, 0), Point(2, 0)), Line(Point(2, 0), Point(2, 3)), Line(Point(2, 3), Point(0, 3)), Line(Point(0, 3), Point(0, 0)))

print(rectangle_1.compute_area())
print(rectangle_2.compute_area())
print(rectangle_3.compute_area())
print(rectangle_4.compute_area())

print(rectangle_1.compute_perimeter())
print(rectangle_2.compute_perimeter())
print(rectangle_3.compute_perimeter())
print(rectangle_4.compute_perimeter())


    
class Square(Rectangle):
    def __init__(self, side:float, bottom_left: "Point"):
        super().__init__(side, side, bottom_left)


      

