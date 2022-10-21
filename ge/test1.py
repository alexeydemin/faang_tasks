inputData = "10\n0"

def codeHere():
    total, diff = inputData.split('\n')
    total = int(total)
    diff = int(diff)
    x = (total-diff)//2
    return str(x+diff) + '\n' + str(x)

print(codeHere())