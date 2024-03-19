grauA = float(input("Insira a nota do grau A:"))
grauB = float(input("Insira a nota do grau B:"))
if grauA < 0 or grauB < 0:
    print("ERRO! A nota não pode ser negativa")
else:
    grauC = (grauA * 0.3) + (grauB * 0.7)
    if grauC >= 6:
        print("Aprovado!")
    else:
        print("Necessita fazer o grau C")