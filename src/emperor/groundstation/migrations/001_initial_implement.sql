CREATE TABLE IF NOT EXISTS satellites (
    norad_cat INTEGER UNIQUE PRIMARY KEY,
    name TEXT,
    last_update TEXT,
    update_period INTEGER DEFAULT 7200,
    expiry_period INTEGER DEFAULT 86400,
    active TEXT
)