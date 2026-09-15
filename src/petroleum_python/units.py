"""Small, explicit engineering-unit conversions."""

from __future__ import annotations
import numpy as np

PSI_TO_PA = 6_894.757293168
ATM_TO_PA = 101_325.0
DARCY_TO_M2 = 9.869233e-13
MILLIDARCY_TO_M2 = DARCY_TO_M2 / 1_000.0
ACRE_FOOT_TO_BBL = 7_758.36735

def _value(result):
    return float(result) if np.ndim(result) == 0 else result

def psi_to_mpa(value):
    return _value(np.asarray(value, dtype=float) * PSI_TO_PA / 1_000_000.0)

def mpa_to_psi(value):
    return _value(np.asarray(value, dtype=float) * 1_000_000.0 / PSI_TO_PA)

def atm_to_psi(value):
    return _value(np.asarray(value, dtype=float) * ATM_TO_PA / PSI_TO_PA)

def kelvin_to_celsius(value):
    return _value(np.asarray(value, dtype=float) - 273.15)

def md_to_m2(value):
    return _value(np.asarray(value, dtype=float) * MILLIDARCY_TO_M2)

def m2_to_md(value):
    return _value(np.asarray(value, dtype=float) / MILLIDARCY_TO_M2)
