import json

def loading_key(seed):
    with open(f"{seed}/key.json") as file:
        key_data = json.load(file)
    key_map = key_data["map"]
    return key_map


def loading_reverse_key(seed):
    with open(f"{seed}/reverse_key.json") as file:
        reverse_key_data = json.load(file)
    reverse_key_map = reverse_key_data["map"]
    return reverse_key_map


def encode(seed):
    string = input("Enter the string: ")
    key_map = loading_key(seed)
    enocoded_text = ""
    for _ in list(string):
        enocoded_text += key_map.get(_, "")
    return enocoded_text


def decode(seed):
    string = input("Enter the string: ")
    reverse_key_map = loading_reverse_key(seed)
    decoded_text = ""
    for _ in range(0, len(string), 5):
        chunk = string[_:_+5]
        decoded_text += reverse_key_map.get(chunk, '?')
    return decoded_text