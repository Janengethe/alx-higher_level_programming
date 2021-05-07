#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) is str:
        dic = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        num = 0
        for i, j in zip(roman_string, roman_string[1:]):
            if dic[i] < dic[j]:
                num -= dic[i]
            else:
                num += dic[i]
        num += dic[roman_string[-1]]
        return num
    else:
        return 0
