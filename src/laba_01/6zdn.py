chis = int(input())
ozh = []
zaoch = []
while chis > 0:
    fio = input()
    chis = chis - 1
    if 'True' in fio:
        ozh.append(fio)
    elif 'False' in fio:
        zaoch.append(fio)
print(len(ozh),len(zaoch))
