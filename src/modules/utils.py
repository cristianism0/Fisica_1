import os
import pandas as pd

def utils_list_data_dir(path= 'data/')-> str:
    """
    Retorna todos os arquivos no formato .csv do diretório data/
    retorna uma string contendo os nomes
    """
    files = [f.replace('.csv', '') for f in os.listdir(path)]
    names = ', '.join(files)
    return names
 
def utils_df_maker(name):
    """
    Cria um DataFrame com um nome inserido pelo usuário
    """
    return pd.read_csv("data/" + name + '.csv') 

def utils_csv_creater(nome: str, new_data: pd.DataFrame, path):
    """
    Cria um arquivo CSV no caminho especificado.
    Lança exceção em caso de erro.
    """
    try:
        file_path = os.path.join(path, nome + '.csv')
        new_data.to_csv(file_path, mode='x', index=True, header=True)
        return new_data
    except:
        raise Exception(f"Ocorreu um erro na criaçaõ do arquivo: {Exception}")
    
def utils_columns_extract(data):
    """
    Extrai as colunas de um DataFrame
    retorna uma lista contendo as colunas
    """
    columns = [column for column in data.columns]
    return columns

