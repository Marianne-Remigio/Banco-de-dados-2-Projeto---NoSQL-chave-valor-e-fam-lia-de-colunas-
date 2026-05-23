# Cassandra - Projeto Spotify

Pasta contendo os arquivos usados pela equipe para criar a estrutura do banco de dados CASSANDRA utilizado neste projeto
## Banco escolhido
Apache Cassandra, um banco NoSQL baseado em família de colunas.

## Como subir o Cassandra com Docker
Baixar a imagem:

```
docker pull cassandra:latest

Criar e iniciar o container:

docker run --name cassandra-db -p 9042:9042 -d cassandra

Verificar os logs:

docker logs -f cassandra-db

Entra no Cassandra

docker exec -it cassandra-db cqlsh

Como criar o banco

Dentro do cqlsh, execute os comandos do arquivo: schema.cql
Esse arquivo vai criar as seguintes coisas:

keyspace spotify
tabela music_by_id
tabela history_by_user
tabela favorites_by_user
Conferir se deu certo
USE spotify;
DESCRIBE TABLES;

e ai vamos ter essas 3 tabelas
favorites_by_user  history_by_user  music_by_id

Para testar os dados temos: (tambem disponiveis em 'seed.sql')
SELECT * FROM music_by_id;
SELECT * FROM history_by_user;
SELECT * FROM favorites_by_user;
