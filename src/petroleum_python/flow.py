"""Single-phase, one-dimensional linear Darcy-flow examples in SI units."""

from __future__ import annotations
from .units import m2_to_md, md_to_m2

def _require_positive(**values: float) -> None:
    invalid = [name for name, value in values.items() if value <= 0]
    if invalid:
        raise ValueError("values must be positive: " + ", ".join(invalid))

def darcy_flow_rate_m3_s(
    permeability_md: float,
    area_m2: float,
    pressure_drop_pa: float,
    viscosity_pa_s: float,
    length_m: float,
) -> float:
    _require_positive(
        permeability_md=permeability_md, area_m2=area_m2,
        pressure_drop_pa=pressure_drop_pa, viscosity_pa_s=viscosity_pa_s,
        length_m=length_m,
    )
    return md_to_m2(permeability_md) * area_m2 * pressure_drop_pa / (viscosity_pa_s * length_m)

def permeability_from_flow_md(
    flow_rate_m3_s: float,
    area_m2: float,
    pressure_drop_pa: float,
    viscosity_pa_s: float,
    length_m: float,
) -> float:
    _require_positive(
        flow_rate_m3_s=flow_rate_m3_s, area_m2=area_m2,
        pressure_drop_pa=pressure_drop_pa, viscosity_pa_s=viscosity_pa_s,
        length_m=length_m,
    )
    permeability_m2 = flow_rate_m3_s * viscosity_pa_s * length_m / (area_m2 * pressure_drop_pa)
    return m2_to_md(permeability_m2)
