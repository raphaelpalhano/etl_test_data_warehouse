import streamlit as st
import pandas as pd

def data_collect(path):
    data = pd.read_csv(path)
    data['date'] = pd.to_datetime(data['date'])
    return data
