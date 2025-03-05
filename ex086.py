"""matriz = [ [ [], [], [] ], [ [],[],[] ], [ [], [], [] ] ]
matriz[0][0].append(int(input("Digite o valor para [0, 0]: ")))
matriz[0][1].append(int(input("Digite o valor para [0, 1]: ")))
matriz[0][2].append(int(input("Digite o valor para [0, 2]: ")))
matriz[1][0].append(int(input("Digite o valor para [1, 0]: ")))
matriz[1][1].append(int(input("Digite o valor para [1, 1]: ")))      ---> Forma complicada e nada escalavel
matriz[1][2].append(int(input("Digite o valor para [1, 2]: ")))
matriz[2][0].append(int(input("Digite o valor para [2, 0]: ")))
matriz[2][1].append(int(input("Digite o valor para [2, 1]: ")))
matriz[2][2].append(int(input("Digite o valor para [2, 2]: ")))
print("--------//--------")
print(f"{matriz[0][0]}  {matriz[0][1]}  {matriz[0][2]}")
print(f"{matriz[1][0]}  {matriz[1][1]}  {matriz[1][2]}")
print(f"{matriz[2][0]}  {matriz[2][1]}  {matriz[2][2]}")"""


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um valor para [{linha}, {coluna}]: "))

for linha in range(0, 3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()