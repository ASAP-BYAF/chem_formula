from .const import *

def dipole(z: int, d: float) -> float:
    """双極子モーメントの大きさを計算します。

    Args:
        z (int): 荷数。
        d (float): 距離 (m)

    Returns:
        float: 双極子モーメントの大きさ。(C m)
    """

    mu: float = z*e*d
    return mu

if __name__ == "__main__":
    res = dipole(1, 2.82e-10)
    print(res)