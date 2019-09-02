#!/usr/bin/python
"""
Serum Sodium Correction Protocol
--------------------------------
Not for medical use.
Source: The Neuro ICU Book, Second Edition, 2018 McGraw-Hill, Lee Kiwon

"""

def get_est_plasma_osmolality(serum_Na):
    serum_Gluc = float(input("Serum Glucose (mg/dL): "))
    serum_Urea = float(input("Serum Urea (mg/dL): "))

    serum_BUN = serum_Urea / 2.1428

    return 2.0 * serum_Na + (serum_Gluc/18.0) + (serum_BUN/2.8)

def get_tbw():
    sex = input("Sex (M/F): ")
    mass = float(input("Weight (kg): "))

    water_fraction = 0.5
    if sex.upper() == "M":
        water_fraction = 0.6

    print("Water fraction: {}".format(water_fraction))

    return water_fraction * mass

def hypernatremia(serum_Na):
    print("Hypernatremia")
    print("-------------")
    print("")
    
    print("ECF Volume\n----------\n1) Increased\n2) Decreased\n3) Normal")
    ecf_vol = input("ECF Volume: ")
    print("")

    if ecf_vol == 1:
        print("Hypertonic Fluid Adminstration NaCl/NaHCO3")
        print("END")
        return

    if ecf_vol == 2:
        print("Hypotonic fluid loss GI, Renal, Skin")
        print("END")
        return

    print("Pure Water Loss")
    print("---------------")
    print("")

    est_plasma_osmolality = get_est_plasma_osmolality(serum_Na)

    print("")
    print("Est. Pl. Osmolality (mOsm/kg): {} [280-295]".format(round(est_plasma_osmolality)))
    print("   Low = Diabetes Insipidus")
    print("   High = Extra renal water loss")
    print("")

    print("Calculate Free water deficit")
    print("----------------------------")

    tbw = get_tbw()

    target_Na = 140

    tbw_deficit = tbw * (1 - (target_Na/serum_Na))
    tbw_deficit_half = tbw_deficit / 2.0

    print("")
    print("Free Water Deficit is {} Liters".format(round(tbw_deficit, 2)))
    print("")
    print("If Acute correct quickly, up to 1 mmoL/L/hr")
    print("If Chronic Slow Correction:")
    print("     Give 1/2 ({}) over first 24 hours".format(round(tbw_deficit_half, 2)))
    print("     Give remaining over next 24-48 hours")
    print("")


def hyponatremia(serum_Na):
    print("Hyponatremia")
    print("-------------")

    est_plasma_osmolality = get_est_plasma_osmolality(serum_Na)

    print("")
    print("Est. Pl. Osmolality (mOsm/kg): {} [280-295]".format(round(est_plasma_osmolality)))
    print("")

    if est_plasma_osmolality >= 280 and est_plasma_osmolality <= 295:
        print("Normal Pl. Osmolality, consider Pseudohyponatremia")
        return

    if est_plasma_osmolality > 295:
        print("Hypertonic Hypernatremia")
        return

    print("Hypotonic Hypernatremia")
    print("")

    mes_urine_osmolality = float(input("Measured Urine Osmolality (mOsm/kg): "))

    if mes_urine_osmolality < 100.0:
        print("Consider Primary Polydipsia")
        return

    print("")
    print("ECF Volume\n----------\n1) Increased\n2) Decreased\n3) Normal")
    ecf_vol = input("ECF Volume: ")
    print("")

    if ecf_vol == 1:
        print("Consider Edema States")

    if ecf_vol == 2:
        print("Consider Volume Depletion")

    if ecf_vol == 3:
        print("Consider Adrenal Insufficiency, Hypothyroidism, SIADH, Thiazide Diuretic, K Depletion")
        if mes_urine_osmolality > 100:
            print("Most probably SIADH as urins osmolality > 100 mOsm/L")

    print("")

    if serum_Na < 125:
        print("Sodium level is very low, consider rapid correction if symptomatic")
        print("Rapid correction")
        print("   Hypertonic Saline (3%, 513 mmol/L) 100mL over 10 minutes")
        print("   Repeat twice if necessary")
        print("   Predicted to raise by 4-6 mEq/L immediately")
        print("   Monitor Na 4-6 hrly")
        print("")

    print("Calculate Sodium Correction")
    print("---------------------------")

    tbw = get_tbw()
    delta_Na = float(input("Delta Na correction over 24hrs (mEq/L)"))

    vol_3_saline = delta_Na * tbw / 513.0

    print("Vol 3% saline is {} mL/24hours for slow correction".format(round(vol_3_saline*1000.0)))
    print("Remember to Monitor Na 4-6 hrly")

    


serum_Na = float(input("Serum Na (mmol/L): "))

if serum_Na > 145.0:
    hypernatremia(serum_Na)
    exit()

if serum_Na < 135.0:
    hyponatremia(serum_Na)
    exit()
    
    print("Looks good, do not think we need to anything")
