#Questão 3

cp1 = float(input("Digite a nota do primeiro Checkpoint: "))
while cp1 > 10 or cp1 < 0:
  cp1 = float(input("Digite uma nota válida para o primeiro Checkpoint (Um número entre 0 e 10): "))

cp2 = float(input("Digite a nota do segundo Checkpoint: "))
while cp2 > 10 or cp2 < 0:
  cp2 = float(input("Digite uma nota válida para o segundo Checkpoint (Um número entre 0 e 10): "))

cp3 = float(input("Digite a nota do terceiro Checkpoint: "))
while cp3 > 10 or cp3 < 0:
  cp3 = float(input("Digite uma nota válida para o terceiro Checkpoint (Um número entre 0 e 10): "))


sp1 = float(input("Digite a nota da primeira Sprint: "))
while sp1 > 10 or sp1 < 0:
  sp1 = float(input("Digite uma nota válida para a primeira Sprint (Um número entre 0 e 10): "))

sp2 = float(input("Digite a nota da segunda Sprint: "))
while sp2 > 10 or sp2 < 0:
  sp2 = float(input("Digite uma nota válida para a segunda Sprint (Um número entre 0 e 10): "))

gs = float(input("Digite a nota da Global Solution: "))
while gs > 10 or gs < 0:
  gs = float(input("Digite uma nota válida para a Global Solution (Um número entre 0 e 10): "))

print(f'\nNota do primeiro Checkpoint: {cp1}\nNota do segundo Checkpoint: {cp2}\nNota do terceiro Checkpoint: {cp3}\nNota da primeira Sprint: {sp1}\nNota da segunda Sprint: {sp2}\nNota da Global Solution: {gs}')