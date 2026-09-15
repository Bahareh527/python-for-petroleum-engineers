import numpy as np
import pytest
from petroleum_python.decline import exponential_rate, hyperbolic_rate
from petroleum_python.flow import darcy_flow_rate_m3_s, permeability_from_flow_md

def test_darcy_round_trip():
    rate = darcy_flow_rate_m3_s(150, 0.01, 2e5, 1e-3, 0.1)
    recovered = permeability_from_flow_md(rate, 0.01, 2e5, 1e-3, 0.1)
    assert recovered == pytest.approx(150)

def test_decline_is_monotonic():
    time = np.arange(50)
    for values in [exponential_rate(time, 1000, 0.03), hyperbolic_rate(time, 1000, 0.03, 0.7)]:
        assert values[0] == pytest.approx(1000)
        assert (np.diff(values) <= 0).all()
