def clean_text(text, default=None):
    """
    Cleans the input text by removing leading/trailing whitespace and converting to lowercase.
    """
    if text is None:
        return default
    text = text.strip().lower() 
    return text

def to_float(value, default=None):
    """
    Converts the input value to a float. Returns default if conversion fails.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default

def to_int(value, default=None):
    """
    Converts the input to an integer. Returns the default value if conversion fails.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

assert clean_text("  ONTARIO  ") == "ontario"
assert clean_text(" ") == ""
assert clean_text(" ") == ""
assert clean_text(None) == None
assert to_float("42.0") == 42.0
assert to_float(0) == 0.00
assert to_int("0") == 0
assert to_int(-3) == -3
assert to_int("4.5") == None
assert to_int("12a") == None
assert to_int("0") == 0
