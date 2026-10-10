import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. 标题，把[Your Name]替换成你的名字
st.title("California Housing Data (1990) by [Gaoya]")

# 读取数据集
df = pd.read_csv("housing 2.csv")

# 2. 房价最小值滑块
house_value_min = st.slider(
    "Minimal Median House Value",
    min_value=0,
    max_value=500001,
    value=200000
)
# 筛选：只保留大于等于滑块数值
df = df[df["median_house_value"] >= house_value_min]

# 3. 子标题
st.subheader("See more filters in the sidebar:")

# 4. 侧边栏多选框，ocean_proximity，默认全部选中
location_categories = df["ocean_proximity"].unique()
location_filter = st.sidebar.multiselect(
    "Choose the location type",
    location_categories,
    default=location_categories
)
df = df[df["ocean_proximity"].isin(location_filter)]

# 5. 侧边栏单选按钮，收入分级
income_selection = st.sidebar.radio(
    "Choose income level",
    ["Low", "Medium", "High"]
)

if income_selection == "Low":
    df = df[df["median_income"] <= 2.5]
elif income_selection == "Medium":
    df = df[(df["median_income"] > 2.5) & (df["median_income"] < 4.5)]
elif income_selection == "High":
    df = df[df["median_income"] >= 4.5]

# 6. 绘制筛选后的地图（latitude & longitude）
st.map(df)

# 7. 直方图，bins=30，放在地图下方
fig, ax = plt.subplots()
ax.hist(df["median_house_value"], bins=30)
ax.set_xlabel("Median House Value (USD)")
ax.set_ylabel("Number of Districts")
st.pyplot(fig)
