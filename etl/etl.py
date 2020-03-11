def transform(legacy_data):
    return {letter.lower(): key for key in legacy_data for letter in legacy_data[key]}
