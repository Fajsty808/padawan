
'''
Absolutely! It sounds like a fun and interactive way to learn. Here’s a simple task for you:

### Task:

Create a Python class named `Rectangle` with the following specifications:

1. **Attributes:**
   - `length` (float)
   - `width` (float)

2. **Methods:**
   - A constructor (`__init__`) that initializes the `length` and `width` with the values provided.
   - A method `area` that returns the area of the rectangle (Area = length * width).
   - A method `perimeter` that returns the perimeter of the rectangle (Perimeter = 2 * (length + width)).
   - A method `is_square` that returns `True` if the rectangle is a square (length == width), else returns `False`.

3. **Usage:**
   - After defining the class, create an instance of the `Rectangle` class with length `10` and width `20`.
   - Print the area, perimeter, and whether it is a square.

### Example of Expected Output:
```
Area: 200
Perimeter: 60
Is Square: False
```

Feel free to share your code once you’ve tried solving it, and I’ll be happy to review it for you!
'''
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def __str__(self):
        return f"\nRectangle attributes: \nlength: {self.length} \nwidth: {self.width}"
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return  2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width

rectangle = Rectangle(10,20) 

print('Area of rectangle is: ', rectangle.area())
print(rectangle.width)
print(rectangle.length)
print(rectangle)