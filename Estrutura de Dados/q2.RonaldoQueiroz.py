def main():
    n = int(input("Informe a quantidade de livros: "))
    
    livros = []
    
    for _ in range(n):
        dados_livro = input("Digite o título, autor e ano de lançamento do livro, separados por vírgula: ").split(',')
        livros.append(dados_livro)
    
    for livro in livros:
        titulo, autor, ano_lancamento = livro
        print(f"Livro {titulo} de {autor} foi publicado em {ano_lancamento}.")

if __name__ == "__main__":
    main()
