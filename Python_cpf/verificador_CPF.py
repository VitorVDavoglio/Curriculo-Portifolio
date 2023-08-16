#Funções
def dois_numeros():
    global cpf_final
    cpf_final = [""] * 11
    global cpf_num1
    global cpf_num2

    sum_num1 = 0 #Soma dos 9 digitos para ver o 1º numero extra
    i = 10
    for x in range(9):
        cpf_final[x] = entrada_cpf[x]
        sum_num1 = sum_num1 + (int(entrada_cpf[x]) * i)
        i = i - 1

    resto_num1 = (sum_num1 % 11) #Resto da divisão da 1º soma 

    #Pegando o resto para finalizar o 1º numero extra.
    if (resto_num1 < 2):  
        cpf_num1 = 0
    else:
        cpf_num1 = 11 - resto_num1 
    
    cpf_num1 = str(cpf_num1)
    cpf_final[9] = cpf_num1

    #COMEÇANDO O CÁLCULO DO SEGUNDO DÍGITO:

    sum_num2 = 0
    j = 11
    for x in range(10):
        sum_num2 = sum_num2 + (int(cpf_final[x]) * j)
        j = j - 1

    resto_num2 = (sum_num2 % 11)

    #Pegando o resto para finalizar o 2º numero extra.
    if (resto_num2 < 2):
        cpf_num2 = 0
    else: 
        cpf_num2 = 11 - resto_num2

    cpf_num2 = str(cpf_num2)
    cpf_final[10] = cpf_num2


def escrita_cpf(x):
    #Deixando o CPF organizado para o usuário ler.
    print("---> ", end="")
    escrita = 0
    while (escrita < 11):
        if(escrita == 3 or escrita == 6):
            print(end=".")
            print(x[escrita], end="")
        elif(escrita == 9):
            print(end="-")
            print(x[escrita], end="")
        else:
            print(x[escrita], end="")
        escrita = escrita + 1

def verifica_usuario():
    global cpf_final_usuario
    cpf_final_usuario = [""] * 11
    
    for x in range(11):
        cpf_final_usuario[x] = entrada_cpf[x]

    if (cpf_final_usuario[9] != cpf_final[9] or cpf_final_usuario[10] != cpf_final[10]):
        print("O aluno Vítor Vieira Simião Davoglio - N7483D5 informa: CPF inválido.")
    else:
        print("O aluno Vítor Vieira Simião Davoglio - N7483D5 informa: CPF válido.")
    

#Início apresentação usuário: 
resp = 1
while (resp != 0):
    resp = int(input("""Escolha uma opção: 
              [0] Para encerrar o programa
              [1] Digite o CPF sem os dígitos verificadores para calcular os dígitos
              [2] Digite o CPF completo para verificar os dígitos informados.
              ---> """))

    if (resp == 0):
        print("O aluno Vítor Vieira Simião Davoglio - N7483D5 informa: Programa encerrado com sucesso.")
        break  # Terminará o looping 

    elif (resp == 1):
        entrada_cpf = input("Digite os 9 primeiros dígitos: ")
        entrada_cpf_ok = entrada_cpf.isdigit()
        if (entrada_cpf_ok):
            if (len(entrada_cpf) < 9 ):
                print("CPF incompleto, necessário 9 caracteres.")
            elif (len(entrada_cpf) > 9):
                print("CPF incorreto para calcular dígitos, necessário 9 caracteres apenas.")
            else:
                dois_numeros()
                print("O aluno Vítor Vieira Simião Davoglio - N7483D5 informa: Os dígitos de validação para CPF informado são",cpf_num1,"e",cpf_num2,".Portanto o CPF completo é:") 
                escrita_cpf(cpf_final)
                print("")
        else:
            print("Só é aceito dígitos.")


    elif (resp == 2):
        entrada_cpf = input("Digite os 11 dígitos: ")
        entrada_cpf_ok = entrada_cpf.isdigit()
        if (entrada_cpf_ok):
            if (len(entrada_cpf) < 11):
                print("CPF incompleto, necessário 11 caracteres.")
            elif (len(entrada_cpf) > 11):
                print("CPF incorreto para verificar os dígitos, necessário 11 caracteres.")
            else:
                dois_numeros()
                verifica_usuario()
                escrita_cpf(cpf_final_usuario)
                print("")

        else:
            print("Só é aceito dígitos.")
        
    else:
        print("Opção escolhida inválida, tente novamente.")

    print("================================================")