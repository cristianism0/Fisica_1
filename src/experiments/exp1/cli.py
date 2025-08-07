import shared.metrics as mt
import shared.config as cnf
import os
import pandas as pd


def exp_values(name: str):
    """Calculates the Experimental Value of a table with [mean] and [std]"""
    df = cnf.df_maker(name)
    if "mean" in df.columns and "std" in df.columns:
            result = pd.DataFrame(mt.get_exp_values(df['mean'].values, df['std'].values), columns= ['Dados Experimentais'])
            return result
    else:
         print("Não foi encotrada as tabelas [mean] e [std] em: ", name, ". Por favor, verifique a tabela!" )

def menu():
    print("LABORATÓRIO DE FÍSICA 1 - MECÂNICA CLÁSSICA\n\n")
    print("Opções de Análise de Dados:")
    print("Lista de planilhas em data/: ", cnf.list_data_dir(path = cnf.DATA_PATH))

    #Pede o DataFrame inicial
    name = input("Digite o nome do planilha de dados: ")

    #Captura o erro caso não insira corretamente a planilha
    try:
        df = cnf.df_maker(name)
    except Exception as e:
        print("Planilha não indentificada: ", e, ". Por favor, verifique a tabela!")
        return None

    #Inicia a interface de interação
    while True:

        print("\n" + "=" * 50)                                              #Linha de separação do menu
        print("1. Desvio Padrão de Média\n")
        print("2. Valores Experimentais (requer média e desvio padrão): \n")
        print("3. Propagação de Erros\n")
        print("q. Sair")
        print("\n" + "=" * 50)  

        #Dá a escolha de interação para o usuário baseado no menu
        option = input("Escolha uma opção [1/2/3/q]: ").strip().lower()

        match option:

            case '1':
                result = mt.mean_std(df).dropna()
                print(result)
                cnf.csv_creater(result, path = cnf.DATA_PATH)
                    
            case '2':
                print("Nome do arquivo com [mean] e [std]:", cnf.list_data_dir(cnf.DATA_PATH))
                file_name = input()
                result = exp_values(file_name)
                print(result)
                cnf.csv_creater(result, path = cnf.DATA_PATH)

            case 'q':
                print("Encerrando...")
                break
