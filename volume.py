#!/usr/bin/python
"Volume calculator for approx spherical volumes on ct and MRI"
width = float(input("Width: "))
length = float(input("Length: "))
height_a = float(input("First Section: "))
height_b = float(input("Last Section: "))
height = abs(height_a - height_b)

volume = (width * height * length)/2.0

print("Volume: {} mL".format(volume))

