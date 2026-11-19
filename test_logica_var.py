from logica_var import impedimento,MEIO_CAMPO

#criei uma funcao test para testar o impedimento coloquei em uma lista pois se fosse numeros separados daria erro no sorted reverse
def test_atacante_impedimento():
    resultado = impedimento(80, [75, 100, 78.5, 60], 60, MEIO_CAMPO)
#o assert serve para usar quando algo falhar e mostrar como sairia fazendo um teste entao caso seja mentira no terminal aparece
    assert resultado == 'jogador impedido'

def test_atacante_atras_do_defensor_impedimento():
    resultado = impedimento(77,[75, 100, 78.5, 60],60, MEIO_CAMPO)
    assert resultado == 'jogador nao esta impedido'

def test_atras_da_bola():
    resultado = impedimento(80,[75, 100, 78.5, 60],85, MEIO_CAMPO)
    assert resultado == 'jogador nao esta impedido'

def test_meio_de_campo():
    resultado = impedimento(40,[100, 30, 25],20, MEIO_CAMPO)
    assert resultado == 'jogador nao esta impedido'

def test_mesma_linha():
    resultado = impedimento(78.5,[75, 100, 78.5, 60],60,MEIO_CAMPO)
    assert resultado == 'jogador nao esta impedido'

def test_goleiro_fora_gol():
    resultado = impedimento(72,[75, 70, 78.5, 60],60,MEIO_CAMPO)
    assert resultado == 'jogador nao esta impedido'

#repeti a mesma coisa do inicio com valores diferentes e situacoes diferentes apenas