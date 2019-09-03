#!/usr/bin/python
"""
MRI/CT ICH Volume Calculator
------------------------
for approx spherical volumes on CT and MRI

References:
    1. Kothari RU, Brott T, Broderick JP, Barsan WG, Sauerbeck LR, Zuccarello M, et al. The ABCs of measuring intracerebral hemorrhage volumes. Stroke. 1996 Aug;27(8):1304–5. 
"""

A  = float(input("A: Max Diameter (cm): "))
B = float(input("B: Diameter Perp A (cm): "))
C1 = float(input("C1: First Section (cm): "))
C2 = float(input("C2: Last Section (cm): "))
C = abs(C1 - C2)

volume = (A * B * C)/2.0

print("Volume: {} mL".format(volume))

