import numpy as np

from src.gates import Pauli_X, Pauli_Y, Pauli_Z, Hadamard, CNOT
from src.states import ZERO, ONE, probabilities


def test_pauli_x():
    result = Pauli_X @ ZERO
    np.testing.assert_allclose(result, ONE)


def test_pauli_z():
    result = Pauli_Z @ ZERO
    np.testing.assert_allclose(result, ZERO)


def test_hadamard():
    result = Hadamard @ ZERO

    expected = np.array(
        [1 / np.sqrt(2), 1 / np.sqrt(2)],
        dtype=complex
    )

    np.testing.assert_allclose(result, expected)


def test_hadamard_probabilities():
    result = Hadamard @ ZERO

    np.testing.assert_allclose(
        probabilities(result),
        [0.5, 0.5]
    )


def test_cnot():
    two_qubit_zero = np.array([1, 0, 0, 0], dtype=complex)
    result = CNOT @ two_qubit_zero

    np.testing.assert_allclose(result, two_qubit_zero)