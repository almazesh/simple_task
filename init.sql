-- Инициализация базы данных
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    caption VARCHAR(255) NOT NULL
);

-- Вставка тестовых данных
INSERT INTO items (caption) VALUES 
    ('Первая запись из init.sql'),
    ('Вторая запись из init.sql'),
    ('Третья запись из init.sql')
ON CONFLICT DO NOTHING;
