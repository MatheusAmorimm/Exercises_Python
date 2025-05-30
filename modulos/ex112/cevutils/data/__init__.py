def leiadinheiro(msg):
    valid = False
    while not valid:
        entry = str(input(msg)).replace(',', '.').strip()
        if entry.isalpha() or entry == '':
            print(f"\033[0;31mERRO: \"{entry}\" é um preço inválido!\033[m")
        else:
            valid = True
            return float(entry)
    return None