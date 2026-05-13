-- models/create_donations.sql
CREATE OR REPLACE TABLE donations AS
SELECT
    donor_id,
    donation_id,
    campaign_id,
    donation_date,
    transaction_fee,
    payment_method,
    TRY_CAST(donation_amount AS DOUBLE) AS donation_amount,
    device_type
FROM read_csv_auto(
    'data/donations.csv',
    dateformat='YYYY-MM-DD HH24:MI:SS',
    nullstr=['null', 'None', 'NA']
    );