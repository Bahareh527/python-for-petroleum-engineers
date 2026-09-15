import numpy as np
import pytest
from petroleum_python.units import atm_to_psi, md_to_m2, psi_to_mpa

def test_reference_conversions():
    assert atm_to_psi(1.0) == pytest.approx(14.69595, rel=1e-6)
    assert md_to_m2(1000.0) == pytest.approx(9.869233e-13)
    assert psi_to_mpa(1000.0) == pytest.approx(6.894757293168)

def test_vector_conversion():
    result = psi_to_mpa([1000, 2000])
    assert isinstance(result, np.ndarray)
    assert result[1] == pytest.approx(2 * result[0])
