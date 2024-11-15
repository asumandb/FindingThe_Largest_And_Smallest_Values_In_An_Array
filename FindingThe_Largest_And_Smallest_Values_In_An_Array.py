def min_max(dizi):
    min = dizi[0]
    max = dizi[0]

    for i in dizi[1:]:
        if i > max:
            max = i

        if i < min:
            min = i

    return max, min

min_max([9,3,7,4,1])
