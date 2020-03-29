fig = str(input("Decidi se scegliere tra perimetro(P) o area(A) -->"))
a = int(input("Inserisci una dimensione--> "))
b = int(input("Inserisci l'altra dimensione--> "))
if fig == A:
	print("L'area del rettangolo è {}".format(a*b))
else:
	print("Il perimetro del rettangolo è {}".format((a+b)*2)