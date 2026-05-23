-- Inserts de Exemplo

INSERT INTO music_by_id (music_id, title, artist, genre)
VALUES (uuid(), '505', 'Arctic Monkeys', 'Indie Rock');

INSERT INTO music_by_id (music_id, title, artist, genre)
VALUES (uuid(), 'After Dark', 'Mr.Kitty', 'Synthwave');

INSERT INTO music_by_id (music_id, title, artist, genre)
VALUES (uuid(), 'Sweater Weather', 'The Neighbourhood', 'Alternative');

INSERT INTO music_by_id (music_id, title, artist, genre)
VALUES (uuid(), 'Starboy', 'The Weeknd', 'R&B');

INSERT INTO music_by_id (music_id, title, artist, genre)
VALUES (uuid(), '505 Slowed', 'Arctic Monkeys', 'Slowed');

-- Para Historico

INSERT INTO history_by_user (
    user_id,
    listened_at,
    music_id,
    title,
    artist
)
VALUES (
    11111111-1111-1111-1111-111111111111,
    toTimestamp(now()),
    uuid(),
    '505',
    'Arctic Monkeys'
);

-- Favoritos

INSERT INTO favorites_by_user (
    user_id,
    music_id,
    title,
    artist,
    added_at
)
VALUES (
    11111111-1111-1111-1111-111111111111,
    uuid(),
    'After Dark',
    'Mr.Kitty',
    toTimestamp(now())
);

-- Testes

SELECT * FROM music_by_id;

SELECT * FROM history_by_user;

SELECT * FROM favorites_by_user;
