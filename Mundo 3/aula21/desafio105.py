# imports

print("""
|******************|
|    Desafio105    |
|******************|
""")
print("Notas dos Alunos - Analise")
print()


# Funções
def notas(* notas, sit=False):
    """
    -> Função que analisa as notas e situações de vários alunos.
    :param notas: Uma ou mais notas dos alunos (aceitando várias)
    :param sit: Indica a situação da média
    :return: Dicionário com as informações analisadas sobre a turma
    """

    retorno = dict()
    retorno["total"] = len(notas)
    retorno["maior"] = ""
    retorno["menor"] = ""
    retorno["média"] = 0

    for nota in notas:
        retorno["média"] += nota
        if retorno["maior"] == "" or retorno["maior"] < nota:
            retorno["maior"] = nota
        if retorno["menor"] == "" or retorno["menor"] > nota:
            retorno["menor"] = nota

    # Calcula a média
    retorno["média"] /= retorno["total"]

    if sit:
        if retorno["média"] < 5:
            retorno["situação"] = "RUIM"
        elif retorno["média"] < 7:
            retorno["situação"] = "RAZOÁVEL"
        elif retorno["média"] >= 7:
            retorno["situação"] = "BOA"

    return retorno


print(notas(5, 2, 6, 9, sit=True))