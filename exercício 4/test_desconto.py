from desconto import aplicar_desconto

def test_sem_desconto():
    assert aplicar_desconto(99.99) == 99.99

def test_limite_exato():
    assert aplicar_desconto(100.00) == 90.0

def test_acima_limite():
    assert aplicar_desconto(101.00) == 90.9