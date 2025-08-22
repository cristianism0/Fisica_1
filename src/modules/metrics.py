import pandas as pd
import numpy as np


def calc_mean_std(data: pd.DataFrame) -> pd.DataFrame:
    """
    Lê um DataFrame e retorna um Dataframe com as colunas: [medidas, mean, std]
    """
    means = data.mean()
    stds = data.std(ddof=0)  # ddof=0 → population standart deviation (laboratory)
    df = pd.DataFrame({'mean': means, 'std': stds})
    df.index.name = "medidas"
    return df

def calc_exp_values(dataframe: pd.DataFrame, name: str) -> pd.DataFrame:
    """
    Calcula os valores experimentais: Cexp = mean - std
    """
    if "mean" not in dataframe.columns or "std" not in dataframe.columns:
        raise ValueError(f"Colunas 'mean' e 'std' não encontradas em {name}")
    
    result = pd.DataFrame({
        'Dados Experimentais': dataframe['mean'] - dataframe['std']
    }, index=dataframe.index)
    
    return result


def calc_get_exp_values(means: np.ndarray, stds: np.ndarray) -> np.ndarray:
    """
    Calcula os valores experimentais de uma equação do tipo: Cexp = C + |error|
    """
    return np.subtract(means, stds)

def calc_error_sum(oA: float, oB: float) -> float:
    """
    Calcula os valores experimentais de uma equação do tipo:: w = x+-y
    """
    return np.sqrt(oA**2 + oB**2)

def calc_error_mult_div(A, B, oA, oB, W) -> float:
    """
    Calcula os valores experimentais de uma equação do tipo:: w = axy or a(y/x)
    """
    return W * np.sqrt((oA/A)**2 + (oB/B)**2)

def calc_error_power(A, oA, W, m) -> float:
    """
    Calcula os valores experimentais de uma equação do tipo:: w = x^m
    """
    return abs(W * m * (oA/A))

def calc_error_multi_poli(A, oA, B, oB, W, m, p) -> float:
    """
    Calcula os valores experimentais de uma equação do tipo:: w = ax^py^m
    """
    return W*np.sqrt((p*(oA/A))**2 + (m*(oB/B))**2)


