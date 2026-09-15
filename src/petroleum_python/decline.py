"""Classical deterministic decline-curve functions."""

from __future__ import annotations
import numpy as np

def _inputs(initial_rate: float, nominal_decline: float) -> None:
    if initial_rate <= 0 or nominal_decline < 0:
        raise ValueError("initial_rate must be positive and nominal_decline nonnegative")

def exponential_rate(time, initial_rate: float, nominal_decline: float):
    _inputs(initial_rate, nominal_decline)
    time = np.asarray(time, dtype=float)
    if (time < 0).any():
        raise ValueError("time cannot be negative")
    return initial_rate * np.exp(-nominal_decline * time)

def hyperbolic_rate(time, initial_rate: float, nominal_decline: float, b: float):
    _inputs(initial_rate, nominal_decline)
    if not 0.0 < b <= 1.0:
        raise ValueError("b must be in (0, 1]")
    time = np.asarray(time, dtype=float)
    if (time < 0).any():
        raise ValueError("time cannot be negative")
    return initial_rate / np.power(1.0 + b * nominal_decline * time, 1.0 / b)
