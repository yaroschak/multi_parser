import random


def f(url: str) -> bool:
    result = random.choice([False, True])
    mapa = {False: "Not done", True: "Done"}
    print(f"{mapa[result]}: {url}")
    return result
