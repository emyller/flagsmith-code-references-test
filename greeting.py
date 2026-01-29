"""
Greeting module - handles user-facing messages.

Uses the greeting feature flag to customize welcome messages.
"""


def get_greeting(flags) -> str:
    """
    Get the greeting message for the user.

    The greeting flag value determines what message is shown.
    """
    greeting_value = flags.get_feature_value("greeting")

    if greeting_value:
        return f"🎉 {greeting_value}"
    else:
        return "Welcome to Fake App!"


def get_personalized_greeting(flags, user_name: str) -> str:
    """
    Get a personalized greeting for a specific user.

    Combines the greeting flag value with the user's name.
    """
    base_greeting = flags.get_feature_value("greeting")

    if base_greeting:
        return f"{base_greeting}, {user_name}!"
    else:
        return f"Hello, {user_name}!"


def get_time_based_greeting(flags, hour: int) -> str:
    """
    Get a greeting based on time of day.

    Falls back to the greeting flag if no time-specific message applies.
    """
    if 5 <= hour < 12:
        time_greeting = "Good morning"
    elif 12 <= hour < 17:
        time_greeting = "Good afternoon"
    elif 17 <= hour < 21:
        time_greeting = "Good evening"
    else:
        time_greeting = "Hello"

    # Check if we have a custom greeting configured
    custom_greeting = flags.get_feature_value("greeting")
    if custom_greeting:
        return f"{time_greeting}! {custom_greeting}"

    return f"{time_greeting}!"


class GreetingService:
    """Service class for managing greetings."""

    def __init__(self, flags):
        self.flags = flags
        self._cache = {}

    def get_cached_greeting(self, locale: str = "en") -> str:
        """Get greeting with caching support."""
        if locale not in self._cache:
            greeting = self.flags.get_feature_value("greeting")
            self._cache[locale] = greeting or "Welcome!"

        return self._cache[locale]
