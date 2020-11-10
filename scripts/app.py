import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
from pandas_datareader import data as pdr

import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)
import os
import datetime

# Config
alt.data_transformers.disable_max_rows()
st.beta_set_page_config(layout="wide")


# load portfolio data
# load news data





# Front Facing
st.title('Stonks')


def loadPortfolio():
    """"""
    df = pd.read_csv('../data/raw/portfolio.csv')
    stock_info = pd.DataFrame()
    stock_history = pd.DataFrame()

    for index, row in df.iterrows():
        data = yf.Ticker(row['Ticker'])
        info = pd.DataFrame([data.info])
        stock_info = pd.concat([stock_info, info])

        history = pdr.get_data_yahoo(row['Ticker'],
                                     start="2017-01-01",
                                     end=datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'),
                                     progress=False)
        history['Ticker'] = row['Ticker']
        stock_history = pd.concat([stock_history, history])

        my_bar.progress(index + 1)

    return stock_info, stock_history, df
    
my_bar = st.sidebar.progress(0)
if st.sidebar.button('load'):
    stock_info, stock_history, portfolio = loadPortfolio()


stock_info, stock_history, portfolio = loadPortfolio()





col1, col2 = st.beta_columns([3, 1])

# col1.subheader('dsafd')
#
# inst_chart = alt.Chart(inst_df, width=1200).mark_line().encode(x='DATE:T', y='CLOSE:Q')
#
# col1.altair_chart(inst_chart, use_container_width=True)
#
# st.beta_color_picker('pickme')
