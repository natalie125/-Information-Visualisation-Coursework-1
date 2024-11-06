import plotly.express as px
import pandas as pd

# Read your data into a DataFrame
df = pd.read_csv('/Users/natalieleung/Desktop/IV/query_data/population.csv', header=0)

# Define a more pronounced custom color scale
color_scale = [
    (0, "rgb(255,237,160)"),    # lightest color for lowest value
    (0.5 / 100, "rgb(254,217,118)"),
    (1 / 100, "rgb(254,178,76)"),
    (5 / 100, "rgb(253,141,60)"),
    (10 / 100, "rgb(252,78,42)"),
    (20 / 100, "rgb(227,26,28)"),    # mid color for value = 50,000
    (50 / 100, "rgb(189,0,38)"),
    (100 / 100, "rgb(128,0,38)"),    # dark color for value = 100,000
]

# Create the choropleth map with the new color scale
fig = px.choropleth(df,
                    locations='Country of origin (ISO)',
                    color='Total',
                    hover_name='Country of origin',
                    color_continuous_scale=color_scale,
                    projection='natural earth',
                    title='Total Number of Refugees Moving to the United Kingdom in 2022')

# Update layout with custom coloraxis for colorbar
fig.update_layout(
    coloraxis_colorbar=dict(
        title='Total Refugees',
        titleside='right',
        tickvals=[0, 12500, 25000, 37500, 50000, 62500, 75000, 87500, 100000],
        ticktext=['0', '12.5k', '25k', '37.5k', '50k', '62.5k', '75k', '87.5k', '100k+'],
    ),
    title=dict(x=0.5, font=dict(size=14)),
    annotations=[
        dict(
            text="This map visualises the total number of refugees (including stateless and asylum seekers, etc.) relocating to the United Kingdom in 2022. Darker shades indicate higher numbers of refugees, with a notable number from countries like Iran, Albania and Ukraine.",
            xref="paper", yref="paper", x=0, y=-0.1, xanchor='left', yanchor='bottom', font=dict(size=12)
        )
    ]
)

# Show figure
fig.show()
