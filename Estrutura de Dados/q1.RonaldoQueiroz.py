estoque = (
    "banana", 15, "maçã", 16, "pêra", 10, "uva", 6,
    "melancia", 30, "cebola", 45, "alho", 12,
    "tomate", 13, "cenoura", 18, "pimentão", 4
)

def verificar_estoque(nome_fruta):
    if nome_fruta in estoque:
        quantidade = estoque[estoque.index(nome_fruta) + 1]
        return f"{quantidade}kg"
    else:
        return "falta"

def main():
    nome_fruta = input("Digite o nome da fruta, verdura ou legume: ")
    resultado = verificar_estoque(nome_fruta)
    print(resultado)

if __name__ == "__main__":
    main()