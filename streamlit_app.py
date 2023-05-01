import streamlit as st
import time
import streamlit_option_menu

st.title('🎈 Divya\'s test app')

st.write('Hello world!')
st.write('experimenting with this app as we learn streamlit')
with st.spinner('Wait for it...'):     #to wait while loading animation
  time.sleep(10)                       #for 10 seconds

  
# st.sidebar.header("huawei apps store：")
# st.sidebar.subheader("1.please chose which app you want to operate")

# side = st.sidebar('side')
cont = st.container() #create a container
cont.write('menu') #write inside container
with st.sidebar: #to write inside the sidebar

  st.header("huawei apps store：")
  st.subheader("1.please chose which app you want to operate")
  st.radio('select one:',[1,2])

col1, col2,col3,col4,col5,col6 = st.columns(2) #creating columns
col1.write("This is column 1")
col2.write("This is column 2")
col2.write("This is column 2")
col2.write("This is column 2")
col3.write("This is column 2")
col4.write("This is column 2")
col5.write("This is column 2")
col6.write("This is column 2")
col2.write("This is column 2")
col2.write("This is column 2")

  
