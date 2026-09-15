import pandas as pd
from petroleum_python.synthetic import generate_ift, generate_production, generate_wells

def test_generators_are_deterministic():
    pd.testing.assert_frame_equal(generate_wells(8), generate_wells(8))
    pd.testing.assert_frame_equal(generate_ift(8), generate_ift(8))
    pd.testing.assert_frame_equal(generate_production(8), generate_production(8))

def test_synthetic_ranges_are_valid():
    wells = generate_wells()
    assert wells["porosity_fraction"].between(0, 1).all()
    assert wells["water_saturation_fraction"].between(0, 1).all()
    assert (wells[["permeability_md", "pressure_mpa", "oil_rate_bpd"]] > 0).all().all()
