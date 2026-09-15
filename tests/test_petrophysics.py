import pytest
from petroleum_python.petrophysics import core_bulk_volume_m3, oil_in_place_stb, porosity

def test_core_and_porosity():
    assert core_bulk_volume_m3(0.1, 0.2) == pytest.approx(0.0015707963)
    assert porosity(0.2, 1.0) == pytest.approx(0.2)

def test_invalid_fraction_rejected():
    with pytest.raises(ValueError):
        oil_in_place_stb(100, 30, 1.2, 0.2, 1.1)

def test_ooip_reference_case():
    expected = 7758.36735 * 100 * 30 * 0.2 * 0.75 / 1.2
    assert oil_in_place_stb(100, 30, 0.2, 0.25, 1.2) == pytest.approx(expected)
