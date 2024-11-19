def calcular_aliquota_ir(dias):
    if dias <= 180:
        return 0.225
    elif 181 <= dias <= 360:
        return 0.20
    elif 361 <= dias <= 720:
        return 0.175
    else:
        return 0.15

def calcular_ir(valor, dias):
    aliquota = calcular_aliquota_ir(dias)
    valor_ir = valor * aliquota
    return valor_ir

def eh_multiplo(numero, multiplos):
    for multiplo in multiplos:
        if numero % multiplo == 0:
            return True
    return False

def calcular_valor_com_juros(valor, taxa, meses):
    valor_com_juros = valor * (1 + taxa * meses)
    return valor_com_juros

def calcular_juros_parcela(dias):
    if dias > 60:
        return 0.006
    elif dias >= 40:
        return 0.009
    elif dias >= 20:
        return 0.012
    else:
        return 0.015

def emprestimo_credito():
    valores_disponiveis = [30000, 60000, 120000]
    multiplos_permitidos = [2, 3, 5]

    print("Bem-vindo à Fintech de Crédito!")
    print("Valores disponíveis para contratação:")
    for valor in valores_disponiveis:
        print(f"R$ {valor}")

    valor_escolhido = int(input("Digite o valor escolhido: "))

    if valor_escolhido not in valores_disponiveis:
        print("Valor não disponível. Tente novamente.")
        return

    parcelas = int(input("Escolha o número de parcelas (múltiplos de 2, 3 ou 5): "))

    if not eh_multiplo(parcelas, multiplos_permitidos) or parcelas > 60:
        print("Número de parcelas inválido. Deve ser múltiplo de 2, 3 ou 5 e não pode exceder 60. Tente novamente.")
        return

    dias = parcelas * 30
    taxa_juros = calcular_juros_parcela(dias)
    valor_total_com_juros = calcular_valor_com_juros(valor_escolhido, taxa_juros, parcelas)
    valor_parcela = valor_total_com_juros / parcelas

    print(f"Você escolheu um empréstimo de R$ {valor_escolhido} em {parcelas} parcelas.")
    print(f"O valor total a pagar com juros é de: R$ {valor_total_com_juros:.2f}")
    print(f"Cada parcela será de: R$ {valor_parcela:.2f}")

# Função para realizar um investimento
def realizar_investimento(investimentos):
    tipos_investimento = {1: "CDB", 2: "LCI", 3: "LCA"}

    print("Tipos de investimento:")
    for key, value in tipos_investimento.items():
        print(f"{key} - {value}")

    tipo = int(input("Escolha o tipo de investimento: "))
    if tipo not in tipos_investimento:
        print("Tipo de investimento inválido. Tente novamente.")
        return

    valor = float(input("Informe o valor do investimento: "))
    investimento = {
        'tipo': tipo,
        'valor': valor
    }
    investimentos.append(investimento)

    print(f"Investimento de R$ {valor:.2f} em {tipos_investimento[tipo]} realizado com sucesso!")

# Função para realizar um resgate
def realizar_resgate(investimentos):
    tipos_investimento = {1: "CDB", 2: "LCI", 3: "LCA"}
    print("Tipos de investimento:")
    for key, value in tipos_investimento.items():
        print(f"{key} - {value}")

    tipo = int(input("Escolha o tipo de investimento para resgate: "))
    if tipo not in tipos_investimento:
        print("Tipo de investimento inválido. Tente novamente.")
        return

    valor_resgate = float(input("Informe o valor a ser resgatado: "))
    dias_investidos = int(input("Informe o número de dias investidos: "))

    for investimento in investimentos:
        if investimento['tipo'] == tipo and investimento['valor'] >= valor_resgate:
            valor_rendimento = valor_resgate * ((1 + 0.000455) ** dias_investidos - 1)
            rendimento_liq = valor_rendimento
            valor_ir = calcular_ir(valor_rendimento, dias_investidos)
            valor_liquido = valor_resgate + rendimento_liq - valor_ir

            investimento['valor'] -= valor_resgate
            if investimento['valor'] <= 0:
                investimentos.remove(investimento)

            print(f"Resgate realizado com sucesso!")
            print(f"Valor resgatado: R$ {valor_resgate:.2f}")
            print(f"Rendimento: R$ {rendimento_liq:.2f}")
            print(f"Imposto de renda: R$ {valor_ir:.2f}")
            print(f"Valor líquido: R$ {valor_liquido:.2f}")
            return
    print("Valor inserido não correspondente. Por favor, digite o valor correto.")

# Função principal
def main():
    investimentos = []

    while True:
        print("\nMenu de Opções:")
        print("1 - Realizar Empréstimo de Crédito")
        print("2 - Realizar Investimento")
        print("3 - Realizar Resgate")
        print("4 - Encerrar Programa")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            emprestimo_credito()
        elif opcao == 2:
            realizar_investimento(investimentos)
        elif opcao == 3:
            realizar_resgate(investimentos)
        elif opcao == 4:
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
