import streamlit as st
import time

st.title('🎈 Divya\'s test app')

st.write('Hello world!')
st.write('experimenting with this app as we learn streamlit')
with st.spinner('Wait for it...'):    
  time.sleep(10)

  
st.sidebar.header("huawei apps store：")
st.sidebar.subheader("1.please chose which app you want to operate")

# side = st.sidebar('side')
sidecont = st.container()
sidecont.write('menu')
with st.sidebar:
  sidecont(greeting="hello")
