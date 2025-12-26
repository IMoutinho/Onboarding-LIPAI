def carregar_dados_alunos(nome_arquivo):
    alunos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            filtra_linha = linha.strip()

            if not filtra_linha:
                continue

            dados = filtra_linha.split(',')
            prontuario = dados[0]
            nome = dados[1]
            email = dados[2]

            aluno = {
                'prontuario': prontuario,
                'nome': nome,
                'email': email
            }
            alunos.append(aluno)
    return tuple(alunos)


alunos = carregar_dados_alunos('s3/src/06-arquivos/exercicios/alunos.txt')
for aluno in alunos:
    print(aluno)
