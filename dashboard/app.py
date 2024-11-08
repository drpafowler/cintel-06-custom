import seaborn as sns
from shiny import reactive
from shiny.express import input, render, ui
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from shinywidgets import render_widget



# Load data
app_dir = Path(__file__).parent
df = pd.read_csv(app_dir / "data" / "gapminder_full.csv")
ui.page_opts(title="GapMinder Life Expectancy", fillable=True)

# filter data
@reactive.calc
def filtered_data():
    filt_df=df[df['continent'].isin(input.continent())]
    filt_df=filt_df[filt_df['country'].isin(input.country())]
    filt_df=filt_df[filt_df['year'].between(input.year()[0], input.year()[1])]

    return filt_df

# Sidebar
with ui.sidebar(title="Filters"):
    ui.input_checkbox_group("continent", "Continent", ["Asia", "Africa", "Europe", "Americas", "Oceania"], selected=["Asia", "Africa", "Europe", "Americas", "Oceania"])
    unique_countries = df['country'].unique().tolist()
    ui.input_select("country", "Country", unique_countries, multiple=True, selected=unique_countries)
    ui.input_slider("year", "Year", min=1952, max=2007, value=[1952, 2007], step=1)
    ui.input_select("xaxis", "X-axis", ["population", "year", "life_exp", "gdp_cap"], selected="year")
    ui.input_select("yaxis", "Y-axis", ["population", "year", "life_exp", "gdp_cap"], selected="life_exp")
    ui.input_select("hue", "Hue", ["population", "year", "life_exp", "gdp_cap", "continent"], selected="population")
    ui.input_dark_mode(mode="light")
# Main content
with ui.navset_pill(id="tab"):  

    with ui.nav_panel("Data Grid"):

        @render.data_frame
        def data_grid():
            columns_to_show = [col for col in filtered_data().columns if col != 'iso_alpha']
            return render.DataGrid(filtered_data()[columns_to_show], filters=True)

    with ui.nav_panel("Bar Charts"):

        @render_widget
        def plotly_barchart():
            fig = px.bar(
                filtered_data(),
                x=input.xaxis(),
                y=input.yaxis(),
                color=input.hue(),
                hover_data=["country"],
                title="Interactive Bar Chart"
            )
            return fig
    with ui.nav_panel("Scatterplots"):

        @render_widget
        def plotly_scatter():
            fig = px.scatter(
            filtered_data(),
            x=input.xaxis(),
            y=input.yaxis(),
            color=input.hue(),
            title="Interactive Scatter Plot"
            )
            return fig
    with ui.nav_panel("Bubble Plots"):
        ui.input_select("size", "Size Variable", ["population", "year", "life_exp", "gdp_cap"], selected="population")
        ui.input_slider("size_scale", "Size Scale", min=1, max=100, value=10, step=1)
        @render_widget
        def plotly_bubble():
            fig = px.scatter(
                filtered_data(),
                x=input.xaxis(),
                y=input.yaxis(),
                color=input.hue(),
                size=input.size(),
                size_max=input.size_scale(),
                title="Interactive Bar Chart"
            )
            return fig
    with ui.nav_panel("Maps"):
        @render_widget
        def plotly_map():
            fig = px.choropleth(
                filtered_data(),
                locations="iso_alpha",
                color=input.hue(),
                title="Interactive Map",
                projection="equirectangular"
            )
            return fig
    with ui.nav_panel("Statistics"):
        @render_widget
        def plotly_heatmap():
            columns_of_interest = ['gdp_cap', 'life_exp', 'population']
            corr = filtered_data()[columns_of_interest].corr()
            fig = px.imshow(
                corr,
                text_auto=True,
                title="Correlation Heatmap"
            )
            return fig


