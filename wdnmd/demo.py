import streamlit as st
from streamlit_folium import folium_static
import folium

"# 您掉落物品的地点"
st.write("具体地点在小蓝针所指处")


import streamlit as st
from streamlit_folium import folium_static
import folium

    # center on Liberty Bell
m = folium.Map(location=[30.725526, 103.950056], zoom_start=16)

    # add marker for Liberty Bell
tooltip = "Liberty Bell"
folium.Marker(
    [30.725526, 103.950056], popup="Liberty Bell", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
folium_static(m)
