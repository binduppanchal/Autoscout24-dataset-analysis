# Fazit und Einschränkungen
import streamlit as st
st.set_page_config(page_title="Fazit und Einschränkungen",
                   layout= "wide")

st.header("Fazit:")
st.markdown("- Es gibt **positive Korrelation** zwischen **'price'** und **'hp'**. Es gibt **negative Korrelation** zwischen **'mileage'** und **'year'**")

st.markdown("- Im Laufe der Jahre **steigen** die Preise.")

st.markdown("- **'Manuel'** ist sehr beliebte Gang. ")

st.markdown("- **Volkswagen, Opel, Ford, Skoda** und **Renault** sind die fünf meistverkauften Automarken.")

st.markdown("- Autos mit **Gasoline** ist sehr beliebt.")

st.markdown("___")

st.header("Einschränkungen:")

st.markdown("- **Fehlende regionale Informationen:** Da keine geografischen Daten vorlagen, konnten regionale Unterschiede bei Angebot nicht analysiert werden.")

st.markdown("- **Markenfokus:** Das Projekt konzentriert sich hauptsächlich auf die fünf meistverkauften Automarken (Volkswagen, Opel, Ford, Skoda und Renault), wodurch andere Marken außen vor bleiben.")

st.markdown("___")

st.header("Verbesserung:")

st.markdown("- **Integration regionaler Daten:** Die Berücksichtigung von geografischen Informationen würde genauere Aussagen über regionale Preisunterschiede und Nachfragetrends ermöglichen.")

st.markdown("- **Erweiterung der Datenbasis:** Durch die Einbindung zusätzlicher Datenquellen könnten mehr Automarken, Modelle oder neuere Marktdaten berücksichtigt werden.")

st.markdown("___")

st.markdown("🙏 **Vielen Dank für Ihre Aufmerksamkeit.**")