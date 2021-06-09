import streamlit as st
import pandas as pd
import numpy as np


### Configuration
st.set_page_config(
    page_title = 'Modify Dashboard',
    layout='wide',
    page_icon='💹',
    # theme='Dark',
)


### Top Row
st.markdown('## Main KPIs')

first_kpi, second_kpi, third_kpi = st.beta_columns(3)

with first_kpi:
    st.markdown('**First KPI**')
    number1 = 111
    st.markdown(f'<h1 style="text-align:center;color:red">{number1}</h1>', unsafe_allow_html=True)

with second_kpi:
    st.markdown('**Second KPI**')
    number2 = 222
    st.markdown(f'<h1 style="text-align:center;color:red">{number2}</h1>', unsafe_allow_html=True)

with third_kpi:
    st.markdown('**Third KPI**')
    number3 = 333
    st.markdown(f'<h1 style="text-align:center;color:red">{number3}</h1>', unsafe_allow_html=True)


### Second Row
st.markdown('<hr/>', unsafe_allow_html=True)
st.markdown('## Secondary KPIs')

first_kpi, second_kpi, third_kpi, fourth_kpi, fifth_kpi, sixth_kpi = st.beta_columns(6)

with first_kpi:
    st.markdown('**First KPI**')
    number1 = 111
    st.markdown(f'<h1 style="text-align:center;color:red">{number1}</h1>', unsafe_allow_html=True)

with second_kpi:
    st.markdown('**Second KPI**')
    number2 = 222
    st.markdown(f'<h1 style="text-align:center;color:red">{number2}</h1>', unsafe_allow_html=True)

with third_kpi:
    st.markdown('**Third KPI**')
    number3 = 333
    st.markdown(f'<h1 style="text-align:center;color:red">{number3}</h1>', unsafe_allow_html=True)

with fourth_kpi:
    st.markdown('**Fourth KPI**')
    number4 = 444
    st.markdown(f'<h1 style="text-align:center;color:red">{number4}</h1>', unsafe_allow_html=True)

with fifth_kpi:
    st.markdown('**Fifth KPI**')
    number5 = 555
    st.markdown(f'<h1 style="text-align:center;color:red">{number5}</h1>', unsafe_allow_html=True)

with sixth_kpi:
    st.markdown('**Sixth KPI**')
    number6 = 666
    st.markdown(f'<h1 style="text-align:center;color:red">{number6}</h1>', unsafe_allow_html=True)


st.markdown('<hr/>', unsafe_allow_html=True)


### Section 1
st.markdown('## Chart Section: 1')

first_chart, second_chart = st.beta_columns(2)

with first_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)


### Section 2
st.markdown('## Chart Section: 2')

first_chart, second_chart = st.beta_columns(2)

with first_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

with second_chart:
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
    st.line_chart(chart_data)