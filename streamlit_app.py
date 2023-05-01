import streamlit as st
import time

st.title('🎈 Divya\'s test app')

st.write('Hello world!')
st.write('experimenting with this app as we learn streamlit')
with st.spinner('Wait for it...'):    
  time.sleep(10)

st.sidebar('side').title('this is inside the sidebar')

sidecont = st.container()

with st.sidebar:
  sidecont(greeting="hello")
sidecont.write('menu')
