todos_valores =[67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
estados = ["SP", "MG", "RJ", "ES", "outros"]
soma_total = 0
for i in todos_valores:
    soma_total += i
for i in range(0, 5):
    print(f"A porcentagem no faturamento total do estado de {estados[i]} foi de "
          f"{(todos_valores[i]/soma_total)*100:.2f}%")
