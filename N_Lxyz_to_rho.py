import numpy as np

def N_Lxyz_to_rho_func(N, Lxyz, len_unit=1):
    ''' セルの各辺の長さと含まれる粒子数を受け取り、数密度を返す。

    Args:
        N (int): ある化学種のセル内の個数
        Lxyz (ndarray[float]): セルの各辺の長さ。 Lx, Ly, Lz の順で、
            m 単位で格納されていることを想定。
    Returns:
        float : 数密度
    '''
    
    Lxyz *= len_unit
    return N / np.prod(Lxyz)

