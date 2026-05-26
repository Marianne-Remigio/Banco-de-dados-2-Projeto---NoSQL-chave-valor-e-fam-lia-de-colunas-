from cassandra.cluster import Cluster
import uuid
from datetime import datetime


USER_ID_FIXO = uuid.UUID("11111111-1111-1111-1111-111111111111")


def conectar_cassandra():
    try:
        cluster = Cluster(["127.0.0.1"], port=9042)
        session = cluster.connect("spotify")
        print("Conectado ao keyspace 'spotify'\n")
        return cluster, session
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None, None


def adicionar_musica(session):
    title = input("Nome da música: ")
    artist = input("Artista: ")
    genre = input("Gênero: ")

    music_id = uuid.uuid4()

    session.execute(
        """
        INSERT INTO music_by_id (music_id, title, artist, genre)
        VALUES (%s, %s, %s, %s)
        """,
        (music_id, title, artist, genre)
    )

    session.execute(
        """
        INSERT INTO music_by_title (title, music_id, artist, genre)
        VALUES (%s, %s, %s, %s)
        """,
        (title, music_id, artist, genre)
    )

    print(f"Música '{title}' cadastrada com sucesso.\n")


def listar_musicas(session):
    resultado = session.execute(
        "SELECT music_id, title, artist, genre FROM music_by_id"
    )

    print("\nMúsicas cadastradas:")
    for musica in resultado:
        print(f"ID: {musica.music_id} | {musica.title} - {musica.artist} | {musica.genre}")
    print()


def buscar_musica_por_nome(session, title):
    resultado = session.execute(
        """
        SELECT music_id, title, artist, genre
        FROM music_by_title
        WHERE title = %s
        """,
        (title,)
    )

    return resultado.one()


def buscar_musica_menu(session):
    title = input("Digite o nome da música: ")
    musica = buscar_musica_por_nome(session, title)

    if musica:
        print(f"\nEncontrada: {musica.title} - {musica.artist} | Gênero: {musica.genre}")
        print(f"ID: {musica.music_id}\n")
    else:
        print("Música não encontrada.\n")


def atualizar_genero(session):
    title = input("Digite o nome da música que deseja atualizar: ")
    musica = buscar_musica_por_nome(session, title)

    if not musica:
        print("Música não encontrada.\n")
        return

    novo_genero = input("Novo gênero: ")

    session.execute(
        "UPDATE music_by_id SET genre = %s WHERE music_id = %s",
        (novo_genero, musica.music_id)
    )

    session.execute(
        "UPDATE music_by_title SET genre = %s WHERE title = %s",
        (novo_genero, title)
    )

    print("Gênero atualizado com sucesso.\n")


def deletar_musica(session):
    title = input("Digite o nome da música que deseja deletar: ")
    musica = buscar_musica_por_nome(session, title)

    if not musica:
        print("Música não encontrada.\n")
        return

    session.execute(
        "DELETE FROM music_by_id WHERE music_id = %s",
        (musica.music_id,)
    )

    session.execute(
        "DELETE FROM music_by_title WHERE title = %s",
        (title,)
    )

    print("Música deletada com sucesso.\n")


def registrar_reproducao(session):
    title = input("Digite o nome da música ouvida: ")
    musica = buscar_musica_por_nome(session, title)

    if not musica:
        print("Música não encontrada.\n")
        return

    session.execute(
        """
        INSERT INTO history_by_user (user_id, listened_at, music_id, title, artist)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (USER_ID_FIXO, datetime.now(), musica.music_id, musica.title, musica.artist)
    )

    print(f"Música '{musica.title}' registrada no histórico.\n")


def listar_historico(session):
    resultado = session.execute(
        """
        SELECT listened_at, music_id, title, artist
        FROM history_by_user
        WHERE user_id = %s
        """,
        (USER_ID_FIXO,)
    )

    print("\nHistórico de reprodução:")
    for item in resultado:
        print(f"{item.listened_at} | {item.title} - {item.artist} | ID: {item.music_id}")
    print()


def favoritar_musica(session):
    title = input("Digite o nome da música para favoritar: ")
    musica = buscar_musica_por_nome(session, title)

    if not musica:
        print("Música não encontrada.\n")
        return

    session.execute(
        """
        INSERT INTO favorites_by_user (user_id, music_id, title, artist, added_at)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (USER_ID_FIXO, musica.music_id, musica.title, musica.artist, datetime.now())
    )

    print(f"Música '{musica.title}' adicionada aos favoritos.\n")


def listar_favoritos(session):
    resultado = session.execute(
        """
        SELECT music_id, title, artist, added_at
        FROM favorites_by_user
        WHERE user_id = %s
        """,
        (USER_ID_FIXO,)
    )

    print("\nMúsicas favoritas:")
    for item in resultado:
        print(f"{item.title} - {item.artist} | Adicionada em: {item.added_at}")
    print()


def remover_favorito(session):
    title = input("Digite o nome da música para remover dos favoritos: ")
    musica = buscar_musica_por_nome(session, title)

    if not musica:
        print("Música não encontrada.\n")
        return

    session.execute(
        """
        DELETE FROM favorites_by_user
        WHERE user_id = %s AND music_id = %s
        """,
        (USER_ID_FIXO, musica.music_id)
    )

    print(f"Música '{musica.title}' removida dos favoritos.\n")


def menu(session):
    while True:
        print("1 - Adicionar música")
        print("2 - Listar músicas")
        print("3 - Buscar música pelo nome")
        print("4 - Atualizar gênero da música")
        print("5 - Deletar música")
        print("6 - Registrar música ouvida")
        print("7 - Listar histórico")
        print("8 - Favoritar música")
        print("9 - Listar favoritos")
        print("10 - Remover favorito")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_musica(session)
        elif escolha == "2":
            listar_musicas(session)
        elif escolha == "3":
            buscar_musica_menu(session)
        elif escolha == "4":
            atualizar_genero(session)
        elif escolha == "5":
            deletar_musica(session)
        elif escolha == "6":
            registrar_reproducao(session)
        elif escolha == "7":
            listar_historico(session)
        elif escolha == "8":
            favoritar_musica(session)
        elif escolha == "9":
            listar_favoritos(session)
        elif escolha == "10":
            remover_favorito(session)
        elif escolha == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    cluster, session = conectar_cassandra()

    if session:
        menu(session)
        cluster.shutdown()
