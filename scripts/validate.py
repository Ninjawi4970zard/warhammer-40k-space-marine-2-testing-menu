# Build: 25c4d623d11d03ea36fd406d48cf1784

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
