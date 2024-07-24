def calcular_cedulas(valor):
    """Calcula a quantidade de cédulas de cada valor necessário para o saque."""
    
    cedulas = {
        50: 0,
        20: 0,
        10: 0,
        1: 0
    }
    
 
    valores_cedulas = sorted(cedulas.keys(), reverse=True)


    for valor_cedula in valores_cedulas:
        cedulas[valor_cedula], valor = divmod(valor, valor_cedula)
    
    return cedulas

def main():
    """Função principal para executar a simulação do caixa eletrônico."""
    print("Bem-vindo ao caixa eletrônico!")

    try:
        valor_saque = int(input("Digite o valor a ser sacado (número inteiro): "))
        
        if valor_saque <= 0:
            print("Valor inválido! O valor a ser sacado deve ser um número inteiro positivo.")
            return
        
    except ValueError:
        print("Valor inválido! Por favor, insira um número inteiro.")
        return

    cedulas = calcular_cedulas(valor_saque)
    
    print("\nCédulas a serem entregues:")
    for valor, quantidade in cedulas.items():
        if quantidade > 0:
            print(f"R${valor}: {quantidade} cédula(s)")
    
if __name__ == "__main__":
    main()
