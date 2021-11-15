import random

def jaucejs(cilveku_saraksts):
	for i in range(len(cilveku_saraksts),1,-1):
		x = random.randrange(0,i)
		temp = cilveku_saraksts[x]
		cilveku_saraksts[x] = cilveku_saraksts[i-1]
		cilveku_saraksts[i-1] = temp
	return(cilveku_saraksts)

def grupas(cilveku_saraksts,grupu_skaits):
	sadalijums = {}
	cilveki_grupa = len(cilveku_saraksts)//grupu_skaits
	atlikums = len(cilveku_saraksts)%grupu_skaits
	if atlikums > 0:
		daudzums = cilveki_grupa+1
		atlikums -= 1
	else:
		daudzums = cilveki_grupa
	numurs = 1
	for cilveks in cilveku_saraksts:
		sadalijums[cilveks] = numurs
		daudzums -= 1
		if daudzums == 0:
			numurs += 1
			if atlikums > 0:
				daudzums = cilveki_grupa+1
				atlikums -= 1
			else:
				daudzums = cilveki_grupa

	return sadalijums

# Programma sadala dotos cilvēkus tik grupās, cik dots
dots = "Arturs,Megija,Ainārs,Daniels,Roberts,Vilis,Sintija,Alīna,Mārcis,Harijs,Nils"
grupu_skaits = 4

saraksts = dots.split(",")
print(grupas(jaucejs(saraksts),grupu_skaits))