
from .const import *

def coulomb(z1: int, z2: int, eps_r: float, r: float) -> float:
    """クーロン相互作用エネルギーを計算します。

    Args:
        z1 (int): 荷数。
        z2 (int): 荷数。
        eps_r (float): 溶媒の比誘電率。
        r (float): ２つの電荷の距離。(m)

    Returns:
        float: クーロン相互作用エネルギー (kcal/mol)
    """
     
    U: float = (z1*z2*e**2)/(4*pi*eps_0*eps_r*r) * (NA*J2kcal)
    return U

if __name__ == "__main__":
    res = coulomb(1,-1,1,2.4e-10)
    print(res)
