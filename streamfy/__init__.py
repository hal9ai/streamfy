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

def taginput(data=[], placeholder="", label="", key=None):
    component_value = _component_func(component="taginput", label=label, data=data, placeholder=placeholder, key=key)
    return component_value

def table(data=[], columns=[], label="", key=None):
    component_value = _component_func(component="table", label=label, data=data, columns=columns)
    return component_value

if not _RELEASE:
    st.subheader("Tags")
    tags = taginput(data = ["A", "B", "C"], placeholder = "Choose letter")
    st.write(tags)
    st.subheader("Table")
    columns = [
        {
            "field": 'id',
            "label": 'ID',
            "width": '40',
            "numeric": True
        },
        {
            "field": 'name',
            "label": 'Name',
        },
    ]
    data = [
        { 'id': 1, 'name': 'Jesse' },
        { 'id': 2, 'first_name': 'John' },
    ]
    table(data = data, columns = columns)
