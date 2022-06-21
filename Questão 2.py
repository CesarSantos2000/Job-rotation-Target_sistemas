import json

maior_valor = 0
dia_maior = 0
menor_valor = 0
dia_menor = 0
soma = 0
media = 0
cont = 0
with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

for i in dados:
        if(maior_valor <= 0):
            maior_valor = i["valor"]
            menor_valor = i["valor"]
            dia_menor = i["dia"]
            dia_maior = i["dia"]
        if(i["valor"] != 0):
            cont += 1
            soma += i["valor"]
            if(i["valor"] < menor_valor):
                menor_valor = i["valor"]
                dia_menor = i["dia"]
            if(i["valor"] > maior_valor):
                maior_valor = i["valor"]
                dia_maior = i["dia"]

print(f"A média de faturamento foi de R${soma/cont:.2f}.")
print(f"O menor faturamento foi de R${menor_valor:.2f} no dia {dia_menor}.")
print(f"O maior faturamento foi de R${maior_valor:.2f} no dia {dia_maior}.")
