MEIO_CAMPO = 52.5

#criei uma def para definir o impedimento 
#O primeiro if atacante estiver a frete do defensor sera impedimento,segundo if atacante passar da bola impedimento e se jogador estiver a frente do meio campo esta impedido
#ANTES DE CRIAR A NOVA FUNCAO

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#APOS CRIAR A NOVA FUNCAO

#Apos criar a def descobrir_penultimo_defensor coloquei ela dentro do impedimento para já comparar o primeiro indice da minha lista que seria o penultimo defensor 
#quando eu criei a variavel defensor ja aproveitei para colocar ela dentro do meu if 
def impedimento(atacante, defensores,bola, meio_campo):
    penultimo_defensor = descobrir_penultimo_defensor(defensores)
    if atacante > penultimo_defensor and atacante > bola and atacante > meio_campo:
        return('jogador impedido')  
    else:
        return('jogador nao esta impedido')

#criei uma funcao para sortear uma lista de defensores comecando do maior para o menor e falei que o indice 1 da minha lista seria o penultimo jogador
#receber a lista e retornar o penultimo defensor 
def descobrir_penultimo_defensor(defensores):
        jogadores_ordenados = sorted(defensores, reverse=True)
        return(jogadores_ordenados[1])

if __name__ == "__main__":
    print(impedimento(80, [75, 100, 78.5, 60], 60, MEIO_CAMPO))
    print(impedimento(77, [75, 100, 78.5, 60], 60, MEIO_CAMPO))
    print(impedimento(72, [75, 70, 78.5, 60], 60, MEIO_CAMPO))
