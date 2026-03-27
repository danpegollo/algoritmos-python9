4. Testando Limites (Boundary Testing): Desconto em Compras
Objetivo: Identificar erros comuns de "off-by-one" (usar > em vez de >=).

Contexto: Uma loja dá 10% de desconto se a compra for de R$ 100,00 ou mais.

Função: aplicar_desconto(valor)

Atividade: O aluno deve testar três valores críticos:

99.99 (não deve ter desconto).

100.00 (deve ter desconto - aqui é onde a maioria erra a condicional).

101.00 (deve ter desconto).