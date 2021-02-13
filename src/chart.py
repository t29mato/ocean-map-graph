import streamlit as st
import time
import pandas as pd

def generate_chart(json, points):
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
                item['ocean_id']
            ]
        )
        st.write(points[item['ocean_id']-1])
        if points[item['ocean_id']-1]:
            chart.add_rows(data)
            # time.sleep(0.0001)
