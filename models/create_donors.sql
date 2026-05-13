-- models/create_donors.sql
CREATE OR REPLACE TABLE donors AS
SELECT *
FROM read_json_auto(
    'data/donors.json',
    columns={
        'preferred_language': 'VARCHAR',
        'donor_id': 'VARCHAR',
        'registration_date': 'TIMESTAMP',
        'acquisition_channel': 'VARCHAR',
        'email_verified': 'BOOLEAN',
        'last_login_ip': 'VARCHAR',
        'country': 'VARCHAR',
        'user_agent': 'VARCHAR'
    },
    format='newline_delimited'
);