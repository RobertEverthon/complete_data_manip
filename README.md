# datamanipulation
Primeiro item da disciplina RAD com Pythom, execução de manupulação de dados, strings e exceções com python. 

# Documentação do Código

Classe LeitorCSV:

Objetivo:

Ler um arquivo CSV com estrutura específica e fornecer métodos para manipular os dados.

Atributos:

    caminho_arquivo: Caminho para o arquivo CSV.

Métodos:

    ler_dados(): Lê o arquivo CSV e retorna uma lista de objetos Registro.
    gravar_dados(dados, caminho_arquivo): Grava os dados em um arquivo CSV.
    editar_dados(dados, indice, novo_registro): Edita um registro na lista de dados.
    excluir_dados(dados, indice): Exclui um registro da lista de dados.

Classe Registro:

Objetivo:

Representar uma linha do arquivo CSV e encapsular seus dados.

Atributos:

    codigo_orgao_superior: Código do órgão superior.
    nome_orgao_superior: Nome do órgão superior.
    codigo_orgao: Código do órgão.
    nome_orgao: Nome do órgão.
    codigo_unidade_gestora: Código da unidade gestora.
    nome_unidade_gestora: Nome da unidade gestora.
    categoria_economica: Categoria econômica.
    origem_receita: Origem da receita.
    especie_receita: Espécie da receita.
    detalhamento: Detalhamento da receita.
    valor_previsto_atualizado: Valor previsto atualizado.
    valor_lancado: Valor lançado.
    valor_realizado: Valor realizado.
    percentual_realizado: Percentual realizado.
    data_lancamento: Data de lançamento.
    ano_exercicio: Ano do exercício.

Exemplos de uso:

    Ler dados do arquivo CSV:

Python

leitor = LeitorCSV("dados_transparencia.csv")
dados = leitor.ler_dados()

Use o código com cuidado.

    Gravar dados em um arquivo CSV:

Python

leitor.gravar_dados(dados, "dados_atualizados.csv")

Use o código com cuidado.

    Editar um registro:

Python

novo_registro = Registro(
    "123456",
    "Novo nome órgão superior",
    "1234",
    "Novo nome órgão",
    "5678",
    "Nova nome unidade gestora",
    "Nova categoria econômica",
    "Nova origem receita",
    "Nova espécie receita",
    "Novo detalhamento",
    "1000.00",
    "900.00",
    "800.00",
    "80.00",
    "2023-03-10",
    "2023",
)
leitor.editar_dados(dados, 1, novo_registro)

Use o código com cuidado.

    Excluir um registro:

Python

leitor.excluir_dados(dados, 2)

Use o código com cuidado.

Observações:

    Esta documentação é apenas um exemplo e pode ser extendida para atender às suas necessidades.
    Você pode adicionar descrições mais detalhadas dos métodos e atributos.
    Você pode incluir exemplos de código para ilustrar como usar a classe.

Recursos adicionais:

    Documentação Python: https://docs.python.org/3/
    Como escrever documentação: https://www.sphinx-doc.org/en/master/usage/index.html
