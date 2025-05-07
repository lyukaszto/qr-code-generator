def validate_input(data):
    if not isinstance(data, str) or len(data) == 0:
        raise ValueError("Input data must be a non-empty string.")
    return True

def format_data_for_qr(data):
    return data.strip()