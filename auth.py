import os


def login():
    seed = float(input("Enter the seed: "))
    seed = str(seed)
    if os.path.exists(seed):
        return True, seed
    else:
        return False, seed