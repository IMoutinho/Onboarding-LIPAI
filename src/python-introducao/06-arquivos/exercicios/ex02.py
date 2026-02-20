def carregar_dados_projetos(nome_arquivo):
    projetos = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            filtra_linha = linha.strip()

            if not filtra_linha:
                continue

            dados = filtra_linha.split(',')
            codigo = int(dados[0])
            titulo = dados[1]
            responsavel = dados[2]

            projeto = {
                'codigo': codigo,
                'titulo': titulo,
                'responsavel': responsavel
            }
            projetos.append(projeto)
    return tuple(projetos)


projetos = carregar_dados_projetos('s3/src/06-arquivos/exercicios/projetos.txt')
for projeto in projetos:
    print(projeto)
