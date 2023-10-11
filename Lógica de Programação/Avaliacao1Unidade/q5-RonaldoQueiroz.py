def dog_to_human_age(dog_age):
    if dog_age <= 2:
        human_age = dog_age * 21
    elif 3 <= dog_age <= 4:
        human_age = 42 + (dog_age - 2) * 5
    elif 5 <= dog_age <= 7:
        human_age = 52 + (dog_age - 4) * 3
    else:
        human_age = 61 + (dog_age - 7) * 2
    return human_age

dog_age = int(input("Digite a idade canina: "))
print(dog_to_human_age(dog_age))