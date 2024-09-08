import random
import numpy as np


def funcao_filmes_em_cartaz (dicionario_filmes):

    for codigo, titulo in dicionario_filmes.items():
        print(f"{codigo} - {titulo}")


def funcao_escolher_filmes(dicionario_filmes):

    escolher_filme = int(input("Digite o código do filme:"))

    if escolher_filme in dicionario_filmes.keys():
        filme_escolhido = dicionario_filmes[escolher_filme]
        print (f"Você escolheu o filme {filme_escolhido}")
        funcao_escolher_assento()

    else:
        print("O código digitado está errado!")

    return escolher_filme

def funcao_escolher_assento():

    decisao_do_assento = str(input("VOcê gostaria de escolher o assento? S/N ")).upper()

    if decisao_do_assento == "N":
        numero_do_assento = random.randint(1, 20)
        print(f"Seu número do assento é: {numero_do_assento}")

    elif decisao_do_assento == "S":
        numeros = np.arange(1, 21)
        matriz = numeros.reshape(4, 5)
        print(matriz)
            

def main():

    print ("QUAL FILME VOCÊ QUER ASSISTIR?")
    
    dicionario_filmes = {1: "Titanic", 
                        2: "Senhor dos Aneis",
                        3: "Piratas do Caribe",
                        4: "Avatar",
                        5: "Mad Max"}
    
    funcao_filmes_em_cartaz(dicionario_filmes)  
    escolher_filme = funcao_escolher_filmes(dicionario_filmes)

    funcao_escolher_assento()

if __name__=="__main__":

    main()