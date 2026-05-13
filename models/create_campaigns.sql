-- models/create_campaigns.sql
CREATE OR REPLACE TABLE campaigns AS
SELECT * 
FROM read_parquet(
    'data/campaigns.parquet'
    );