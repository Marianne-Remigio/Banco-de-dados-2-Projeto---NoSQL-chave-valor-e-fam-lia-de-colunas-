-- Usuário de exemplo (Versão estendida)

INSERT INTO users_by_id (user_id, username, email)
VALUES (
    11111111-1111-1111-1111-111111111111,
    'kaio',
    'kaio@email.com'
);

-- Músicas de exemplo

INSERT INTO music_by_id (music_id, title, artist, genre)
VALUES (
    22222222-2222-2222-2222-222222222222,
    '505',
    'Arctic Monkeys',
    'Indie Rock'
);

-- (Versão estendida)

INSERT INTO music_by_title (title, music_id, artist, genre) 
VALUES (
    '505',
    22222222-2222-2222-2222-222222222222,
    'Arctic Monkeys',
    'Indie Rock'
);

INSERT INTO music_by_id (music_id, title, artist, genre)
VALUES (
    33333333-3333-3333-3333-333333333333,
    'After Dark',
    'Mr.Kitty',
    'Synthwave'
);

--(Versão estendida)

INSERT INTO music_by_title (title, music_id, artist, genre)
VALUES (
    'After Dark',
    33333333-3333-3333-3333-333333333333,
    'Mr.Kitty',
    'Synthwave'
);

-- Histórico

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
    22222222-2222-2222-2222-222222222222,
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
    33333333-3333-3333-3333-333333333333,
    'After Dark',
    'Mr.Kitty',
    toTimestamp(now())
);

-- Testes

SELECT * FROM users_by_id;

SELECT * FROM music_by_id;

SELECT * FROM music_by_title;

SELECT * FROM history_by_user;

SELECT * FROM favorites_by_user;
