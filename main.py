from shared.config import DATA_PATH
from src.modules import utils as ut
from src.modules import metrics as mt
import os


print("LABORATÓRIO DE FÍSICA 1 - MECÂNICA CLÁSSICA\n\n")
print("Opções de Análise de Dados:")

def ask_for_csv_creation(data):
    """Pergunta se usuário quer salvar como CSV"""
    opt = input("Deseja criar CSV? [S/n]: ").strip().lower()
    if opt == "s":
        nome = input("Insira o nome do arquivo: ").strip()
        ut.utils_csv_creater(nome, data, path=DATA_PATH)
        return True
    return False

def show_match_errors(choice):
    match choice:
        case '1':
            try:
                oA, oB = map(float, input("Insira os valores da incerteza de X e Y, use . para separar os decimais.: ").split(','))
                result= mt.calc_error_sum(oA,oB)
                ask_for_csv_creation(result)


            except Exception as e:
                print(f"Ocorreu um erro: {e}.Por favor! Tente novamente!")
                        
        case '2':
            try:
                A, B, oA, oB, W = map(float, input("Insira os valores de X, Y e da incerteza de X e Y: ").split(','))
                result = mt.calc_error_mult_div(A, B, oA, oB, W)
                ask_for_csv_creation(result)

            except Exception as e:
                print(f"Ocorreu um erro: {e}.Por favor! Tente novamente!")
                    
        case '3':
            try:
                A, oA, W, m = map(float, input("Insira os valores de: X, desvio de X, o valor previsto de W = x^y e o expoente separados por virgula: "))
                result = mt.calc_error_power(A, oA, W, m)
                ask_for_csv_creation(result)

            except Exception as e:
                print(f"Ocorreu um erro: {e}.Por favor! Tente novamente!")
                    
        case '4':
            try:
                A, B, oA, oB, W, m, p = map(float, input("Insira os valores de X, Y e da incerteza de X e Y,o valor de W, expoente de X e Y: ").split(','))
                result = mt.calc_error_multi_poli(A, oA, B, oB, W, m, p)
                ask_for_csv_creation(result)

            except Exception as e:
                print(f"Ocorreu um erro: {e}.Por favor! Tente novamente!")


def error_choice() -> str:
    """
    Escolhe uma das opções de erro:
    1 -> soma
    2 -> mult
    3 -> potencia
    4 -> poli. misto
    """

    print("Escolha uma opção de erro baseada na equação de estudo: \n")
    print("1. Soma => w = x+-y \n")
    print("2. Multiplicação ou Divisão => w = axy ou a(y/x) \n")
    print("3. Potência (expoente constante) => w = x^m \n")
    print("4. Polinômio Misto (expoentes constantes) => w = ax^py^m \n")

    choice = input("Digite a sua escolha [1,2,3,4]: ")
    return choice


def main():
    print("Lista de planilhas em data/: ", ut.utils_list_data_dir(path = DATA_PATH))

    #Pede o DataFrame inicial
    name = input("Digite o nome do planilha de dados: ")

    #Captura o erro caso não insira corretamente a planilha
    try:
        df = ut.utils_df_reader(name)
        df_columns = ut.utils_columns_extract(df)

    except Exception as e:
        print(f"Ocorreu um erro: {e}.Por favor! Tente novamente!")

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
                result = mt.calc_mean_std(df)
                print(result)
                ask_for_csv_creation(result)

                    
            case '2':
                try:
                    print("Nome do arquivo com [mean] e [std]:", ut.utils_list_data_dir(DATA_PATH))
                    file_name = input()

                    """ Checa se possui um arquivo no diretório data/ com o nome dado"""
                    if os.path.exists(os.path.join(DATA_PATH, file_name + '.csv')):
                        dataframe = ut.utils_df_reader(file_name)

                        result = mt.calc_exp_values(dataframe,file_name)

                        result.index = df_columns
                        result.index.name = "medidas"
                        print(result)
                        ask_for_csv_creation(result)
         
                        
                except Exception as e:
                    print(f"Ocorreu um erro: {e}. Por favor! Tente novamente!")
                
            case '3':
                # Escolhe o tipo de equação

                print()
                choice = error_choice()
                show_match_errors(choice)

            #Saída
            case 'q':
                print("Encerrando...")
                break
    return 0

if __name__ == "__main__":
    main()