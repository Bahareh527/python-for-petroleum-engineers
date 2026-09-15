"""Reference solutions for selected exercises."""

from petroleum_python.flow import permeability_from_flow_md
from petroleum_python.petrophysics import core_bulk_volume_m3, oil_in_place_stb
from petroleum_python.units import psi_to_mpa

def compare_wells(planned, completed):
    planned, completed = set(planned), set(completed)
    return {"missing": sorted(planned - completed), "unexpected": sorted(completed - planned)}

def pressure_array_mpa(values_psi):
    return psi_to_mpa(values_psi)

__all__ = ["compare_wells", "core_bulk_volume_m3", "oil_in_place_stb", "permeability_from_flow_md", "pressure_array_mpa"]
