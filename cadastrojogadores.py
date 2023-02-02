jogador = dict()
partidas = list()
jogador['nome'] = input('Nome do jogador: ').capitalize().strip()
total = int(input(f'Quantas partidas o {jogador["nome"]} jogou: '))
for i in range(0, total):
    partidas.append(int(input(f'      Quantos gols na partida {i}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 30)
print(jogador)
print('-' * 30)
for k, v in jogador.items():
    print(f'O {k} = {v}')
print('-' * 30)