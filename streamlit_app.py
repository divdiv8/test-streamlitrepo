import streamlit as st
import time

st.title('🎈 Divya\'s test app')

st.write('Hello world!')
st.write('experimenting with this app as we learn streamlit')
st.balloons()

with st.spinner('Wait for it...'):    
  time.sleep(10)

# Sample openai with streamlit
# April 2023
#--------------------------------------------------------------------------------------------------------
import os, sys
import streamlit as st
import streamlit.components.v1 as components
import numpy
import torch
import openai
import pandas
from torch import nn, optim
from torch.utils.data import DataLoader
from collections import Counter

datapath = '/home/marcbohlen/data/'
authpath = datapath + 'auth/'
authfile = 'myapi.txt'
st.title("openai prompt generation")

#--------------------------------------------------------------------------------------------------------
# Access OPENAI
# read in the OpenAI key
# import json
# import requests
# gpt_creds = authpath + authfile

# file = open(gpt_creds, 'r')
# data = file.read()
# cdata = json.loads(data)
# file.close()
# APIkey = (cdata['apikey'])
APIkey = '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'
#print('got the apikey')

import openai
openai.api_key = APIkey

# Text --------------------------------------------------------------------------------------------------
# select the text engine
this_engine = "text-davinci-003"
tokens = 256
temp = 0.75
fp = 0.52
pp = 0.5

#create the responses
start = "Create 6 numbered headlines in the style of New York Times relating to travel"
ntokens = tokens - len(start)
completions = openai.Completion.create(engine=this_engine, prompt=start, max_tokens=ntokens, frequency_penalty = fp, presence_penalty = pp,stop=["11."], temperature=temp)
response = completions.choices[0].text

#display the response
st.text(response)

# parse the response and create new texts with valid entries based on the parsed response
messages = response.split('\n')
results = []
# discard empty entries
for entry in messages:
	if(len(entry) > 2):
		results.append(entry.split('.')[-1])

tokens = 1024
rresponses = []
for r in results:
	ntokens = tokens - len(r)
	completions = openai.Completion.create(engine=this_engine, prompt=r, max_tokens=ntokens, frequency_penalty = fp, presence_penalty = pp,stop=["11."], temperature=temp)
	# add more filtering here...
	rresponses.append(completions.choices[0].text)

for item in rresponses:
	#check these items first...
	st.text(item)


# --------------------------------------------------------------------------------------------------------
