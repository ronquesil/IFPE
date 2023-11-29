import random
from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init(autoreset=True)

def boas_vindas():
    print(Fore.GREEN + Style.BRIGHT + "Bem-vindo ao Brasil! Vamos explorar as belezas deste maravilhoso país.\n")

def jogo():
    perguntas_respostas = {
        "Qual é a capital do Brasil?": "Brasília",
        "Qual é a maior cidade do Brasil?": "São Paulo",
        "Qual é a famosa estátua no Rio de Janeiro?": "Cristo Redentor",
        "Qual é o maior rio do Brasil?": "Rio Amazonas",
        "Quantas praias o Brasil tem?": "Milhares"
        # Adicione mais perguntas e respostas conforme necessário
    }

    perguntas = list(perguntas_respostas.keys())
    random.shuffle(perguntas)

    pontuacao = 0

    for pergunta in perguntas:
        print(Fore.CYAN + Style.BRIGHT + pergunta)
        resposta_usuario = input(Fore.YELLOW + "Sua resposta: ")

        resposta_correta = perguntas_respostas[pergunta]

        if resposta_usuario.lower() == resposta_correta.lower():
            print(Fore.GREEN + Style.BRIGHT + "Correto!\n")
            pontuacao += 1
        else:
            print(Fore.RED + Style.BRIGHT + f"Incorreto. A resposta correta é: {resposta_correta}\n")

    print(Fore.MAGENTA + Style.BRIGHT + f"Fim do jogo! Sua pontuação é: {pontuacao}/{len(perguntas)}")

if __name__ == "__main__":
    boas_vindas()
    jogo()
