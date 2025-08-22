import os
import pandas as pd
import numpy as np

def utils_convert_to_dataframe(data):
    """
    Converte qualquer dado para DataFrame para serialização
    """
    if isinstance(data, pd.DataFrame):
        return data
    elif isinstance(data, (pd.Series, np.ndarray, list, tuple)):
        return pd.DataFrame(data)
    elif isinstance(data, (int, float, str, bool, np.float64)):
        return pd.DataFrame({'Valor': [data]})
    else:
        return pd.DataFrame({'Dado': [str(data)]})

def utils_list_data_dir(path='data/')-> str:
    """
    Retorna todos os arquivos no formato .csv do diretório data/
    retorna uma string contendo os nomes
    """
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        return "Diretório criado. Nenhum arquivo CSV encontrado."
    
    files = [f.replace('.csv', '') for f in os.listdir(path) if f.endswith('.csv')]
    names = ', '.join(files) if files else "Nenhum arquivo CSV encontrado."
    return names
 
def utils_df_reader(name, path = 'data/'):
    """
    Cria um DataFrame com um nome inserido pelo usuário
    """
    return pd.read_csv(path + name + '.csv') 

def utils_csv_creater(nome: str, new_data, path):
    """
    Cria um arquivo CSV no caminho especificado.
    Lança exceção em caso de erro.
    """
    try:
        """Converte para DF qualquer tipo de DADO"""
        df_data = utils_convert_to_dataframe(new_data)

        file_path = os.path.join(path, nome + '.csv')
        df_data.to_csv(file_path, mode='x', index=True, header=True)
        print(f"Arquivo {file_path} criado com sucesso!")
        return df_data
    
    except Exception as e:
        raise Exception(f"Ocorreu um erro na criaçaõ do arquivo: {str(e)}")
    
def utils_columns_extract(data):
    """
    Extrai as colunas de um DataFrame
    retorna uma lista contendo as colunas
    """
    columns = [column for column in data.columns]
    return columns

