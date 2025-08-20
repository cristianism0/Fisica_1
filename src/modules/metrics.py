import pandas as pd
import numpy as np

def mean_std(data: pd.DataFrame) -> pd.DataFrame:
    """Returns a DataFrame with mean and standard deviation for each column."""
    means = data.mean()
    stds = data.std(ddof=0)  # ddof=0 → population standart deviation (laboratory)
    df = pd.DataFrame({'mean': means, 'std': stds})
    df.index.name = "medidas"
    return df

def get_exp_values(means: np.ndarray, stds: np.ndarray) -> np.ndarray:
    """Calculates the experimental value: Cexp = C + |error|"""
    return np.subtract(means, stds)

def error_sum(oA: float, oB: float) -> float:
    """Equations like: w = x+-y"""
    return np.sqrt(oA**2 + oB**2)

def error_mult_div(A, B, oA, oB, W) -> float:
    """Equations like: w = axy or a(y/x)"""
    return W * np.sqrt((oA/A)**2 + (oB/B)**2)

def error_power(A, oA, W, m) -> float:
    """Equations like: w = x^m"""
    return abs(W * m * (oA/A))

def error_multi_poli(A, oA, B, oB, W, m, p) -> float:
    """Equations like: w = ax^py^m"""
    return W*np.sqrt((p*(oA/A))**2 + (m*(oB/B))**2)


