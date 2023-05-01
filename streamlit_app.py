import streamlit as st
import time
import streamlit-option-menu

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
  choose = option_menu("App Gallery", ["About", "Photo Editing", "Project Planning", "Python e-Course", "Contact"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
#   st.header("huawei apps store：")
#   st.subheader("1.please chose which app you want to operate")
#   st.radio('select one:',[1,2])
  
col1, col2 = st.columns(2) #creating columns
col1.write("This is column 1")
col2.write("This is column 2")
  
