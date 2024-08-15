def exibir_cardapio():
    cardapio = {
        1: "Margherita",
        2: "Pepperoni",
        3: "Frango com Catupiry",
        4: "Quatro Queijos",
        5: "Calabresa"
    }
    print("Cardápio de Pizzas:")
    for chave, valor in cardapio.items():
        print(f"{chave} - {valor}")
    return cardapio


def escolher_pizza(cardapio):
    while True:
        try:
            escolha = int(input("Escolha o sabor da pizza (1-5): "))
            if escolha in cardapio:
                return cardapio[escolha], escolha
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 5.")


def definir_preco_pizza(escolha):
    if escolha == 1:
        return 25.00
    elif escolha == 2:
        return 30.00
    elif escolha == 3:
        return 28.00
    elif escolha == 4:
        return 32.00
    elif escolha == 5:
        return 27.00
    else:
        return 0.00  # Caso de escolha inválida


def exibir_ingredientes():
    # Dicionário de ingredientes com códigos
    dicionario_ingredientes = {
        'a': "Azeitona",
        'b': "Bacon",
        'c': "Cebola",
        'd': "Tomate",
        'e': "Orégano",
        'f': "Pimentão",
        'g': "Champignon"
    }
    print("Lista de Ingredientes Adicionais:")
    for codigo, ingrediente in dicionario_ingredientes.items():
        print(f"{codigo} - {ingrediente}")
    return dicionario_ingredientes


def escolher_ingredientes(dicionario_ingredientes):
    ingredientes_escolhidos = []
    preco_ingrediente = 2.00  # Preço fixo por ingrediente adicional

    print("Escolha até 3 ingredientes adicionais (Digite o código correspondente ou 'S' para sair):")
    while len(ingredientes_escolhidos) < 3:
        escolha = input(f"Escolha {len(ingredientes_escolhidos) + 1}: ").strip().lower()
        if escolha == "s":
            break
        if escolha in dicionario_ingredientes:
            ingredientes_escolhidos.append(dicionario_ingredientes[escolha])
        else:
            print("Código inválido. Tente novamente.")

    return ingredientes_escolhidos, preco_ingrediente * len(ingredientes_escolhidos)


def escolher_pagamento():
    formas_pagamento = ["Pix", "Dinheiro", "Cartão"]
    while True:
        print("Formas de pagamento:")
        for i, forma in enumerate(formas_pagamento, start=1):
            print(f"{i} - {forma}")
        try:
            escolha = int(input("Escolha a forma de pagamento (1-3): "))
            if 1 <= escolha <= 3:
                return formas_pagamento[escolha - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 3.")


def gerar_nota_fiscal(pizza, preco_pizza, ingredientes, custo_ingredientes, pagamento):
    total = preco_pizza + custo_ingredientes
    print("\n--- Nota Fiscal ---")
    print(f"Pizza escolhida: {pizza} - R$ {preco_pizza:.2f}")
    if ingredientes:
        print(f"Ingredientes adicionais: {', '.join(ingredientes)} - R$ {custo_ingredientes:.2f}")
    else:
        print("Ingredientes adicionais: Nenhum - R$ 0.00")
    print(f"Forma de pagamento: {pagamento}")
    print(f"Total: R$ {total:.2f}")
    print("-------------------\n")


# Função principal para execução do programa
def main():
    cardapio = exibir_cardapio()
    pizza, escolha_pizza = escolher_pizza(cardapio)
    preco_pizza = definir_preco_pizza(escolha_pizza)
    dicionario_ingredientes = exibir_ingredientes()
    ingredientes, custo_ingredientes = escolher_ingredientes(dicionario_ingredientes)
    pagamento = escolher_pagamento()
    gerar_nota_fiscal(pizza, preco_pizza, ingredientes, custo_ingredientes, pagamento)


# Execute a função principal
if __name__ == "__main__":
    main()
