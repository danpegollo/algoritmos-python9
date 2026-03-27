from notas import verificarNota
def test_aprovado():
    assert verificarNota(8) == "Aprovado"

def test_exame():
    assert verificarNota(5) == "Exame"

def test_reprovado():
    assert verificarNota(2) == "Reprovado"