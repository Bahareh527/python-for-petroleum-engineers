"""Unit-aware educational calculations for petroleum engineers."""

from .decline import exponential_rate, hyperbolic_rate
from .flow import darcy_flow_rate_m3_s, permeability_from_flow_md
from .petrophysics import core_bulk_volume_m3, hydrocarbon_pore_volume, oil_in_place_stb, porosity

__all__ = [
    "core_bulk_volume_m3", "darcy_flow_rate_m3_s", "exponential_rate",
    "hydrocarbon_pore_volume", "hyperbolic_rate", "oil_in_place_stb",
    "permeability_from_flow_md", "porosity",
]
__version__ = "0.1.0"
