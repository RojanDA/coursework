CREATE TABLE character_info_extra (
    character_id SERIAL PRIMARY KEY,
    character_name TEXT NOT NULL,
    species TEXT,
    planet_id INT,
    ship_id INT,
    estimated_net_worth NUMERIC(12,2),
    has_both_arms CHAR(1),
    birth_date DATE
);

INSERT INTO character_info_extra 
(character_name, species, planet_id, ship_id, estimated_net_worth, has_both_arms, birth_date)
VALUES
('Ahsoka Tano', 'Togruta', 3, NULL, 220000.00, 'Y', '1985-10-14'),
('Mace Windu', 'Human', 4, 5, 950000.00, 'Y', '1950-02-03'),
('Rey', 'Human', 1, 2, 120000.00, 'Y', '1999-04-10'),
('Finn', 'Human', 1, NULL, 45000.00, 'Y', '1992-07-21'),
('Poe Dameron', 'Human', 2, 1, 310000.00, 'Y', '1982-03-09'),
('General Hux', 'Human', 7, NULL, 80000.00, 'Y', '1984-11-18'),
('BB-8', 'Droid', 2, 6, 5000.00, 'Y', '2014-01-01'),
('Kylo Ren', 'Human', 2, 3, 2000000.00, 'N', '1989-12-18'),
('Luke Skywalker', 'Human', NULL, 2, 150000.00, 'N', '1977-09-25');
