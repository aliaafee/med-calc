"""Calculators"""

from . import sodium

CALCULATORS = {
    "sodium": sodium
}

def get_calculator(name):
    try:
        return CALCULATORS[name]
    except KeyError:
        return None

