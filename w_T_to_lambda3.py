import math

def w_T_to_lambda3_func(w, T):
    '''分子量(g)と温度(K)を受け取って、熱的ドブロイ波長(m^3) を返します。

    Args:
        w (float): 分子量(g)
        T (float): 温度(K)

    Returns:
        浮動小数: 熱的ドブロイ波長(m^3)
    '''
    
    boltz = 1.38e-23
    avo = 6.02e+23
    pi = math.pi
    planck = 6.63e-34
    
    w *= 1.0e-3 # g --> kg 
    w /= avo
    return (planck / math.sqrt(2*pi*w*boltz*T))**3
