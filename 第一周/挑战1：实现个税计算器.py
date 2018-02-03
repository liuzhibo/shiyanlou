#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Parameter Error")
    exit()
try:
    gz = int(sys.argv[1])
except Exception as e:
    print("Parameter Error")

ynssde = gz - 3500

if 0 < ynssde <= 1500:
    ynse = ynssde * 0.03 - 0
elif 1500 < ynssde <= 4500:
    ynse = ynssde * 0.1 - 105
elif 4500 < ynssde <= 9000:
    ynse = ynssde * 0.2 - 555
elif 9000 < ynssde <= 35000:
    ynse = ynssde * 0.25 - 1005
elif 35000 < ynssde <= 55000:
    ynse = ynssde * 0.3 - 2755
elif 55000 < ynssde <= 80000:
    ynse = ynssde * 0.35 - 5505
elif ynssde > 80000:
    ynse = ynssde * 0.45 - 13505
else:
    ynse = 0
print(format(ynse, ".2f"))
