from flask import jsonify

def dados_planalto(maxCords):
    maxCords = maxCords.split(' ')
    cordXmax = int(maxCords[0])
    cordYmax = int(maxCords[1])
    return cordXmax, cordYmax

def validar_coordenadas(cordXmax, cordYmax, cordXsonda, cordYsonda):
    return cordXsonda < cordXmax and cordYsonda < cordYmax

def validar_comandos(comandos):
    for i in comandos:
        if i != 'M' and i != 'L' and i != 'R':
            return False
    return True

def validar_direcao(direcao):
    return direcao == 'N' or direcao == 'S' or direcao == 'E' or direcao == 'W'

def validar_planalto(cordXmax, cordYmax, cordXsonda, cordYsonda):
    return cordXsonda < cordXmax or cordYsonda < cordYmax

def separar_coordenadas(cordXmax, cordYmax, cordsSonda, comandos):    
    cordsSonda = cordsSonda.split(' ')
    cordXsonda = int(cordsSonda[0])
    cordYsonda = int(cordsSonda[1])
    direcao = str(cordsSonda[2])
    direcao = direcao.upper()
    comandos = comandos.upper()

    return cordXsonda, cordYsonda, direcao, comandos

def virar_direita(direcao):
    if direcao == 'N':
        direcao = 'E'
    elif direcao == 'E':
        direcao = 'S'
    elif direcao == 'S':
        direcao = 'W'
    elif direcao == 'W':
        direcao = 'N'
    return direcao

def virar_esquerda(direcao):
    if direcao == 'N':
        direcao = 'W'
    elif direcao == 'W':
        direcao = 'S'
    elif direcao == 'S':
        direcao = 'E'
    elif direcao == 'E':
        direcao = 'N'
    return direcao

def mover_frente(direcao, cordXsonda, cordYsonda):
    if direcao == 'N':
        cordYsonda += 1
    elif direcao == 'S':
        cordYsonda -= 1
    elif direcao == 'E':
        cordXsonda += 1
    elif direcao == 'W':
        cordXsonda -= 1
    return cordXsonda, cordYsonda

def executar_comandos(comandos, cordXsonda, cordYsonda, direcao):
    for i in comandos:
        if i == 'M':
            cordXsonda, cordYsonda = mover_frente(direcao, cordXsonda, cordYsonda)
        elif i == 'L':
            direcao = virar_esquerda(direcao)
        elif i == 'R':
            direcao = virar_direita(direcao)
    return str(cordXsonda) + ' ' + str(cordYsonda) + ' ' + direcao

def main(maxCords, sondas):
    cordXmax, cordYmax = dados_planalto(maxCords)
    resultados = []
    for sonda in sondas:
        cordsSonda = sonda['cordsSonda']
        comandos = sonda['comandos']
        cordXsonda, cordYsonda, direcao, comandos = separar_coordenadas(cordXmax, cordYmax, cordsSonda, comandos)
        if not validar_coordenadas(cordXmax, cordYmax, cordXsonda, cordYsonda):
            return jsonify({'error': 'Coordenadas inválidas'})
        if not validar_comandos(comandos):
            return jsonify({'error': 'Comandos inválidos'})
        if not validar_direcao(direcao):
            return jsonify({'error': 'Direção inválida'})
        
        if not validar_planalto(cordXmax, cordYmax, cordXsonda, cordYsonda):
            return jsonify({'error': 'Sonda fora do planalto'})
        resultados.append(executar_comandos(comandos, cordXsonda, cordYsonda, direcao))
    return jsonify(resultados)
