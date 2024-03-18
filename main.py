import os

from domain.leitor_csv import LeitorCSV
from model.registro import Registro

if __name__ == '__main__':
    caminho_arquivo = "dados_transparencia.csv"
    check_file = os.path.exists(caminho_arquivo)
    if check_file:
        leitor = LeitorCSV(caminho_arquivo)
        dados = leitor.ler_dados()

        # Edita o segundo registro
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
            "2024",
        )
        leitor.editar_dados(dados, 1, novo_registro)

        # Exclui o terceiro registro
        leitor.excluir_dados(dados, 2)

        # Grava os dados atualizados
        leitor.gravar_dados(dados)