from math import pow


def composto(capital, juros, tempo):
    return capital * pow((1 + juros), tempo)


def simples(capital, juros, tempo):
    return capital * (1 + juros * tempo)


capital = float(input('Qual o capital do investimento? R$ '))
juros = float(input('Qual o juros anual em porcentagem (%)? '))
meses = int(input('Quantos meses será o investimento? '))


juros = juros / 100
tempo_anos = meses / 12  


valor_final_composto = composto(capital, juros, tempo_anos)


valor_final_simples = simples(capital, juros, tempo_anos)

juros_acumulados = valor_final_composto - capital


print(f'\nMontante final com juros compostos após {meses} meses: R$ {valor_final_composto:.02f}')
print(f'Juros acumulados com juros compostos: R$ {juros_acumulados:.02f}')

print(f'\nMontante final com juros simples após {meses} meses: R$ {valor_final_simples:.02f}')
