import json

def load_crypto_groups(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise ValueError(f"The file {file_path} was not found. Please check the file path.")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON. Please check the format of the file.")
    except Exception as e:
        raise ValueError(f"An unexpected error occurred while loading the crypto groups: {e}")
