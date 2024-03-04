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

def hyphen_case(string):
    string = string.replace('_', '-')
    return string

def hyphen_case_keys(args):
    snaked = {}
    for key, value in args.items():
        new_key = hyphen_case(key)
        snaked[new_key] = value
    return snaked

def breadcrumb(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="breadcrumb", **hyphened)
    return component_value

def button(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="button", **hyphened)
    return component_value

def carousel(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="carousel", **hyphened)
    return component_value

def autocomplete(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="autocomplete", **hyphened)
    return component_value

def checkbox(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="checkbox", **hyphened)
    return component_value

def clockpicker(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="clockpicker", **hyphened)
    return component_value

def colorpicker(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="colorpicker", **hyphened)
    return component_value

def datepicker(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="datepicker", **hyphened)
    return component_value

def input(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="input", **hyphened)
    return component_value

def taginput(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="taginput", **hyphened)
    return component_value

def table(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="table", **hyphened)
    return component_value

if not _RELEASE:
    st.subheader("Breadcrumb")
    item = breadcrumb(items=[{"text": "A"}, {"text": "B"}])
    st.write(item)

    st.subheader("Button")
    if button(text = "Click!"):
        st.write("Clicked!")

    st.subheader("Carousel")
    selection = carousel(items=[
        "https://picsum.photos/id/1051/1230/500",
        "https://picsum.photos/id/1052/1230/500",
        "https://picsum.photos/id/1053/1230/500",
    ])
    st.write(selection)
    
    st.subheader("Autocomplete")
    complete = autocomplete(data=["Apple", "Bannana", "Cherry"])
    st.write(complete)

    st.subheader("Checkbox")
    checked = checkbox(text = "Check me")
    st.write(checked)

    st.subheader("Clockpicker")
    clock = clockpicker()
    st.write(clock)

    st.subheader("Colorpicker")
    color = colorpicker()
    st.write(color)

    st.subheader("Datepicker")
    datepick = datepicker()
    st.write(datepick)

    st.subheader("Input")
    email = input(type="email", default="john@", maxlength="30")
    st.write(email)

    st.subheader("Tags")
    tags = taginput(data=["A", "B", "C"], default=["B"], allow_new=True, open_on_focus=True, type="is-info", aria_close_label="Remove", placeholder="Choose letter")
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
    table(data=data, columns=columns, paginated=True)
