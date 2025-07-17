import streamlit as st

st.set_page_config(page_title="Einleitung",
                   layout= "wide")

st.header("🚗 Autoscout Projekt")

st.markdown("Dieses Data-Science-Projekt untersucht einen Datensatz von AutoScout24, einem europäischen Online-Marktplatz für Autos. Der Datensatz enthält verschiedene Merkmale von auf der Plattform gelisteten Gebrauchtwagen, wie z. B. Preis, Marke, Treibstoff, PS (Pferdestärke), Kilometerstand und Baujahr.")

st.subheader("Fragen:")

st.markdown("""
- Wie viele Autos wurden in verschiedenen Zeiträumen verkauft?
- Welche Automarken sind am häufigsten vertreten?
- Gibt es Korrelationen zwischen dem Preis und Eigenschaften wie PS oder Kilometerstand?
- Wie haben sich die Preise im Laufe der Jahre verändert?
- Welche Getriebearten und Treibstoff sind am beliebtesten?
""")

st.subheader("Ziel:")

st.markdown("Muster und Trends auf dem Gebrauchtwagenmarkt aufzudecken. ")