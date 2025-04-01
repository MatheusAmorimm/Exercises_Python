print("{:=^30}".format(" RB Faz Tudo "))
def area(length, width):
    total_area = length * width
    print(f"A area do seu terreno e: {total_area:.2f}m²")

leng = float(input("Qual a largura do terreno em metros? "))
wdt = float(input("Qual o comprimento em metros ? "))

area(leng, wdt)
