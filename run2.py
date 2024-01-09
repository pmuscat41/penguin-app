import streamlit as st
import pandas as pd
import altair as alt    
import seaborn as sns
st.title('Palmer Penguins')
st.markdown('Use this streamlit app to make your own scatterplots about penguins!')
select_species= st.selectbox('What species would you like to visualize?',
['Adelie', 'Chinstrap', 'Gentoo'])  
select_x = st.selectbox('What should be the x-axis?',
['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])    
select_y = st.selectbox('What should be the y-axis?',
['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])    
penguins_df = pd.read_csv('https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv')
penguins_df = penguins_df[penguins_df['species'] == select_species]
alt_chart = alt.Chart(penguins_df,title='Palmer Penguins').mark_circle().encode( x=select_x,
 y=select_y, ).interactive()        

st.altair_chart(alt_chart,use_container_width=True  )


