import streamlit as st
import time

st.title('🎈 Divya\'s test app')

st.write('Hello world!')
st.write('experimenting with this app as we learn streamlit')
st.balloons()

with st.spinner('Wait for it...'):    
  time.sleep(10)
sidecont = st.container
st.sidebar().title('this is inside the sidebar')
with st.sidebar:
  sidecont(greeting="hello")
sidecont.write('menu')
