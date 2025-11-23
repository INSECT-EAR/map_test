# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 20:12:45 2025

@author: Lenovo
"""

import streamlit as st
import folium
import streamlit_folium
import pandas as pd

m = folium.Map(location=[32.055, 118.7794], zoom_start=11, tiles=None)

# 添加高德地图图层
folium.TileLayer(
    tiles='http://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
    attr='果蔬地图',
    subdomains=['1', '2', '3', '4']  # 子域名
).add_to(m)

icon = folium.CustomIcon("https://s2.loli.net/2025/11/23/USTYMOAy7LFZeqK.png", icon_size=(40, 40))

locations = pd.DataFrame({"lat":[32.05512344513,31.14176,38.86537],
                          "lot":[118.779423254,121.66210,121.61752]})
for _,row in locations.iterrows():
    folium.Marker([row["lat"],row["lot"]],icon=icon).add_to(m)
'''
folium.Marker(
    [32.05512344513, 118.779423254],
    icon=icon,
    popup='🦭'
).add_to(m) #南京

folium.Marker(
    [31.14176, 121.66210],
    icon=icon,
    popup='🦭'
).add_to(m) #上海

folium.Marker(
    [38.86537, 121.61752],
    icon=icon,
    popup='🦭'
).add_to(m) #大连

folium.Marker([118.77478,32.01766],icon=icon,popup='🦭').add_to(m) #南京
folium.Marker([121.66210,31.14176],icon=icon,popup='🦭').add_to(m) #上海
folium.Marker([121.61752,38.86537],icon=icon,popup='🦭').add_to(m) #大连
folium.Marker([119.74096,30.62176],icon=icon,popup='🦭').add_to(m) #hellokitty
folium.Marker([113.26630888834939,23.121096917773666],icon=icon,popup='🦭').add_to(m) #广州
folium.Marker([118.50892694191964,31.705546329308735],icon=icon,popup='🦭').add_to(m) #马鞍山
folium.Marker([118.28809750759285,32.28317366893078],icon=icon,popup='🦭').add_to(m) #滁州
folium.Marker([120.63365398672772,31.2980209995723],icon=icon,popup='🦭').add_to(m) #苏州
folium.Marker([119.45728122528317,32.21828539673205],icon=icon,popup='🦭').add_to(m) #镇江
folium.Marker([120.7561320353683,30.755458431702845],icon=icon,popup='🦭').add_to(m) #嘉兴
folium.Marker([126.87364206673749,33.487832365907046],icon=icon,popup='🦭').add_to(m) #济州岛
folium.Marker([116.073456,5.980408],icon=icon,popup='🦭').add_to(m) #亚庇沙比岛
folium.Marker([101.711861,3.157764],icon=icon,popup='🦭').add_to(m) #吉隆坡
folium.Marker([102.240143,2.200844],icon=icon,popup='🦭').add_to(m) #马六甲


m.add_child(folium.ClickForMarker(popup='🦭'))
'''
streamlit_folium.st_folium(m, width=725)
