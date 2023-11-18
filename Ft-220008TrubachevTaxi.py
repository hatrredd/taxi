taxDist = []; taxCost = []; Summa = []; result = []
N = int(input("Введите количество такси, которое хотите заказать: "))
while N < 1:
    N = int(input("Введено некорректное число машин, попробуйте ещё раз: "))
for D in range (N):
    print(D+1, "сотрудник -", end="")
    Dist = int(input(" сколько километров до дома: "))
    while Dist < 1:
        Dist = int(input("Введено некорректное число километров, попробуйте ещё раз: "))
    taxDist.append(Dist)
for C in range(N):
    print(C+1, "машина - ", end="")
    Cost = int(input(" стоимость за 1 километр: "))
    while Cost < 1:
        Cost = int(input("Введено некорректная стоимость, попробуйте ещё раз: "))
    taxCost.append(Cost)
sortDist = taxDist.copy()
sortCost = taxCost.copy()
sortDist.sort()
sortCost.sort(reverse=True)
for i in range(N):
    res = taxDist.index(sortDist[i]) + 1, "сотрудник поедет на", taxCost.index(sortCost[i]) + 1, "машине"
    result.append(res)
    Summa.append(taxDist[taxDist.index(sortDist[i])]*taxCost[taxCost.index(sortCost[i])])
    taxDist[taxDist.index(sortDist[i])] = 0
    taxCost[taxCost.index(sortCost[i])] = 0
result.sort()
for k in range(len(result)):
    print(*result[k])
x = sum(Summa); Summa =[]
match (x//1000)%10:
    case 9:
        Summa.append("девять тысяч")
    case 8:
        Summa.append("восемь тысяч")
    case 7:
        Summa.append("семь тысяч")
    case 6:
        Summa.append("шесть тысяч")
    case 5:
        Summa.append("пять тысяч")
    case 4:
        Summa.append("четыре тысячи")
    case 3:
        Summa.append("три тысячи")
    case 2:
        Summa.append("две тысячи")
    case 1:
        Summa.append("одна тысяча")
match (x//100)%10:
    case 9:
        Summa.append("девятьсот")
    case 8:
        Summa.append("восемьсот")
    case 7:
        Summa.append("семьсот")
    case 6:
        Summa.append("шестьсот")
    case 5:
        Summa.append("пятьсот")
    case 4:
        Summa.append("четыреста")
    case 3:
        Summa.append("триста")
    case 2:
        Summa.append("двести")
    case 1:
        Summa.append("сто")
match (x//10)%10:
    case 9:
        Summa.append("девяносто")
    case 8:
        Summa.append("восемьдесят")
    case 7:
        Summa.append("семьдесят")
    case 6:
        Summa.append("шестьдесят")
    case 5:
        Summa.append("пятьдесят")
    case 4:
        Summa.append("сорок")
    case 3:
        Summa.append("тридцать")
    case 2:
        Summa.append("двадцать")
    case 1:
        match x%100:
            case 19:
                Summa.append("девятнадцать")
            case 18:
                Summa.append("восемнадцать")
            case 17:
                Summa.append("семнадцать")
            case 16:
                Summa.append("шестнадцать")
            case 15:
                Summa.append("пятнадцать")
            case 14:
                Summa.append("четырнадцать")
            case 13:
                Summa.append("тринадцать")
            case 12:
                Summa.append("двенадцать")
            case 11:
                Summa.append("одиннадцать")
            case 10:
                Summa.append("десять")
if x%100 < 20 and x%100 > 9:
    Summa.append("рублей")
else:
    match x%10:
        case 9:
            Summa.append("девять рублей")
        case 8:
            Summa.append("восемь рублей")
        case 7:
            Summa.append("семь рублей")
        case 6:
            Summa.append("шесть рублей")
        case 5:
            Summa.append("пять рублей")
        case 4:
            Summa.append("четыре рубля")
        case 3:
            Summa.append("три рубля")
        case 2:
            Summa.append("два рубля")
        case 1:
            Summa.append("один рубль")
        case 0:
            Summa.append("рублей")
Summa[0] = Summa[0].capitalize()
print("Общая стоимость всех такси в рублях:", x, "-", *Summa)