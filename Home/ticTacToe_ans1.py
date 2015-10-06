def checkio(gr):
    
    results = []
    for str in gr:
        results.append(str)
        print str
    print results    
    verticals = ["" for i in range(3)]
    for i in range(3):
        for str in gr:
            verticals[i] += str[i]
    results += verticals
    print results
    diagonals = ["" for i in range(2)]
    for i in range(3):
        diagonals[0] += gr[i][i]
        diagonals[1] += gr[i][2-i]
    results += diagonals    
    print results    
    return "X" if "XXX" in results else ("O" if "OOO" in results else "D")

print checkio([
    "X.O",
    "XX.",
    "XOO"])
