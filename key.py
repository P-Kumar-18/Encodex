import json, random, string, os


def key_generator():
    value = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + " ")
    seed = round(random.uniform(1, 100), 6)
    random.seed(seed)
    key = {}

    for _ in value:
        key[_] = "".join(random.choices(string.ascii_letters + string.digits, k = 5))

    reverse_key = {v: k for k, v in key.items()}

    key_data = {
        "seed": seed,
        "map": key
    }

    reverse_key_data = {
        "seed": seed,
        "map": reverse_key
    }

    os.makedirs(f"{seed}", exist_ok = True)

    with open(f"{seed}/key.json", "w") as file:
        json.dump(key_data, file, indent = 4)

    with open(f"{seed}/reverse_key.json", "w") as file:
        json.dump(reverse_key_data, file, indent = 4)

    return seed