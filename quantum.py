"""
Quantum module - experimental quantum computing features.

Uses the quantum_mode feature flag to enable experimental functionality.
"""

import random


def run_quantum_experiment(flags) -> dict:
    """
    Run a simulated quantum experiment.

    Only executes if quantum_mode is enabled.
    """
    if not flags.is_feature_enabled("quantum_mode"):
        return {"error": "Quantum mode is not enabled"}

    print("  → Initializing quantum simulation...")
    result = _simulate_quantum_state()
    print(f"  → Quantum state collapsed to: {result['state']}")

    return result


def _simulate_quantum_state() -> dict:
    """Simulate a quantum superposition collapse."""
    states = ["spin_up", "spin_down", "entangled", "superposition"]
    collapsed_state = random.choice(states)

    return {
        "state": collapsed_state,
        "probability": random.random(),
        "coherence_time_ms": random.randint(1, 100),
    }


def check_quantum_availability(flags) -> bool:
    """
    Check if quantum features are available.

    Returns True if quantum_mode flag is enabled.
    """
    return flags.is_feature_enabled("quantum_mode")


def run_quantum_optimization(flags, problem_size: int) -> dict:
    """
    Run quantum-inspired optimization algorithm.

    Requires quantum_mode to be enabled for full functionality.
    """
    if flags.is_feature_enabled("quantum_mode"):
        print(f"  → Running quantum optimization for problem size {problem_size}")
        return {
            "algorithm": "quantum_annealing",
            "iterations": problem_size * 100,
            "solution_quality": 0.95,
        }
    else:
        print(f"  → Running classical optimization for problem size {problem_size}")
        return {
            "algorithm": "simulated_annealing",
            "iterations": problem_size * 1000,
            "solution_quality": 0.80,
        }


class QuantumProcessor:
    """Processor for quantum computations."""

    def __init__(self, flags):
        self.flags = flags
        self.is_quantum_enabled = flags.is_feature_enabled("quantum_mode")

    def process(self, data: list) -> list:
        """Process data using quantum or classical methods."""
        if self.is_quantum_enabled:
            return self._quantum_process(data)
        return self._classical_process(data)

    def _quantum_process(self, data: list) -> list:
        """Quantum-enhanced data processing."""
        print("  → Using quantum processing pipeline")
        return [x * 2 for x in data]  # Simplified simulation

    def _classical_process(self, data: list) -> list:
        """Classical data processing."""
        print("  → Using classical processing pipeline")
        return [x + 1 for x in data]

    def get_processing_mode(self) -> str:
        """Return the current processing mode."""
        # Re-check the flag in case it changed
        if self.flags.is_feature_enabled("quantum_mode"):
            return "quantum"
        return "classical"
