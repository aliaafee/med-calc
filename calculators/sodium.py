"""
Serum Sodium Correction Protocol
--------------------------------
Not for medical use.

References:
    1. Lee K. The NeuroICU Book, Second Edition. 2 edition. New York: McGraw-Hill Education / Medical; 2017. 1104 p. 
"""
from click import echo
from .utils import prompt_float, prompt_choice


def get_est_plasma_osmolality(serum_Na):
    serum_Gluc = prompt_float("Serum Glucose", "mg/dL")
    serum_Urea = prompt_float("Serum Urea", "mg/dL")

    serum_BUN = serum_Urea / 2.1428

    return 2.0 * serum_Na + (serum_Gluc/18.0) + (serum_BUN/2.8)


def get_tbw():
    sex = prompt_choice("Sex", ["M", "F"])
    mass = prompt_float("Weight", "kg")#float(input("Weight (kg): "))

    water_fraction = 0.5
    if sex.upper() == "M":
        water_fraction = 0.6

    echo("Water fraction: {}".format(water_fraction))

    return water_fraction * mass


def hyponatremia(serum_Na):
    echo("Hyponatremia")
    echo("-------------")

    est_plasma_osmolality = get_est_plasma_osmolality(serum_Na)

    echo("")
    echo("Est. Pl. Osmolality (mOsm/kg): {} [280-295]".format(round(est_plasma_osmolality)))
    echo("")

    if est_plasma_osmolality >= 280 and est_plasma_osmolality <= 295:
        echo("Normal Pl. Osmolality, consider Pseudohyponatremia")
        return

    if est_plasma_osmolality > 295:
        echo("Hypertonic Hypernatremia")
        return

    echo("Hypotonic Hypernatremia")
    echo("")

    mes_urine_osmolality = prompt_float("Measured Urine Osmolality", "mOsm/kg")

    if mes_urine_osmolality < 100.0:
        echo("Consider Primary Polydipsia")
        return

    echo("")
    echo("ECF Volume\n----------\n1) Increased\n2) Decreased\n3) Normal")
    ecf_vol = prompt_choice("ECF Volume", [1, 2, 3])
    echo("")

    if ecf_vol == 1:
        echo("Consider Edema States")

    if ecf_vol == 2:
        echo("Consider Volume Depletion")

    if ecf_vol == 3:
        echo("Consider Adrenal Insufficiency, Hypothyroidism, SIADH, Thiazide Diuretic, K Depletion")
        if mes_urine_osmolality > 100:
            echo("Most probably SIADH as urins osmolality > 100 mOsm/L")

    echo("")

    if serum_Na < 125:
        echo("Sodium level is very low, consider rapid correction if symptomatic")
        echo("Rapid correction")
        echo("   Hypertonic Saline (3%, 513 mmol/L) 100mL over 10 minutes")
        echo("   Repeat twice if necessary")
        echo("   Predicted to raise by 4-6 mEq/L immediately")
        echo("   Monitor Na 4-6 hrly")
        echo("")

    echo("Calculate Sodium Correction")
    echo("---------------------------")

    tbw = get_tbw()
    delta_Na = prompt_float("Delta Na correction over 24hrs", "mEq/L)")

    vol_3_saline = delta_Na * tbw / 513.0

    echo("Vol 3% saline is {} mL/24hours for slow correction".format(round(vol_3_saline*1000.0)))
    echo("Remember to Monitor Na 4-6 hrly")


def hypernatremia(serum_Na):
    echo("Hypernatremia")

    echo("ECF Volume\n----------\n1) Increased\n2) Decreased\n3) Normal")
    ecf_vol = prompt_choice("ECF Volume", [1, 2, 3])

    if ecf_vol == 1:
        echo("Hypertonic Fluid Adminstration NaCl/NaHCO3")
        return

    if ecf_vol == 2:
        echo("Hypotonic fluid loss GI, Renal, Skin")
        return

    echo("Pure Water Loss")
    echo("---------------")
    echo("")

    est_plasma_osmolality = get_est_plasma_osmolality(serum_Na)

    echo("")
    echo("Est. Pl. Osmolality (mOsm/kg): {} [280-295]".format(round(est_plasma_osmolality)))
    echo("   Low = Diabetes Insipidus")
    echo("   High = Extra renal water loss")
    echo("")

    echo("Calculate Free water deficit")
    echo("----------------------------")

    tbw = get_tbw()

    target_Na = 140

    tbw_deficit = tbw * (1 - (target_Na/serum_Na))
    tbw_deficit_half = tbw_deficit / 2.0

    echo("")
    echo("Free Water Deficit is {} Liters".format(round(tbw_deficit, 2)))
    echo("")
    echo("If Acute correct quickly, up to 1 mmoL/L/hr")
    echo("If Chronic Slow Correction:")
    echo("     Give 1/2 ({}) over first 24 hours".format(round(tbw_deficit_half, 2)))
    echo("     Give remaining over next 24-48 hours")
    echo("")


def start():
    serum_Na = prompt_float("Serum Na", "mmol/L")

    if serum_Na > 145.0:
        hypernatremia(serum_Na)
        return

    if serum_Na < 135.0:
        hyponatremia(serum_Na)
        return

    echo("Looks good, do not think we need to do anything.")
