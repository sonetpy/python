import math

def area_of_shape(shape_fn, width, height):
  """Calculates the area of a shape based on a provided function."""
  return shape_fn(width, height)

def square_area(width, height):
  return width * height

def triangle_area(width, height):
  return 0.5 * width * height

# Calculate area of a square
square_area = area_of_shape(square_area, 5, 5)
print(f"Area of square: {square_area}")

# Calculate area of a triangle
triangle_area = area_of_shape(triangle_area, 6, 4)
print(f"Area of triangle: {triangle_area}")