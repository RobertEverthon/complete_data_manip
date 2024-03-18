"""Contains the Leitor CSV actions."""
import csv

from model.registro import Registro


class LeitorCSV:
    """Leitor CSV Class."""
    def __init__(self, caminho_arquivo):
        """Initialize um Leitor CSV.

        :param caminho_arquivo: caminho do arquivo
        """
        self.caminho_arquivo = caminho_arquivo

    def ler_dados(self):
        """Ler dados do arquivo csv.

        :returns dados: dados do arquivo csv
        """
        with open(self.caminho_arquivo, "r", encoding="latin-1") as arquivo:
            leitor = csv.reader(arquivo, delimiter=";")

            # Ignora cabeçalho
            next(leitor, None)

            dados = []
            for linha in leitor:
                # Cria um objeto Registro com os campos da linha
                registro = Registro(
                    linha[0],
                    linha[1],
                    linha[2],
                    linha[3],
                    linha[4],
                    linha[5],
                    linha[6],
                    linha[7],
                    linha[8],
                    linha[9],
                    linha[10],
                    linha[11],
                    linha[12],
                    linha[13],
                    linha[14],
                    linha[15],
                )

                dados.append(registro)

        return dados

    def gravar_dados(self, dados):
        """
        Grava os dados em um arquivo CSV.

        Args:
            dados: Lista de objetos `Registro`.
        """

        with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")

            # Escreve cabeçalho
            escritor.writerow([
                "CODIGO_ORGAO_SUPERIOR",
                "NOME_ORGAO_SUPERIOR",
                "CODIGO_ORGAO",
                "NOME_ORGAO",
                "CODIGO_UNIDADE_GESTORA",
                "NOME_UNIDADE_GESTORA",
                "CATEGORIA_ECONOMICA",
                "ORIGEM_RECEITA",
                "ESPECIE_RECEITA",
                "DETALHAMENTO",
                "VALOR_PREVISTO_ATUALIZADO",
                "VALOR_LANCADO",
                "VALOR_REALIZADO",
                "PERCENTUAL_REALIZADO",
                "DATA_LANCAMENTO",
                "ANO_EXERCICIO",
            ])

            # Escreve os dados
            for registro in dados:
                escritor.writerow([
                    registro.codigo_orgao_superior,
                    registro.nome_orgao_superior,
                    registro.codigo_orgao,
                    registro.nome_orgao,
                    registro.codigo_unidade_gestora,
                    registro.nome_unidade_gestora,
                    registro.categoria_economica,
                    registro.origem_receita,
                    registro.especie_receita,
                    registro.detalhamento,
                    registro.valor_previsto_atualizado,
                    registro.valor_lancado,
                    registro.valor_realizado,
                    registro.percentual_realizado,
                    registro.data_lancamento,
                    registro.ano_exercicio,
                ])

    @staticmethod
    def editar_dados(dados, indice, novo_registro):
        """
        Edita um registro na lista de dados.

        Args:
            dados: Lista de objetos `Registro`.
            indice: Índice do registro a ser editado.
            novo_registro: Novo objeto `Registro` com os dados atualizados.
        """

        dados[indice] = novo_registro

    @staticmethod
    def excluir_dados(dados, indice):
        """
        Exclui um registro da lista de dados.

        Args:
            dados: Lista de objetos `Registro`.
            indice: Índice do registro a ser excluído.
        """

        del dados[indice]
