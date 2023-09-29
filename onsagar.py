from .const import *

def onsagar(mu: float, a: float, eps_r: float) -> float:
    """オンサーガーの溶媒和自由エネルギーを計算します。

    Args:
        mu (float): 双極子モーメント。(C m)
        a (float): 溶媒の中で双極子が占めるとする空洞の半径。(m)
        eps_r (float): 溶媒の比誘電率。

    Returns:
        float: オンサーガーの式による溶媒和自由エネルギー
    """

    dU: float = -(mu**2)/(4*pi*eps_0*eps_r*(a)**3) * ((eps_r-1)/(2*eps_r+1)) * (NA*J2kcal)
    return dU   

if __name__ == "__main__":
    res = onsagar(4.51764e-29,2.4e-10,9.1)
    print(res)
