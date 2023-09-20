a = int(input())
b = int(input())
c = int(input())
Maior_ab = (a+b+(abs(a-b)))/2
Maior_ab = (Maior_ab+c+(abs(Maior_ab-c)))/2

print(f"{Maior_ab:.0f} é o maior")