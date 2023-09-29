from .const import *

def born(z: int, eps_r: float, a: float) -> float:
    """ボルンの式に基づいて溶媒和自由エネルギーを計算します。

    Args:
        z (int): 荷数。
        eps_r (float): 溶媒の比誘電率。
        a (float): 溶媒の中で溶質電荷が占めるとする空洞の半径。(m)

    Returns:
        float: ボルンの式による溶媒和自由エネルギー
    """

    dU: float = - ( (z*e)**2/(8*pi*eps_0*a) ) * (1 - (1/eps_r)) * (NA*J2kcal)
    return dU

if __name__ == "__main__":
    na = born(1,9.1,1.13e-10)
    cl = born(1,9.1,2.21e-10)
    print(f"na = {na:5.3e}, cl = {cl:5.3e}")