import streamlit as st
import time

st.title('🎈 Divya\'s test app')

st.write('Hello world!')
st.write('experimenting with this app as we learn streamlit')
with st.spinner('Wait for it...'):    
  time.sleep(10)

side = st.sidebar('side')
sidecont = st.container()
sidecont.write('menu')
with side:
  sidecont(greeting="hello")

