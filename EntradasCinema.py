import random
import numpy as np

def funcao_filmes_em_cartaz(dicionario_filmes):
    for codigo, titulo in dicionario_filmes.items():
        print(f"{codigo} - {titulo}")

def funcao_escolher_filmes(dicionario_filmes):
    
    escolher_filme = int(input("Digite o código do filme: "))
   
    if escolher_filme in dicionario_filmes:
        filme_escolhido = dicionario_filmes[escolher_filme]
        print(f"Você escolheu o filme {filme_escolhido}")
        return filme_escolhido
    else:
        print("O código digitado está errado!")
        return None

def funcao_decisao_assento():
    decisao_do_assento = input("Você gostaria de escolher o assento? S/N ").upper()
    if decisao_do_assento == "N":
        numero_do_assento = random.randint(1, 20)
        return numero_do_assento
    
    elif decisao_do_assento == "S":
        numeros = np.arange(1, 21)
        matriz = numeros.reshape(4, 5)
        print(matriz)
        return escolher_assento(matriz)
    
    else:
        print("Opção inválida!")
        return None

def escolher_assento(matriz):
    assento = int(input("Digite o número do assento desejado: "))
    if assento in matriz:
        return assento
    
    else:
        print("Assento inválido!")
        return None

def formas_de_pagamentos(dicionario_formas_de_pagamento):

    for codigo, pagamento in dicionario_formas_de_pagamento.items():
        print(f"{codigo} - {pagamento}")

def escolher_forma_de_pagamento(dicionario_formas_de_pagamento):

    forma_de_pagamento = int(input("Digite o código referente a forma de pagamento: "))

    if forma_de_pagamento in dicionario_formas_de_pagamento:
        opcao_pagamento = dicionario_formas_de_pagamento[forma_de_pagamento]
        return opcao_pagamento

    else:
        print("Código de pagamento inválido!")
        return None


def main():
    print("QUAL FILME VOCÊ QUER ASSISTIR?")
    
    dicionario_filmes = {
        1: "Titanic",
        2: "Senhor dos Anéis",
        3: "Piratas do Caribe",
        4: "Avatar",
        5: "Mad Max"
    }
    
    funcao_filmes_em_cartaz(dicionario_filmes)
    
    filme_escolhido = funcao_escolher_filmes(dicionario_filmes)
    
    if filme_escolhido:
        assento_escolhido = funcao_decisao_assento()
        if assento_escolhido:
            print("\nDETALHE DO PEDIDO:")
            print(f"Filme: {filme_escolhido}")
            print(f"Assento: {assento_escolhido}")
            print("Valor.... R$ 30,00")
            print("\nQUAL SERÁ A FORMA DE PAGAMENTO?")
    
    dicionario_formas_de_pagamento = {
        1: "PIX",
        2: "Cartão",
        3: "Dinheiro"
    }
    formas_de_pagamentos(dicionario_formas_de_pagamento)
    opcao_pagamento = escolher_forma_de_pagamento(dicionario_formas_de_pagamento)

    if opcao_pagamento:
        print("\nRECIBO DO PEDIDO")
        print(f"Filme: {filme_escolhido}")
        print(f"Assento: {assento_escolhido}")
        print("Valor.... R$ 30,00")
        print(f"Pagamento: {opcao_pagamento}")
        print(f"TENHA UM EXCELENTE FILME!")
    else:
        print("Forma de pagamento inválida.")
        
if __name__ == "__main__":
    main()
