def calcular_dias_para_topo():
    altura_muro = int(input())
    subida_diurna = int(input())
    descida_noturna = int(input())

    if subida_diurna >= altura_muro:
        return 1
    
    dist_efetiva_diaria = subida_diurna - descida_noturna

    dias = (altura_muro - subida_diurna) / dist_efetiva_diaria + 1

    return int(dias) if dias.is_integer() else int(dias) + 1

dias_necessarios = calcular_dias_para_topo()
print(f"{dias_necessarios}")
