import streamlit as st
import pandas as pd

st.title('My first app')

st.write('## テーブル')
st.write('スパムが多い')

import streamlit as st

'''
# ウィジェット
## input box
テキストの変更もちゃんと反映される
'''

text = st.text_input('入力するよ', 'でふぉると')
st.write(text)

'''
## check box
チェックボックス
'''

if st.checkbox('ちぇっくぼっくす'):
    st.write('オンだよ')
else:
    st.write('オフだよ')

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

n = st.sidebar.number_input('n', min_value=2)

x = np.linspace(0, n*np.pi, 100)
plt.plot(x, np.sin(x))

st.pyplot()