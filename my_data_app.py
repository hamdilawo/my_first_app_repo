import streamlit as st
import pandas as pd


#st.markdown("<h1 style='text-align: center; color: black;'>MY DATA APP</h1>", unsafe_allow_html=True)
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #e0f7fa;  /* Arrière-plan en bleu clair */
#     }
#     .stButton>button {
#         background-color: #0078ff;  /* Bouton en bleu */
#         color: white;
#     }
#     </style>,
#     unsafe_allow_html=True
#     """)
# st.markdown("""
# This app allows you to download scraped data on motocycles from expat-dakar 
# * **Python libraries:** base64, pandas, streamlit
# * **Data source:** [Expat-Dakar](https://www.expat-dakar.com/).
# """)


# Fonction de loading des données
def load_(dataframe, title, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(title,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 12;
    height: 3em;
    width: 25em;
}</style>''', unsafe_allow_html=True)
        
        # Modifier le style d'affichage sur Streamlit
# st.markdown("""
#     <style>
#     .main {
#         background-color: #f5f5f5;
#         padding: 20px;
#         border-radius: 10px;
#     }
#     .stButton>button {
#         background-color: #4CAF50;
#         color: white;
#         border: none;
#         border-radius: 5px;
#         padding: 10px 20px;
#         text-align: center;
#         text-decoration: none;
#         display: inline-block;
#         font-size: 16px;
#         margin: 4px 2px;
#         cursor: pointer;
#     }
#     </style>
#     """, unsafe_allow_html=True)
# Charger les données 
load_(pd.read_csv('data/motos_scooters1.csv'), 'scraper des données suivant plusieurs pages', '1')
load_(pd.read_csv('data/motos_scooters2.csv'), 'Motocycles data 2', '2')
load_(pd.read_csv('data/motos_scooters3.csv'), 'Motocycles data 3', '3')
load_(pd.read_csv('data/motos_scooters4.csv'), 'Motocycles data 4', '4')
load_(pd.read_csv('data/motos_scooters5.csv'), 'Motocycles data 5', '5')




 


