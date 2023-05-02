import streamlit as st
import time


st.title('🎈 BTS')

st.write('Hello world!')
st.write('experimenting with this app as we learn streamlit')

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


