import numpy as np

ZERO = np.array([1, 0], dtype=complex)
ONE = np.array([0, 1], dtype=complex)


def normalize(state):
    """Normalize a quantum state vector."""
    norm = np.linalg.norm(state)

    if norm == 0:
        raise ValueError("A quantum state cannot have zero norm.")

    return state / norm


def probabilities(state):
    """Calculate measurement probabilities."""
    return np.abs(state) ** 2