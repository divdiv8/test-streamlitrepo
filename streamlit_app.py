import streamlit as st
import time




# Create a list of the navigation bar items
nav_items = ["Home", "About", "Contact"]

# Create a top navigation bar
st.markdown("<nav class='navbar navbar-expand-sm navbar-light bg-light'>", unsafe_allow_html=True)
st.markdown("<a class='navbar-brand' href='/'>My App</a>", unsafe_allow_html=True)
st.markdown("<ul class='navbar-nav mr-auto'>", unsafe_allow_html=True)
for nav_item in nav_items:
  st.markdown("<li class='nav-item'><a class='nav-link' href='{}'>{}</a></li>".format(nav_item, nav_item), unsafe_allow_html=True)
st.markdown("</ul>", unsafe_allow_html=True)
st.markdown("</nav>", unsafe_allow_html=True)

# Add CSS styling
st.markdown("""
<style>
  .navbar {
    border-radius: 0;
    box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.2);
  }
  .navbar-brand {
    font-size: 1.5rem;
    font-weight: bold;
  }
  .navbar-nav li a {
    color: #333;
    font-size: 1rem;
    padding: 10px 15px;
  }
  .navbar-nav li a:hover {
    color: #fff;
    background-color: #000;
  }
</style>
""", unsafe_allow_html=True)
st.title('🎈 BTS')

st.write('Hello world!')
st.write('experimenting with this app as we learn streamlit')


with st.spinner('Wait for it...'):     #to wait while loading animation
  time.sleep(2)                       #for 10 seconds

  
# st.sidebar.header("huawei apps store：")
# st.sidebar.subheader("1.please chose which app you want to operate")

# side = st.sidebar('side')
cont = st.container() #create a container
cont.write("BTS debuted in 2013 under Big Hit Entertainment with the single album 2 Cool 4 Skool. BTS released their first Korean and Japanese-language studio albums, Dark & Wild and Wake Up respectively, in 2014. The group's second Korean studio album, Wings (2016), was their first to sell one million copies in South Korea. By 2017, BTS had crossed into the global music market and led the Korean Wave into the United States, becoming the first Korean ensemble to receive a Gold certification from the Recording Industry Association of America (RIAA) for their single \"Mic Drop\", as well as the first act from South Korea to top the Billboard 200 with their studio album Love Yourself: Tear (2018). In 2020, BTS became one of the few groups since the Beatles (in 1966–1968) to chart four US number-one albums in less than two years, with Love Yourself: Answer (2018) becoming the first Korean album certified Platinum by the RIAA; in the same year, they also became the first all-South Korean act to reach number one on both the Billboard Hot 100 and Billboard Global 200 with their Grammy-nominated single \"Dynamite\". Follow-up releases \"Savage Love\", \"Life Goes On\", \"Butter\", and ") 

st.container().write('\"Permission to Dance\" made them the fastest act to earn four US number-one singles since Justin Timberlake in 2006.As of 2022, BTS is the best-')
#write inside container
with st.sidebar: #to write inside the sidebar

  st.header("huawei apps store：")
  st.subheader("1.please chose which app you want to operate")
  st.radio('select one:',[1,2])

col1, col2,col3,col4,col5,col6 = st.columns(6) #creating columns
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



