"""Deterministic synthetic datasets used throughout the course."""

from __future__ import annotations
from pathlib import Path
import numpy as np
import pandas as pd
from .decline import hyperbolic_rate

def generate_wells(seed: int = 42, count: int = 36) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    fields = np.resize(np.array(["North", "Central", "South"]), count)
    rng.shuffle(fields)
    porosity = np.clip(rng.normal(0.21, 0.035, count), 0.10, 0.32)
    permeability = np.exp(6.0 * (porosity - 0.18) + rng.normal(3.7, 0.45, count))
    sw = np.clip(0.48 - 0.9 * (porosity - 0.15) + rng.normal(0, 0.045, count), 0.15, 0.60)
    pressure = rng.normal(24.0, 2.8, count)
    net_pay = np.clip(rng.normal(18.0, 5.0, count), 5.0, 34.0)
    rate = np.clip(4.5 * permeability * (1.0 - sw) + rng.normal(80, 35, count), 20, None)
    return pd.DataFrame({
        "well_id": [f"W-{index:02d}" for index in range(1, count + 1)],
        "field": fields,
        "x_m": rng.uniform(0, 8_000, count).round(1),
        "y_m": rng.uniform(0, 6_000, count).round(1),
        "net_pay_m": net_pay.round(2),
        "porosity_fraction": porosity.round(4),
        "water_saturation_fraction": sw.round(4),
        "permeability_md": permeability.round(2),
        "pressure_mpa": pressure.round(2),
        "temperature_k": rng.normal(355, 8, count).round(2),
        "oil_rate_bpd": rate.round(1),
    })

def generate_ift(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed + 1)
    rows = []
    for temperature in [323.15, 343.15, 363.15, 383.15]:
        for pressure in np.linspace(5, 35, 15):
            for salinity in [2.0, 6.0]:
                # Illustrative teaching surface, not an empirical correlation.
                ift = 31.0 - 0.10 * (temperature - 323.15) - 0.24 * pressure + 0.38 * salinity
                ift += rng.normal(0, 0.65)
                rows.append((temperature, pressure, salinity, max(2.0, ift)))
    frame = pd.DataFrame(rows, columns=["temperature_k", "pressure_mpa", "salinity_wt_pct", "ift_mn_m"])
    frame.insert(0, "sample_id", [f"IFT-{i:03d}" for i in range(1, len(frame) + 1)])
    return frame.round({"temperature_k": 2, "pressure_mpa": 3, "salinity_wt_pct": 2, "ift_mn_m": 3})

def generate_production(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed + 2)
    rows = []
    settings = {"W-04": (820, 0.035, 0.65), "W-17": (610, 0.028, 0.50), "W-29": (940, 0.042, 0.80)}
    for well, (qi, decline, b_value) in settings.items():
        months = np.arange(60)
        expected = hyperbolic_rate(months, qi, decline, b_value)
        observed = np.clip(expected * (1.0 + rng.normal(0, 0.035, len(months))), 0, None)
        water_cut = np.clip(0.18 + 0.006 * months + rng.normal(0, 0.01, len(months)), 0, 0.80)
        for month, oil, wc in zip(months, observed, water_cut):
            rows.append((well, int(month), float(oil), float(oil * wc / (1.0 - wc))))
    return pd.DataFrame(rows, columns=["well_id", "month", "oil_rate_bpd", "water_rate_bpd"]).round(2)

def write_course_data(directory: str | Path, seed: int = 42) -> None:
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    generate_wells(seed).to_csv(directory / "synthetic_wells.csv", index=False)
    generate_ift(seed).to_csv(directory / "synthetic_ift.csv", index=False)
    generate_production(seed).to_csv(directory / "synthetic_production.csv", index=False)
