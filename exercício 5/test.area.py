from area import area_circulo

def test_area_valida():
    assert area_circulo(2) == 12.56  # 3.14 * 4

def test_raio_negativo():
    assert area_circulo(-3) == 0