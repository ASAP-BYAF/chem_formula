import math

# constant
## 物理量
e: float = 1.602e-19 # C
eps_0: float = 8.85e-12 # m^{-3} :kg^{-1} s^4 A^2
NA: float = 6.02e+23
kb: float = 1.38e-23
h: float = 6.63e-34
c: float = 3.0e+8
faraday: float = 9.65e+4

## 数学
pi: float = math.pi
exp = math.e

## 単位変換
J2kcal: float = 1/4184 # kcal/J
htr2kcalmol: float = 627.5 #kcal mol^{-1} htr{-1}
kayser2K: float = 100*(h*c)/kb

## 補助単位変換
Ang2m: float = 1.0e-10
