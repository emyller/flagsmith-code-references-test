"""
Checkout module - handles payment processing.

Uses the checkout_v2 feature flag to switch between checkout implementations.
"""


def process_checkout(flags, cart_total: float) -> dict:
    """
    Process a checkout transaction.

    Uses checkout_v2 flag to determine which checkout flow to use.
    """
    # Check if we should use the new checkout flow
    if flags.is_feature_enabled("checkout_v2"):
        return _checkout_v2_flow(cart_total)
    else:
        return _checkout_legacy_flow(cart_total)


def _checkout_v2_flow(cart_total: float) -> dict:
    """
    New checkout flow with improved UX.

    Features:
    - Streamlined payment form
    - Express checkout options
    - Real-time validation
    """
    print("  → Using checkout_v2 flow (new experience)")
    return {
        "success": True,
        "flow": "v2",
        "amount": cart_total,
        "features": ["express_checkout", "real_time_validation", "saved_cards"],
    }


def _checkout_legacy_flow(cart_total: float) -> dict:
    """Legacy checkout flow for backwards compatibility."""
    print("  → Using legacy checkout flow")
    return {
        "success": True,
        "flow": "legacy",
        "amount": cart_total,
        "features": ["basic_checkout"],
    }


def validate_checkout_eligibility(flags, user_id: str) -> bool:
    """
    Validate if a user is eligible for checkout.

    The checkout_v2 flag also enables additional validation rules.
    """
    # Basic validation
    if not user_id:
        return False

    # checkout_v2 includes enhanced fraud detection
    if flags.is_feature_enabled("checkout_v2"):
        print(f"  → Running enhanced validation for user {user_id}")
        # Simulate enhanced validation
        return True

    return True
