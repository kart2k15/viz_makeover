import numpy as np
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from PIL import Image
import plotly.express as px
from streamlit import session_state as session


df = pd.read_csv("viz_comp.csv", sep="\t")
st.set_page_config(layout="wide")
st.title("Viz Makeover")

def get_plot(res_df):
    res_df['day'] = pd.to_datetime(res_df['day'])
    fig = px.scatter(data_frame=res_df, x="day", y="num_rats", render_mode="auto", color="Status", width=1400,
                     height=600,
                     trendline="lowess", labels={
            "day": "Date",
            "num_rats": "Rodent Complaints",
            "Status": "Complaint Status"
        }, title="NYC Sanitation Department (DSNY) performance for Rodent issues")
    tr_line = []
    for k, trace in enumerate(fig.data):
        if trace.mode is not None and trace.mode == 'lines':
            tr_line.append(k)

    cols = ["#14692a", "#060806", "#f2f5f2"]
    for i, id in enumerate(tr_line):
        fig.data[id].update(line_width=3, line_dash="longdashdot", line_color=cols[i])

    fig.update_layout(title_x=0.47, title_y=0.91, margin_r=0, margin_l=0)
    return fig

plot = get_plot(df)
st.write(plot)
st.subheader("Observations")
obs = """
* Ratio of **Closed** (blue points) to **Pending** (red points) complaints was almost 1:1 from Jan 2010 - Jun 2010. And greatly improved thereafter, hence showing DSNY's promptness to address rodent infestations
* Most rodent complaints pre-2013 were **directly put into a Pending status and then Closed**. Post 2013, it seems, most complaints were Assigned --> Pending --> Closed. Is Assigned status a **"proxy placebo"**?
"""
st.markdown(obs)
img = Image.open("rats_pic.png")
st.image(img, caption="original viz")
