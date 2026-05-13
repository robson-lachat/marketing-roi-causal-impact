# analysis.py

from pathlib import Path

import duckdb
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX

# Path configuration
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database.duckdb"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def get_connection():
    return duckdb.connect(str(DB_PATH))


def analyze_ltv(con):
    print("\n--- 1. Lifetime Value (LTV) Analysis ---")
    # Calculate average LTV directly from raw data
    query = """
        SELECT AVG(total_amount) as avg_ltv
        FROM (
            SELECT donor_id, SUM(CAST(donation_amount AS DOUBLE)) as total_amount
            FROM donations
            GROUP BY donor_id
        )
    """

    avg_ltv = con.execute(query).fetchone()[0]
    # df = con.execute(query).fetchdf()
    # avg_ltv = df['avg_ltv'].iloc[0]
    print(f"💰 The average LTV per donor is: ${avg_ltv:.2f}")
    return avg_ltv


def analyze_causal_impact(con):
    print("\n--- 2. Causal Impact Analysis (Marketing Campaign) ---")

    # Extract daily data for the time series
    query = """
        SELECT
            CAST(donation_date AS DATE) as date,
            COUNT(*) as daily_donations
        FROM donations
        GROUP BY 1
        ORDER BY 1
    """
    df = con.execute(query).fetchdf()
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)

    df = df.asfreq("D").fillna(0)

    # Campaign start date (adjusted for generic context)
    campaign_start = pd.to_datetime("2024-06-01")

    # Split the data
    pre_period = df[df.index < campaign_start]
    post_period = df[df.index >= campaign_start]

    # SARIMAX model (simulating the counterfactual scenario)
    # We use a simple (1,1,1) configuration as a technical example
    model = SARIMAX(pre_period["daily_donations"], order=(1, 1, 1))
    model_fit = model.fit(disp=False)

    # Forecast what would have happened without the campaign
    forecast = model_fit.predict(start=len(pre_period), end=len(df) - 1)
    forecast.index = post_period.index

    # Impact calculation
    actual = post_period["daily_donations"]
    impact = actual - forecast
    total_added_value = impact.sum()

    print(f"Estimated Campaign Impact: +{total_added_value:.0f} donations.")

    # Professional plotting
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["daily_donations"], label="Actual Data", color="#2c3e50")
    plt.plot(
        forecast.index,
        forecast,
        label="Counterfactual Scenario (Forecast)",
        linestyle="--",
        color="#e74c3c",
    )
    plt.fill_between(
        forecast.index,
        actual,
        forecast,
        color="#2ecc71",
        alpha=0.3,
        label="Causal Impact",
    )

    plt.axvline(x=campaign_start, color="gray", linestyle=":", label="Campaign Start")
    plt.title("Marketing Campaign Impact on Donation Volume")
    plt.legend()

    # Save the chart for README use
    plot_path = OUTPUT_DIR / "causal_impact_analysis.png"
    plt.savefig(plot_path)
    print(f"✅ Chart saved to: {plot_path}")


def main():
    try:
        conn = get_connection()
        analyze_ltv(conn)
        analyze_causal_impact(conn)
        conn.close()
    except Exception as e:
        print(f"❌ Analysis error: {e}")


if __name__ == "__main__":
    main()
