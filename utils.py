import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load the data from the csv file
def load_data(file):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file (str): The path to the CSV file.

    Returns:
    DataFrame: The loaded data.
    """
    df = pd.read_csv(file)
    return df

def tidy_data(df):
    """
    Transform the DataFrame from wide to long format.

    Parameters:
    df (DataFrame): The original DataFrame.

    Returns:
    DataFrame: The transformed DataFrame in long format.
    """
    melted_df = pd.melt(df, id_vars="Year", var_name="Country", value_name="GDP")
    return melted_df


def line_plot(df, x: str, y:str, hue:str, title:str):
    """
    Create a line plot using seaborn.

    Parameters:
    df (DataFrame): The data for plotting.
    x (str): The column name to be used for the x-axis.
    y (str): The column name to be used for the y-axis.
    hue (str): The column name to be used for color encoding.
    title (str): The title of the plot.

    Returns:
    None
    """
    ax = sns.lineplot(data=df, x=x, y=y, hue=hue)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title(title)
    plt.show()
    return None

def pct_change_graph(df, x:str, hue:str, title:str):
    """
    Create a line plot of the percentage change in GDP.

    Parameters:
    df (DataFrame): The data for plotting.
    x (str): The column name to be used for the x-axis.
    hue (str): The column name to be used for color encoding.
    title (str): The title of the plot.

    Returns:
    None
    """
    df["GDP Growth"] = df.groupby("Country")["GDP"].pct_change()
    df.dropna(inplace=True)
    ax = sns.lineplot(data=df, x=x, y=df["GDP Growth"], hue=hue)
    sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
    plt.title(title)
    plt.show()
    return None

def indexed_graph(df, x:str, hue:str, title:str):
    """
    Create a line plot of the indexed GDP.

    Parameters:
    df (DataFrame): The data for plotting.
    x (str): The column name to be used for the x-axis.
    hue (str): The column name to be used for color encoding.
    title (str): The title of the plot.

    Returns:
    None
    """
    indexed_value = df.groupby('Country')["GDP"].apply(lambda x: (x / x.iloc[0]) * 100).reset_index(level=0, drop=True)
    df["Indexed GDP"] = indexed_value
    sns.lineplot(data=df, x=x, y="Indexed GDP", hue=hue)
    plt.title(title)
    plt.show()
    return None