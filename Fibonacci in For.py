print("\nBem vindo ao programa de calculo de fibonacci!")
quantidade = 1

while(quantidade != 0): 

    quantidade = int(input("\nDigite a quantidade que calcular ou 0 (zero) para finalizar: "))
    num1 = 0
    num2 = 1
    auxiliar = 0
    contador = 0

    print("Sequência fibonacci")
    print(quantidade, fim = " ")

   
    for i in range (quantidade - 1):  

        num1 = num2
        num2 = auxiliar
        auxiliar = num1 + num2

        print(quantidade, fim = " ")

