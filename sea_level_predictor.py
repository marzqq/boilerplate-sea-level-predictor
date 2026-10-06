
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create first line of best fit using all data
    result = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years = pd.Series(range(1880, 2051))
    sea_level_predicted = (
        result.slope * years + result.intercept
    )

    plt.plot(
        years,
        sea_level_predicted
    )

    # Create second line of best fit using data from 2000 onward
    df_recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = pd.Series(range(2000, 2051))
    sea_level_predicted_recent = (
        result_recent.slope * years_recent + result_recent.intercept
    )

    plt.plot(
        years_recent,
        sea_level_predicted_recent
    )

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")

    return plt.gca()

