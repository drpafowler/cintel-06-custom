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

# Load data
app_dir = Path(__file__).parent
df = pd.read_csv(app_dir / "data" / "gapminder_full.csv")
ui.page_opts(title="GapMinder Life Expectancy", fillable=True)

# Sidebar
with ui.sidebar(title="Filter controls"):
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )

# Main content
with ui.navset_pill(id="tab"):  
    with ui.nav_panel("Data Grid"):
        "Panel A content"

    with ui.nav_panel("Bar Charts"):
        "Panel B content"

    with ui.nav_panel("Scatterplots"):
        "Panel C content"

    with ui.nav_panel("Bubble Plots"):
        "Panel D content"

    with ui.nav_panel("Maps"):
        "Map content"

    with ui.nav_menu("Other links"):
        with ui.nav_panel("E"):
            "Page E content"

        "----"
        "Description:"
        with ui.nav_control():
            ui.a("Shiny", href="https://shiny.posit.co", target="_blank")

