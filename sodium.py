#!/usr/bin/python
"""
Serum Sodium Correction Protocol
--------------------------------
Not for medical use.
Source: The Neuro ICU Book, Second Edition, 2018 McGraw-Hill, Lee Kiwon

"""

serum_Na = float(input("Serum Na (mmol/L): "))

if serum_Na < 145.0:
    print("No Hypernatremia")
    print("END")
    exit()

print("Hypernatremia")
print("-------------")
print(
"""
ECF Volume
----------
1) Increased
2) Decreased
3) Normal
""")

ecf_vol = input("ECF Volume: ")
print("")

if ecf_vol == 1:
    print("Hypertonic Fluid Adminstration NaCl/NaHCO3")
    print("END")
    exit()

if ecf_vol == 2:
    print("Hypotonic fluid loss GI, Renal, Skin")
    print("END")
    exit()

print("Pure Water Loss")
print("---------------")
print("")
serum_Gluc = float(input("Serum Glucose (mg/dL): "))
serum_Urea = float(input("Serum Urea (mg/dL): "))

serum_BUN = serum_Urea / 2.1428

est_serum_osmolality = 2.0 * serum_Na + (serum_Gluc/18.0) + (serum_BUN/2.8)

print("")
print("Est. Pl. Osmolality (mOsm/kg): {} [280-285]".format(round(est_serum_osmolality)))
print("   Low = Diabetes Insipidus")
print("   High = Extra renal water loss")
print("")

print("Calculate Free water deficit")
print("----------------------------")
sex = input("Sex (M/F): ")
mass = float(input("Weight (kg): "))
target_Na = 140

water_fraction = 0.5
if sex.upper() == "M":
    water_fraction = 0.6

print("Water fraction: {}".format(water_fraction))

tbw = water_fraction * mass

tbw_deficit = tbw * (1 - (target_Na/serum_Na))
tbw_deficit_half = tbw_deficit / 2.0

print("Free Water Deficit is {} Liters".format(round(tbw_deficit, 2)))
print("If Acute correct quickly, up to 1mmoL/L/hr")
print("If Chronic Slow Correction:")
print("     Give 1/2 ({}) over first 24 hours".format(round(tbw_deficit_half, 2)))
print("     Give remaining over next 24-48 hours")
print("")
