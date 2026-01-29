"""
Fake App - A demo application for Flagsmith Code References.

This app demonstrates feature flag usage across multiple modules.
"""

from flagsmith import Flagsmith

from checkout import process_checkout
from greeting import get_greeting
from quantum import run_quantum_experiment


def create_flagsmith_client(api_key: str) -> Flagsmith:
    """Initialize and return a Flagsmith client."""
    return Flagsmith(environment_key=api_key)


def main():
    """Main entry point for the fake app."""
    import os

    api_key = os.environ.get("FLAGSMITH_ENVIRONMENT_KEY")
    if not api_key:
        print("Error: FLAGSMITH_ENVIRONMENT_KEY environment variable not set")
        return

    flagsmith = create_flagsmith_client(api_key)
    flags = flagsmith.get_environment_flags()

    # Display greeting based on the greeting flag
    greeting_message = get_greeting(flags)
    print(greeting_message)

    # Check if quantum_mode is enabled for experimental features
    if flags.is_feature_enabled("quantum_mode"):
        print("\n🔬 Quantum Mode is ACTIVE!")
        run_quantum_experiment(flags)
    else:
        print("\n📊 Running in classical mode.")

    # Process a sample checkout
    print("\n💳 Processing checkout...")
    checkout_result = process_checkout(flags, cart_total=99.99)
    print(f"Checkout result: {checkout_result}")


if __name__ == "__main__":
    main()
