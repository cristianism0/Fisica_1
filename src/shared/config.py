import os
import pandas as pd

EXPERIMENT_PATH = 'src/experiments'
DATA_PATH = 'data/'


def list_data_dir(path= 'data/'):
    """Returns a all files in data/ directory"""
    files = [f.replace('.csv', '') for f in os.listdir(path)]
    names = ', '.join(files)
    return names
 
def df_maker(name):
    """Creates a DataFrame on data/ with a certain name"""
    return pd.read_csv("data/" + name + '.csv') 

def csv_creater(new_data, path):
    """Asks for update"""
    opt = input("Deseja criar CSV? [S/n]: ").strip().lower()
    if opt == 's':
        nome = input("Insira o nome do arquivo: ").strip()
        try:
            new_data.to_csv(path + nome + '.csv', mode='x', index=False)
            return new_data
        except Exception as e:
            print("Ops! Ocorreu um erro na geração do CSV. Tente novamente!", e)
    else:
        return None