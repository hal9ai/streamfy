import streamlit as st
import streamlit.components.v1 as components

import os

_RELEASE = False

if not _RELEASE:
    _component_func = components.declare_component(
        "streamfy",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/dist")
    _component_func = components.declare_component(
        "streamfy", path=build_dir)

def taginput(data=[], placeholder="", key=None):
    component_value = _component_func(data=data, placeholder=placeholder, key=key)
    return component_value

if not _RELEASE:
    st.subheader("Start")
    tags = taginput(data = ["A", "B", "C"], placeholder = "Choose letter")
    st.write(tags)
    st.subheader("End")
