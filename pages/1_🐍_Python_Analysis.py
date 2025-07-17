import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Python Analysis",
                   page_icon= "🐍",
                   layout= "wide")


st.header("Python Analysis")

data = pd.read_csv("autoscout24.csv")
data.head()

for key in ["show_count", "show_marken", "show_corr", "show_veränderung", "show_gang", "show_meist", "show_fuel"]:
    if key not in st.session_state:
        st.session_state[key] = False

#Wie viele autos verkauft? Über welchen zeitraum?


st.write("1. Wie viele autos verkauft? Über welchen zeitraum?")

starting_year = st.selectbox("Geben Sie ein Anfangsjahr ab 2011 ein:", (2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021))
end_year = st.selectbox("Geben Sie ein Endjahr bis 2021 ein", (2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021))
if st.button("Klicke hier"):
    st.session_state.show_count = True
    no_of_autos = (data['year'] >= starting_year) & (data['year'] <= end_year)
    count = data[no_of_autos].shape[0]
if st.session_state.show_count:
    no_of_autos = (data['year'] >= starting_year) & (data['year'] <= end_year)
    count = data[no_of_autos].shape[0]
    st.write(f"**{count}** autos waren verkauft zwischen Jahr **{starting_year}** und **{end_year}**.")

#Welchen Marken sind erfasst?


st.write("2. Welchen Marken sind erfasst?")
if st.button("Marken"):
    st.session_state.show_marken = True
if st.session_state.show_marken:
    Marken = pd.DataFrame(data["make"].unique(), columns=["Marken"])

    st.dataframe(Marken, use_container_width= False)


# Existieren Korrelation zwischen den (numerischen) Features?

st.write("3. Existieren Korrelation zwischen den (numerischen) Features?")

if st.button("Correlation"):
    st.session_state.show_corr = True
if st.session_state.show_corr:
    corr = data[["price", "hp", "mileage", "year"]].corr()
    fig, ax = plt.subplots(figsize = (5, 5))
    heatmap = sns.heatmap(corr, ax= ax, annot= True, annot_kws= {"size": 6}, cbar= False)
    ax.tick_params(axis='x', labelsize=5)
    ax.tick_params(axis='y', labelsize=5)
    st.pyplot(fig, use_container_width= False)
    st.write("Es gibt **positive Korrelation** zwischen **'price'** und **'hp'**")

# Gibt es veränderungen über die Jahre?

st.write("4. Gibt es veränderungen über die Jahre?")
if st.button("Veränderungen"):
    st.session_state.show_veränderung = True
if st.session_state.show_veränderung:
    st.bar_chart(data=data, x="year",y = "price", x_label= "Jahr", y_label= "Preis")
    sns.barplot(data= data, x= "year", y= "price")
    st.write("**Im Laufe der Jahre steigen die Preise.**")

#Welche gear sehr beliebt ist?
st.write("5. Welche Gang sehr beliebt ist?")
if st.button("Beliebte Gang"):
    st.session_state.show_gang = True
if st.session_state.show_gang:
    fig, ax = plt.subplots(figsize=(5, 2))  
    countplot = sns.countplot(data=data, x="gear", hue="year", ax=ax)
    plt.xlabel("Gang")
    plt.ylabel("Anzahl")
    st.pyplot(fig)

#Welches Auto der Firma wird am meisten verkauft?

st.write("6. Welches Auto der Firma wird am meisten verkauft?")

if st.button("Meisten verkaufte Autos"):
    st.session_state.show_meist = True
if st.session_state.show_meist:
    no_of_autos_sold_per_company = data["make"].value_counts().reset_index()
    no_of_autos_sold_per_company.columns = ["Marke", "Anzahl der Verkäufe Autos"]
    def highlight_first_row(row):
        return ['background-color: green' if row.name == 0 or row.name == 1 or row.name == 2 or row.name == 3 or row.name == 4 else '' for _ in row]

    # Apply the styling
    styled_df = no_of_autos_sold_per_company.style.apply(highlight_first_row, axis=1)

    # Display the styled DataFrame
    st.dataframe(styled_df, use_container_width=False)

#Autos mit welche fuel ist beliebt?

st.write("7. Autos mit welche Treibstoff ist beliebt?")
if st.button("Beliebte Treibstoff"):
    st.session_state.show_fuel = True
if st.session_state.show_fuel:
    fig, ax = plt.subplots(figsize=(5, 2))  
    
    countplot_fuel = sns.countplot(data= data, x= "fuel", hue= "year", ax= ax)
    plt.xlabel("Treibstoff")
    plt.ylabel("Anzahl")
    plt.xticks(rotation=45, ha='right')  
    st.pyplot(fig)

    st.write("Autos mit **Gasoline** ist sehr beliebt.")





