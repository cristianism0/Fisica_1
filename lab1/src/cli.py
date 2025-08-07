import metrics as mt
import os
import pandas as pd

def up_option(new_data, path = 'lab1/data/'):
    """Asks for update"""
    opt = input("Deseja criar CSV? [S/n]: ").strip().lower()
    if opt == 's':
        nome = input("Insira o nome do arquivo: ").strip()
        new_data.to_csv(path + nome + '.csv', mode='x', index=False)
        return new_data
    else:
        return None

def list_data_dir(path='lab1/data/'):
    files = [f.replace('.csv', '') for f in os.listdir(path)]
    names = ', '.join(files)
    return names

def exp_values(name: str):
    df = mt.df_maker(name)
    try:
        if "mean" in df.columns and "std" in df.columns:
            result = pd.DataFrame(mt.get_exp_values(df['mean'].values, df['std'].values), columns='Dados Experimentais')
            return result
    except Exception as e:
        print("Não foi possível concluir a operação:", e)
        return None

def menu():
    df = mt.df_maker('lab1')
    print("LABORATÓRIO DE FÍSICA 1 - MECÂNICA CLÁSSICA\n\n")
    print("Dados atuais: \n", df, "\n")
    print("Opções de Análise de Dados:")

    print("""1. Desvio Padrão de Média\n
2. Valores Experimentais (requer média e desvio padrão)\n
3. Propagações de Error\n
q. Sair""")
    

    while True:
        option = input("Escolha uma opção [1/2/3/q]: ").strip().lower()
        match option:

            case '1':
                result = mt.mean_std(df).dropna()
                print(result)
                return up_option(result)
            
            case '2':
                print("Qual o nome do arquivo onde está localizado [mean] e [std]? ", list_data_dir())
                name = input()
                result = exp_values(name)
                print(result)
                return up_option(result)
            case 'q':
                print("Encerrando...")
                break
