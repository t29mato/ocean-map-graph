import streamlit as st
import json
import time
import pandas as pd

st.sidebar.title('表示するポイント')

point_master = [
    '岩',
    '川奈',
    '富戸',
    'IOP',
    '伊豆大島',
    '大瀬璃',
    '雲見',
    '神子元島'
]

chk1 = st.sidebar.checkbox('岩', value=True)
chk2 = st.sidebar.checkbox('川奈')
chk3 = st.sidebar.checkbox('富戸')
chk4 = st.sidebar.checkbox('IOP')
chk5 = st.sidebar.checkbox('伊豆大島')
chk6 = st.sidebar.checkbox('大瀬璃')
chk7 = st.sidebar.checkbox('雲見')
chk8 = st.sidebar.checkbox('神子元島')
checks = [chk1, chk2, chk3, chk4, chk5, chk6, chk7, chk8]

st.title('2020年の伊豆半島周辺の透明度')
json = json.load(open('./data/ocean.json'))

chart = st.line_chart()
for item in json:
    data = pd.DataFrame(
        [
            [
                float(item['avg'])
            ]
        ],
        [
            pd.to_datetime(item['created_at'])
        ],
        [
            point_master[item['ocean_id']-1]
        ]
    )
    if checks[item['ocean_id']-1]:
        chart.add_rows(data)
        time.sleep(0.001)
