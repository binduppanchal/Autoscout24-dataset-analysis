import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Tableau Visulization",
                   page_icon= "📈",
                   layout= "wide")

st.link_button(label= "Link zum Tableau dashboard", url= 'https://public.tableau.com/app/profile/bindu.panchal/viz/Autoscout_visulization/autoscout_visulization')

st.markdown("___")

st.image("Anzahl des Autos verkauft nach Firma und Gear.png")

st.markdown("___")

st.image("Anzahl des Autos verkauft nach Jahr und gear type.png")

st.markdown("___")

st.image("Scatterplot HP vs Price.png")

