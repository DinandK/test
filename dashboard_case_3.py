#import packages
#from multiprocessing.sharedctypes import Value
import streamlit as st
#import matplotlib.pyplot as plt
import pandas as pd
#import plotly.express as px
#import plotly.graph_objects as go
from PIL import Image
#import seaborn as sns
import streamlit.components.v1 as components

#title
st.markdown("<h1 style='text-align: center; color: grey;'>🔌Dashboard EV🔌</h1>", unsafe_allow_html=True)

#create header
components.html(
    """
        <div style="text-align: center">
            <a href="https://opendata.rdw.nl/Voertuigen/Elektrische-voertuigen/w4rt-e856" target="_blank" class="button">Link naar de gebruikte data set van de RDW🔗</a>
            </div>
    """, height= 30
)

#image
image = Image.open('HVA-logo.jpg')
st.image(image)
st.markdown("<h4 style='text-align: center; color: grey;'>Opdracht 2 gemaakt door: Jaskirat, Thijs, Maureen en Dinand</h4>", unsafe_allow_html=True)

#import dataset
ev_data = pd.read_csv('ev_app_data.csv')
ev_user = ev_data
url_data = pd.read_csv('url_data.csv',index_col=[0])
lp_data = pd.read_csv('laadpaaldata.csv', index_col=[0])


#visualisations
def display_ev_data():
    _id = 0
    see_data = st.expander('Orginele data 👇')
    with see_data:
        st.dataframe(data=ev_data)
    if st.sidebar.checkbox("Sliders menu🎚️"):
     _id = st.sidebar.slider('Aantal elektrische voertuigen', 1 , 307949, 150000)
     ev_user = ev_data[ev_data['slider_number'] <= _id]
     see_user_data = st.expander('Data na selectie👇')
     with see_user_data:
        st.dataframe(data=ev_user)
   
    #KPI's
    kpi1, kpi2 = st.columns(2)
    _max_weight = round(ev_data['Massa rijklaar'].sum()/ev_data['slider_number'].max(),1)
    if _id > 0 :
        _weight_user = round(ev_user['Massa rijklaar'].sum()/ev_user['slider_number'].max(),1)
    else  :
        _weight_user = round(ev_data['Massa rijklaar'].sum()/ev_data['slider_number'].max(),1)        
    kpi1.metric(label = "Gemiddelde massa",
           value = _weight_user,
             delta = round(_weight_user-_max_weight)) 

    _max_price = round(ev_data['Catalogusprijs'].sum()/ev_data['slider_number'].max(),1)
    if _id > 0:
        _price_user = round(ev_user['Catalogusprijs'].sum()/ev_user['slider_number'].max(),1)
    else  :
        _price_user = round(ev_data['Catalogusprijs'].sum()/ev_data['slider_number'].max(),1)
    kpi2.metric(label = "Gemiddelde catalogusprijs",
           value = _price_user,
           delta = round(_price_user-_max_price))
    
    st.write("""#####  Hier de plot\'s""")


def display_opencharge_map():
    see_data = st.expander('Orginele data 👇')
    with see_data:
        st.dataframe(data=url_data)
    if st.sidebar.checkbox("Sliders menu🎚️"):
      _id = st.sidebar.slider('Aantal elektrische voertuigen', 1 , 7877, 3800)
      url_user = url_data[url_data['slider_number'] <= _id]
      see_user_data = st.expander('Data na selectie👇')
      with see_user_data:
        st.dataframe(data=url_user)
    st.write("""#####  Hier de plot\'s""")

def display_charge_data():
    st.write("""#####  Hier de plot\'s""")
    see_data = st.expander('Orginele data 👇')
    with see_data:
        st.dataframe(data=lp_data)
    if st.sidebar.checkbox("Sliders menu🎚️"):
      _id = st.sidebar.slider('Aantal elektrische voertuigen', 1 , 10188, 5000)
      lp_user = lp_data[lp_data['slider_number'] <= _id]
      see_user_data = st.expander('Data na selectie👇')
      with see_user_data:
        st.dataframe(data=lp_user)

#side-bar + data selection
st.sidebar.write("""# Selectie menu⚙️""")
options = st.sidebar.radio('Bladzijdes📂', options=['RDW voertuigen', 'Locaties van laadpalen', 'Laadsessie\'s'])

if options == 'RDW voertuigen':
    display_ev_data()     

elif options == 'Locaties van laadpalen' :
    display_opencharge_map()
    
elif options == 'Laadsessie\'s':
    display_charge_data()
    