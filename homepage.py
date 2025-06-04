import streamlit as st
import importlib

st.set_page_config(page_title="FTI", layout="wide")

region_modules = {
    "All Regions": "main_dashboard",
    "Muscat": "Muscat",
    "Ad Dakhliyah": "Dakhliyah",
    "Ash Sharqiyah South": "South_sharqiyah",
    "Ash Sharqiyah North": "North_sharqiyah",
    "Al Wusta": "Al_wusta",
    "Al Batinah North": "North_bathinah",
    "Al Batinah South": "South_bathinah",
    "Musandam": "Musandam",
    "Adh Dhahirah": "Dhahirah",
}

# Sidebar radio selection
st.sidebar.title("🔎 Select Dashboard")
page = st.sidebar.radio("Navigation", list(region_modules.keys()),label_visibility="collapsed")

# Import and run the selected module dynamically
module_name = region_modules[page]
module = importlib.import_module(module_name)
importlib.reload(module)
module.run()
