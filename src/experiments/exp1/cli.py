from src.modules import metrics as mt
from src.modules import utils as ut
from shared.config import DATA_PATH, EXPERIMENT_PATH
import pandas as pd

def exp_values(name: str):
    """Calculates the Experimental Value of a table with [mean] and [std]"""

    df = ut.df_maker(name)
    if "mean" in df.columns and "std" in df.columns:
            result = pd.DataFrame(mt.get_exp_values(df['mean'].values, df['std'].values), columns= ['Dados Experimentais'])
            return result
    else:
         print("Não foi encotrada as tabelas [mean] e [std] em: ", name, ". Por favor, verifique a tabela!" )

def error_choice() -> str:
    """Choice a Error metrics based on the equation"""

    print("Escolha uma opção de erro baseada na equação de estudo: \n")
    print("1. Soma => w = x+-y \n")
    print("2. Multiplicação ou Divisão => w = axy ou a(y/x) \n")
    print("3. Potência (expoente constante) => w = x^m \n")
    print("4. Polinômio Misto (expoentes constantes) => w = ax^py^m \n")

    choice = input("Digite a sua escolha [1,2,3,4]: ")
    return choice


def menu():
    print("LABORATÓRIO DE FÍSICA 1 - MECÂNICA CLÁSSICA\n\n")
    print("Opções de Análise de Dados:")
    print("Lista de planilhas em data/: ", ut.list_data_dir(path = DATA_PATH))

    #Pede o DataFrame inicial
    name = input("Digite o nome do planilha de dados: ")

    #Captura o erro caso não insira corretamente a planilha
    try:
        df = ut.df_maker(name)

    except Exception as e:
        print("Planilha não indentificada: ", e, ". Por favor, verifique a tabela!")
        return None

    #Inicia a interface de interação
    while True:

        print("\n" + "=" * 50)                                              #Linha de separação do menu
        print("1. Desvio Padrão de Média\n")
        print("2. Valores Experimentais (requer [mean] e [std]): \n")
        print("3. Propagação de Erros (requer [std]) \n")
        print("q. Sair")
        print("\n" + "=" * 50)  

        #Dá a escolha de interação para o usuário baseado no menu
        option = input("Escolha uma opção [1/2/3/q]: ").strip().lower()

        #Inicia a I/O do usuário
        match option:

            case '1':
                result = mt.mean_std(df).dropna()  #######
                print(result)
                ut.csv_creater(result, path = DATA_PATH)
                    
            case '2':
                try:
                    print("Nome do arquivo com [mean] e [std]:", ut.list_data_dir(DATA_PATH))
                    file_name = input()
                    result = exp_values(file_name)
                    print(result)
                    ut.csv_creater(result, path = DATA_PATH)
                except Exception as e:
                    print("Planilha não indentificada: ", e, ". Por favor, verifique a tabela!")
                    return None
                
            case '3':
                choice = error_choice()

                match choice:

                    case '1':
                        break

            case 'q':
                print("Encerrando...")
                break
