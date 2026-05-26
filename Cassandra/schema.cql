-- VERSÃO APRESENTADA

CREATE KEYSPACE spotify
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 1
};

USE spotify;

CREATE TABLE music_by_id (
    music_id UUID PRIMARY KEY,
    title TEXT,
    artist TEXT,
    genre TEXT
);

CREATE TABLE history_by_user (
    user_id UUID,
    listened_at TIMESTAMP,
    music_id UUID,
    title TEXT,
    artist TEXT,
    PRIMARY KEY (user_id, listened_at)
) WITH CLUSTERING ORDER BY (listened_at DESC);

CREATE TABLE favorites_by_user (
    user_id UUID,
    music_id UUID,
    title TEXT,
    artist TEXT,
    added_at TIMESTAMP,
    PRIMARY KEY (user_id, music_id)
);
