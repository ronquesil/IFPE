ddd = int(input("Digite o DDD: "))

ddd_to_capital = {
    82: "Maceió",
    71: "Salvador",
    88: "Fortaleza",
    98: "São Luís",
    83: "João Pessoa",
    81: "Recife",
    86: "Teresina",
    84: "Natal",
    79: "Aracaju"
}

print(ddd_to_capital.get(ddd, "DDD INEXISTENTE"))