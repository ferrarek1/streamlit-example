from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

st.title("yasin kac senin")
dogum=st.number_input("Dogum Tarihini Giriniz")
yas=2022-dogum
st.subheader(yas)
