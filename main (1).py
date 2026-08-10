while True:
    try:
        idade = int(input("Digite sua idade: "))
        print("Idade:", idade)
    except ValueError:
        print("Digite uma idade valida!")
        
    break
