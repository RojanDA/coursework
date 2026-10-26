DROP TABLE IF EXISTS character_info;
DROP TABLE IF EXISTS ships;
DROP TABLE IF EXISTS planets;

CREATE TABLE ships (
    ship_id SERIAL PRIMARY KEY,
    ship_name TEXT NOT NULL,
    ship_type TEXT
);

INSERT INTO ships (ship_name, ship_type) VALUES
('Millennium Falcon', 'Freighter'),
('X-Wing', 'Starfighter'),
('TIE Fighter', 'Starfighter'),
('Naboo Royal Starship', 'Transport'),
('Jedi Starfighter', 'Starfighter'),
('Escape Pod', 'Utility'),
('None', NULL);

CREATE TABLE planets (
    planet_id SERIAL PRIMARY KEY,
    planet_name TEXT NOT NULL,
    region TEXT
);

INSERT INTO planets (planet_name, region) VALUES
('Tatooine', 'Outer Rim'),
('Alderaan', 'Core Worlds'),
('Naboo', 'Mid Rim'),
('Coruscant', 'Core Worlds'),
('Dagobah', 'Outer Rim'),
('Kashyyyk', 'Mid Rim'),
('Mustafar', 'Outer Rim');

CREATE TABLE character_info (
    character_id SERIAL PRIMARY KEY,
    character_name TEXT NOT NULL,
    species TEXT,
    planet_id INT REFERENCES planets(planet_id),
    ship_id INT REFERENCES ships(ship_id),
    estimated_net_worth NUMERIC(12,2),
    has_both_arms CHAR(1),
    birth_date DATE
);

INSERT INTO character_info
(character_name, species, planet_id, ship_id, estimated_net_worth, has_both_arms, birth_date)
VALUES
('Luke Skywalker', 'Human', NULL, 2, 150000.00, 'N', '1977-09-25'),
('Leia Organa', 'Human', 2, 7, 5000000.00, 'Y', '1977-09-25'),
('Han Solo', 'Human', 1, 1, 300000.00, 'Y', '1970-06-15'),
('Chewbacca', 'Wookiee', 6, 1, 180000.00, 'Y', '1810-04-02'),
('Darth Vader', 'Human', 4, 3, 10000000.00, 'N', '1966-03-12'),
('Padmé Amidala', 'Human', 3, 4, 8000000.00, 'Y', '1960-11-04'),
('Yoda', 'Unknown', 5, NULL, 50000.00, 'Y', '1125-05-01'),
('R2-D2', 'Droid', 3, 6, 2000.00, 'Y', '1995-01-01'),
('C-3PO', 'Droid', 1, 7, 1500.00, 'Y', '1990-01-01'),
('Obi-Wan Kenobi', 'Human', 4, 5, 300000.00, 'Y', '1956-03-11'),
('Darth Maul', 'Zabrak', 6, NULL, 120000.00, 'N', '1969-08-22'),
('Jar Jar Binks', 'Gungan', 3, NULL, 500.00, 'Y', '1972-02-14');