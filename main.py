def count_string(string):
    result = {}
    for symbol in string:
        result[symbol] = result.get(symbol, 0) + 1

    for s in result:
        print(s, result[s])


count_string('aaaaaf')
