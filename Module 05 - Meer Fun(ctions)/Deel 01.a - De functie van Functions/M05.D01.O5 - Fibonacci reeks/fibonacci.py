def fibonacci(aantal: int) -> list:
    getallenreeks = [0,1]
    for x in range(aantal):
        getallenreeks.append(getallenreeks[x] + getallenreeks[x + 1])
    snede = getallenreeks[-1] / getallenreeks[-2]
    return getallenreeks, snede
print(fibonacci(8))