from .const import kb, h, exp, kayser2K, NA, J2kcal

def calc_e_vib(T_vib: float, T: float) -> float:
    """ 振動を温度と温度を受け取り振動のエネルギーを返します。

    Args:
        T_vib (float): 振動温度 (K)
        T (float): 温度 (K)

    Returns:
        float: 振動エネルギー (kcal/mol)
    """
    
    e_vib: float = kb*T_vib*(0.5 + (exp**(T_vib/T)-1)**(-1))
    e_vib *= NA*J2kcal
    return e_vib

if __name__ == "__main__":
    T_vib = 359*kayser2K
    print(T_vib)
    T = 300
    res: float = calc_e_vib(T_vib, T)
    print(res)
    