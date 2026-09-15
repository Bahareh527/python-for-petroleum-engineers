"""Introductory petrophysical and volumetric calculations."""

from __future__ import annotations
import math
from .units import ACRE_FOOT_TO_BBL

def _positive(name: str, value: float) -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive")

def _fraction(name: str, value: float) -> None:
    if not 0.0 <= value <= 1.0:
        raise ValueError(f"{name} must be between 0 and 1")

def core_bulk_volume_m3(diameter_m: float, length_m: float) -> float:
    _positive("diameter_m", diameter_m)
    _positive("length_m", length_m)
    return math.pi * (diameter_m / 2.0) ** 2 * length_m

def porosity(pore_volume: float, bulk_volume: float) -> float:
    _positive("bulk_volume", bulk_volume)
    if pore_volume < 0 or pore_volume > bulk_volume:
        raise ValueError("pore_volume must be between zero and bulk_volume")
    return pore_volume / bulk_volume

def hydrocarbon_pore_volume(bulk_volume: float, porosity_fraction: float, water_saturation: float) -> float:
    _positive("bulk_volume", bulk_volume)
    _fraction("porosity_fraction", porosity_fraction)
    _fraction("water_saturation", water_saturation)
    return bulk_volume * porosity_fraction * (1.0 - water_saturation)

def oil_in_place_stb(
    area_acres: float,
    net_pay_ft: float,
    porosity_fraction: float,
    water_saturation: float,
    formation_volume_factor_rb_stb: float,
) -> float:
    _positive("area_acres", area_acres)
    _positive("net_pay_ft", net_pay_ft)
    _positive("formation_volume_factor_rb_stb", formation_volume_factor_rb_stb)
    _fraction("porosity_fraction", porosity_fraction)
    _fraction("water_saturation", water_saturation)
    reservoir_oil_bbl = (
        ACRE_FOOT_TO_BBL * area_acres * net_pay_ft * porosity_fraction * (1.0 - water_saturation)
    )
    return reservoir_oil_bbl / formation_volume_factor_rb_stb
