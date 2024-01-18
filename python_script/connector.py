import mysql.connector

conn = mysql.connector.connect (
    user='root',
    password='root',
    host='127.0.0.1',
    database='meu',
    port='3306'
)
# if conn.is_connected():
#     print("CONECTAMOS!!!")

print("Este é um jogo de Pedra Papel Tesoura:")
print("Por favor insira seu nome:")
nome_jogador = input()

while True:
    print("Insira a sua jogada (PEDRA, PAPEL, TESOURA)")
    jogador = input()

    computador = 'PEDRA'

    if jogador == computador:
        resultado = 'EMPATE'
    elif jogador == 'PAPEL':
        resultado = 'VITÓRIA'
    else:
        resultado = 'DERROTA'

    print(resultado)

    cursor = conn.cursor()
    query = f"""
        INSERT INTO contagem_jogos
            (nome_player, jogada_player, jogada_computador, resultado)
        VALUES
            ('{nome_jogador}','{jogador}','{computador}','{resultado[0]}')
    """
    cursor.execute(query)
    conn.commit()
    cursor.close()

    print("Deseja continuar jogando? (Y/N)")
    continuar = input()
    if continuar == 'N':
        break
