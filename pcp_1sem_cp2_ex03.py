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

if cp1 <= cp2 and cp1 <= cp3:
  cp_nota = cp1
elif cp2 <= cp1 and cp2 <= cp3:
  cp_nota = cp2
elif cp3 <= cp1 and cp3 <= cp2:
  cp_nota = cp3


media_1 = (((cp1 + cp2 + cp3 - cp_nota + sp1 + sp2) / 4) *0.4) + gs * 0.6
print(f'\nA Nota do aluno no primeiro Semestre é: {media_1:.1f}')

media_ponderada = media_1 * 0.4
print(f'A Nota do aluno no primeiro Semestre com peso é: {media_ponderada:.1f}')