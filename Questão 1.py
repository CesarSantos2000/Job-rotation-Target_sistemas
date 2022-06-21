entrada = int(input())

fb = [0, 1]
aux = 0
i = 0
for i in range(2, entrada):
    fb.append(fb[i - 1] + fb[i - 2])
    if(fb[i] == entrada):
        print(f"o número {entrada} está presente na sequência de Fibonacci!")
        aux = 1
        exit()
if(aux == 0):
    print(f"o número {entrada} não está presente na sequência de Fibonacci!")
