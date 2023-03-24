import dists


def a_star(start):
    distancias_inicial = dists.dists[start]
    cidades_exploradas = [start]
    distancia_percorrida = 0
    objetivo = 'Bucharest'

    return fila_prioridades(distancias_inicial, cidades_exploradas, distancia_percorrida, objetivo)


def fila_prioridades(distancias, cidades_exploradas, distancia_percorrida, objetivo):
    if not distancias:
        return 'Erro, não é possível resolver o problema'

    borda = []

    for distancia in distancias:
        if distancia[0] == objetivo:
            cidades_exploradas.append(objetivo)
            return cidades_exploradas
        fn = distancia_percorrida + distancia[1] + dists.straight_line_dists_from_bucharest[distancia[0]]
        borda.append([distancia[0], fn, distancia[1]])

    for i in borda:
        if i[0] in cidades_exploradas:
            borda.remove(i)

    prox_caminho = borda[0]

    for i in borda:
        if i[1] < prox_caminho[1]:
            prox_caminho = i

    cidades_exploradas.append(prox_caminho[0])
    distancia_percorrida = + prox_caminho[2]

    return fila_prioridades(dists.dists[prox_caminho[0]], cidades_exploradas, distancia_percorrida, objetivo)


print(a_star('Oradea'))
