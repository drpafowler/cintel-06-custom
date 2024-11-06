import seaborn as sns
from faicons import icon_svg
from shiny import reactive
from shiny.express import input, render, ui
from pathlib import Path
import pandas as pd

app_dir = Path(__file__).parent
df = pd.read_csv(app_dir / "gapminder_full.csv")
ui.page_opts(title="GapMinder Life Expectancy", fillable=True)


with ui.sidebar(title="Filter controls"):
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )


with ui.navset_pill(id="tab"):  
    with ui.nav_panel("A"):
        "Panel A content"

    with ui.nav_panel("B"):
        "Panel B content"

    with ui.nav_panel("C"):
        "Panel C content"

    with ui.nav_menu("Other links"):
        with ui.nav_panel("D"):
            "Page D content"

        "----"
        "Description:"
        with ui.nav_control():
            ui.a("Shiny", href="https://shiny.posit.co", target="_blank")