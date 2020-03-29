import math
fig = str(input("Scegli una figura tra il rettangolo(R) o il triangolo rettangolo(T)--> "))
tipo = str(input("Decidi se scegliere tra perimetro(P) o area(A) -->"))
a = int(input("Inserisci la lunghezza della base (cateto 1 per il triangolo)--> "))
b = int(input("Inserisci la lunghezza dell'altezza (cateto 2 per il triangolo)--> "))
if fig == "R":
	if tipo == "A":
		print("L'area del rettangolo è {}".format(a*b))
	else:
		print("Il perimetro del rettangolo è {}".format((a+b)*2))
else:
	if tipo == "A":
		print("L'area del triangolo rettangolo è {}".format((a*b)/2))
	else:
		print("Il perimetro del triangolo rettangolo è {}".format(a+b+math.sqrt(a**2+b**2)))
