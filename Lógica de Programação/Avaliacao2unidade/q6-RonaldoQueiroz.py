def find_top_scorer(file_path):
    top_scorer = ''
    max_goals = 0

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            name = parts[0]
            goals = sum(map(int, parts[1:]))

            if goals > max_goals:
                max_goals = goals
                top_scorer = name

    return top_scorer

if __name__ == "__main__":
    file_path = file_path = r'C:/Users/ronal/OneDrive/Área de Trabalho/Repositório/IFPE/Lógica de Programação/Avaliacao2unidade/gols.dat'  # Substitua por seu caminho de arquivo
    top_scorer = find_top_scorer(file_path)
    with open('artilheiro.dat', 'w') as output_file:
        output_file.write(top_scorer)
