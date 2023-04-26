from csv import reader

with open("estudantes.csv", 'r', encoding='utf-8') as arquivo:
    boletim = reader(arquivo)
    for l in sorted(boletim):
        aluno = l[0]
        notas = l[1:]
        nota_em_numero = list(map(int, notas))
        maiores_notas = sorted(nota_em_numero, reverse=True)[:3]
        media = round((sum(map(lambda nota: nota if nota in maiores_notas else 0, nota_em_numero))) / 3, 2)
        print(f"Nome: {aluno} Notas: {maiores_notas} Média: {media}")
