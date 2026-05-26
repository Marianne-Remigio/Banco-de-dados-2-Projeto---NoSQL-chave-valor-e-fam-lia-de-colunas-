from cassandra.cluster import Cluster
import uuid

def conectar_cassandra():
    try:
        cluster = Cluster(['127.0.0.1'], port=9042)
        session = cluster.connect('spotify')
        print("Conectado ao 'spotify'\n")
        return cluster, session
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None, None

def adicionar_musica(session, title, artist, genre):
    id_musica = uuid.uuid4()
    session.execute( 
        """
        INSERT INTO music_by_id (music_id, title, artist, genre)
        VALUES (%s, %s, %s, %s);
        """,
        (id_musica, title, artist, genre)
    )

    print(f"Música {title} adicionada")

def listar_musicas_cadastradas(session):
    listar = "SELECT music_id, title, artist, genre FROM music_by_id;"
    playlists = session.execute(listar)

    for playlist in playlists:
        print(f"ID: {playlist.music_id} | Songs: {playlist.title} | Artist: {playlist.artist} | Genre: {playlist.genre}")
    print("------------------------------------------------\n")

def update_song_genre(session, new_genre, id_music):
    session.execute(
        "UPDATE music_by_id SET genre = %s WHERE music_id = %s",
        (new_genre, uuid.UUID(id_music))
    )
    print(f"O gênero da música {id_music} foi atualizado para {new_genre}")

def delete_song(session, id_music):
    session.execute(
        "DELETE FROM music_by_id WHERE music_id = %s",
        (uuid.UUID(id_music),)
    )
    print(f"Música {id_music} foi removida")

def menu():
    while True:
        print("Digite 1 para adicionar uma nova música")
        print("Digite 2 para listar as músicas cadastradas")
        print("Digite 3 para atulizar o gênero da música")
        print("Digite 4 para deletar a música")
        print("Digite 0 para sair")

        escolha = input("Digite uma das alternativas acima: ")

        if escolha == "1":
            title = input("Digite o nome da música: ")
            artist = input("Digite o nome do artista da música: ")
            genre = input("Digite o gênero da música: ")
            adicionar_musica(session, title, artist, genre)
        elif escolha == "2":
            listar_musicas_cadastradas(session)
        elif escolha == "3":
            id_music = input("Digite o ID(UUID) música que quer atualizar: ")
            new_genre = input("Digite o novo gênero da música: ")
            update_song_genre(session, new_genre, id_music)
        elif escolha == "4":
            id_music = input("Digite o ID (UUID) da música que deseja deletar: ")
            delete_song(session, id_music)
        elif escolha == "0":
            break
        else:
            print("Digite algo válido")

if __name__ == "__main__":
    cluster, session = conectar_cassandra()
    
    if session:
        menu()
        cluster.shutdown()
