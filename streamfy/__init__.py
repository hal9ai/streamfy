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

def numberinput(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="numberinput", **hyphened)
    return component_value

def radio(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="radio", **hyphened)
    return component_value

def rate(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="rate", **hyphened)
    return component_value

def select(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="select", **hyphened)
    return component_value

def slider(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="slider", **hyphened)
    return component_value

def switch(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="switch", **hyphened)
    return component_value

def taginput(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="taginput", **hyphened)
    return component_value

def message(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    if not "default" in hyphened:
        hyphened['default'] = True
    component_value = _component_func(component="message", **hyphened)
    return component_value

def notification(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    if not "default" in hyphened:
        hyphened['default'] = True
    component_value = _component_func(component="notification", **hyphened)
    return component_value

def progress(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    component_value = _component_func(component="progress", **hyphened)
    return component_value

def steps(**kwargs):
    hyphened = hyphen_case_keys(kwargs)
    if not "has-navigation" in hyphened:
        hyphened['has-navigation'] = False
    component_value = _component_func(component="steps", **hyphened)
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

    button(text = "Primary Light", type="is-primary is-light")
    button(text = "Success", type="is-success")
    button(text = "Success Light", type="is-success is-light")
    button(text = "Danger", type="is-danger")
    button(text = "Danger Light", type="is-danger is-light")
    button(text = "Warning", type="is-warning")
    button(text = "Warning Light", type="is-warning is-light")
    button(text = "Info", type="is-info")
    button(text = "Info Light", type="is-info is-light") 
    button(text = "Link", type="is-link")
    button(text = "Link Light", type="is-link is-light") 
    button(text = "Light", type="is-light")
    button(text = "Ghost", type="is-ghost")

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

    checkbox(text="Info", type="is-info", default=True)
    checkbox(text="Success", type="is-success", default=True)
    checkbox(text="Danger", type="is-danger", default=True)
    checkbox(text="Warning", type="is-warning", default=True)

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
    text = input()
    st.write(text)
    input(type="email", icon="email", default="john@", maxlength="30")
    input(type="is-success", maxlength="30")
    input(type="password", value="iwantmytreasure", password_reveal=True)
    input(type="textarea", maxlength="200")
    input(label="Success", type="is-success")
    input(label="Error", type="is-danger")
    input(label="Info", type="is-info")
    input(label="Warning", type="is-warning")

    st.subheader("Numberinput")
    number = numberinput(placeholder="10", min="5")
    st.write(number)

    st.subheader("Radio")
    radio = radio(radios=[{"text": "A"}, {"text": "B"}])
    st.write(radio)

    st.subheader("Rate")
    rate = rate()
    st.write(rate)

    st.subheader("Select")
    selected = select(data=[{"text": "Seattle"},{"text": "Portland"}])
    st.write(selected)

    st.subheader("Slider")
    slide = slider()
    st.write(slide)

    st.subheader("Switch")
    switched = switch(text="Switch me!")
    st.write(switched)

    st.subheader("Tags")
    tags = taginput(data=["A", "B", "C"], default=["B"], allow_new=True, open_on_focus=True, type="is-info", aria_close_label="Remove", placeholder="Choose letter")
    st.write(tags)

    st.subheader("Message")
    message(text="This is a message", title="Info", type="is-info")

    st.subheader("Notification")
    notification(text="Important notification")

    st.subheader("Progress")
    progress(value=80)

    st.subheader("Steps")
    steps(steps=[
        {"step": "1", "label": "First"},
        {"step": "2", "label": "Second"}
    ])

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
