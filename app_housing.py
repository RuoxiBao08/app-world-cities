import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 标题 (记得改成你的名字)
st.title('California Housing Data (1990) by ruoxibao')

# 读取数据
df = pd.read_csv('housing.csv')

# 2. 主滑块
slider_value = st.slider('Minimal Median House Value', 0, 500001, 200000)

# 3. 侧边栏副标题
st.subheader('See more filters in the sidebar:')

# 4. 侧边栏多选框 (默认全选)
location_filter = st.sidebar.multiselect(
    'Choose the location type',
    df.ocean_proximity.unique(),
    df.ocean_proximity.unique()
)

# 5. 侧边栏单选按钮
income_filter = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Medium', 'High')
)

# 开始数据过滤
df = df[df.median_house_value >= slider_value]
df = df[df.ocean_proximity.isin(location_filter)]

# 根据收入级别过滤 (使用 if/elif/else)
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]

# 6. 地图
st.map(df)

# 7. 直方图 (30个bins)
st.subheader('Histogram of Median House Value')
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df.median_house_value, bins=30)
ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')
st.pyplot(fig)