import numpy as np
import pandas as pd
#import matplotlib as plt
#import seaborn as sns
#from IPython.display import display
#import joblib
import streamlit as st

# Importations des DataFrames Utiles
expresso_data = pd.read_csv('Expresso_clean_data.csv')
data_region = pd.read_csv('Encodind_and_true_names_of_region.csv')
data_top_pack = pd.read_csv('Encodind_and_true_names_of_top_pack.csv')
data_mrg = pd.read_csv('Encodind_and_true_names_of_mrg.csv')
data_tenure = pd.read_csv('Encodind_and_true_names_of_tenure.csv')

list_mrg_values =list(expresso_data['MRG'].value_counts().index[:])
list_region_values =list(expresso_data['REGION'].value_counts().index[:])
list_tenure_values =list(expresso_data['TENURE'].value_counts().index[:])
list_top_pack_values =list(expresso_data['TOP_PACK'].value_counts().index[:])

list_of_data_trues_and_enc_names = ['data_region', 'data_top_pack', 'data_mrg', 'data_tenure']
list_of_selectbox_var = ['region','top_pack','mrg' ,'tenure']

st.title('Bienvenue dans ma toute premiere App')
st.text('Merci de respecter les consignes pour obtenir une bonne prediction.')

# Création des champs text_input pour les variables
region = st.selectbox(
    label='REGION',
    options=list_region_values,
    index=None,
    placeholder='Ou etes vouis actuellement?')

tenure = st.selectbox(label='TENURE',
                      options=list_tenure_values,
                      index=None,
                      placeholder='Depuis combien de temps utiluser vous Expresso')

mrg = st.selectbox(label='Entrez la valeur de MRG',
                   options=list_mrg_values,
                   index=None)

top_pack = st.selectbox(label='Entrez la valeur de TOP_PACK',
                         options=list_top_pack_values,
                         index=None)

montant = st.number_input(label='MONTANT',
                    min_value=10,
                    max_value=500000,
                          value=None,
                    placeholder='Entrez la valeur de MONTANT')

frequence_rech = st.number_input(label='FREQUENCE_RECH',
                           min_value=1,
                           max_value=500,
                                 value=None,
                           placeholder='Entrez la valeur de FREQUENCE_RECH')

revenue = st.number_input(label='REVENUE',
                          min_value=1,
                          max_value=5500000,
                          value=None,
                          placeholder='Quel est votre revenu au cours du dernier moi')

arpu_segment = st.number_input(label='ARPU_SEGMENT',
                               min_value=1,
                               max_value=1000000,
                               value=None,
                               placeholder='Quel est votre revenu au cours des 90/3 jours')

frequence = st.number_input(label='FREQUENCE',
                            min_value=1,
                            max_value=1000000,
                            value=None,
                            placeholder='Entrez le '' nombre de fois que client à fait un revenu')

data_volume = st.number_input(label='DATA_VOLUME',
                              min_value=1,
                              max_value=1000000,
                              value=None,
                              placeholder='Entrez la valeur de DATA_VOLUME')

on_net = st.number_input(label='ON_NET',
                         min_value=1,
                         max_value=1000000,
                         value=None,
                         placeholder='Entrez la valeur de ON_NET')

orange = st.number_input(label='ORANGE',
                         min_value=1,
                         max_value=1000000,
                         value=None,
                         placeholder='Entrez la valeur de ORANGE')

tigo = st.number_input(label='TIGO',
                       min_value=1,
                       max_value=1000000,
                       value=None,
                       placeholder='Entrez la valeur de TIGO')

regularity = st.number_input(label='REGULARITY',
                             min_value=1,
                             max_value=1000000,
                             value=None,
                             placeholder='Entrez la valeur de REGULARITY')

freq_top_pack = st.number_input(label='FREQ_TOP_PACK',
                                min_value=1,
                                max_value=1000000,
                                value=None,
                                placeholder='Entrez la valeur de FREQ_TOP_PACK')

if st.button(label='Valider', type="primary"):
    indice_region = data_region['Vraies Noms'].index[data_region['Vraies Noms'] == region].tolist()[0]
    region = data_region['Noms Encodes'][indice_region]

    indice_tenure = data_tenure['Vraies Noms'].index[data_tenure['Vraies Noms'] == tenure].tolist()[0]
    tenure = data_tenure['Noms Encodes'][indice_tenure]

    indice_mrg = data_mrg['Vraies Noms'].index[data_mrg['Vraies Noms'] == mrg].tolist()[0]
    mrg = data_mrg['Noms Encodes'][indice_mrg]

    indice_top_pack = data_top_pack['Vraies Noms'].index[data_top_pack['Vraies Noms'] == top_pack].tolist()[0]
    top_pack = data_top_pack['Noms Encodes'][indice_top_pack]
    st.success('Envoi reussi')

    model =joblib.load('mon_modele_001.joblib')
    prediction = model.predict(np.array([[region, tenure, montant, frequence_rech, revenue, arpu_segment, frequence, data_volume, on_net, orange, tigo, mrg, regularity, top_pack, freq_top_pack]]))[0]
    if prediction == 0:
        st.write('Vos donnes montre que vous allez migrer vers un autre operateur ')
    else:
        st.write('Vos donnees montre que vous n\'allez pas migrer vers un autre operateur')

else:
    st.write('Appuyer pour soumettre le formulaire')
