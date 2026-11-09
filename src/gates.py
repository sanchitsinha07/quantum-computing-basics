import numpy as np

Pauli_X = np.array([
    [0, 1],
    [1, 0]
], dtype=complex)

Pauli_Y = np.array([
    [0, -1j],
    [1j, 0]
], dtype=complex)

Pauli_Z = np.array([
    [1, 0],
    [0, -1]
], dtype=complex)

Hadamard = (1 / np.sqrt(2)) * np.array([
    [1, 1],
    [1, -1]
], dtype=complex)

CNOT = np.array([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
], dtype=complex)


def apply_gate(gate, state):
    """Apply a quantum gate to a state vector."""
    return gate @ state