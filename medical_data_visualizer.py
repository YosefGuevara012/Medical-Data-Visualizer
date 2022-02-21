import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")


# Add 'overweight' column
BMI = df["weight"] / pow(df["height"] * 0.01, 2)
df['overweight'] = [1 if i > 25 else 0 for i in BMI]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['gluc'] = [0 if i == 1 else 1 for i in df['gluc']]
df['cholesterol'] = [0 if i == 1 else 1 for i in df['cholesterol']]

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars = ["cardio"], value_vars = ['cholesterol','gluc', 'smoke', 'alco', 'active','overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = "total")

    # Draw the catplot with 'sns.catplot()'
    cat_plot = sns.catplot(x = "variable", y = "total", col = "cardio", hue = "variable", kind = "bar", data = df_cat)
    fig = cat_plot.get_figure()


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig