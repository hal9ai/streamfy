# Streamfy — Bulma for Streamlit

Modern frontend components based on [Bulma](https://bulma.io/) for [Streamlit](https://streamlit.io/) based of [Buefy](https://buefy.org/).

## Starting

Install `streamfy`:

```bash
pip install streamfy
```

Create a simple application `app.py`:

```py
import streamlit as st
import streamfy as sy

sy.carousel(items=[
  "https://picsum.photos/id/1051/1230/500",
  "https://picsum.photos/id/1052/1230/500",
  "https://picsum.photos/id/1053/1230/500",
])
```

Run this application:

```
streamlit run app.py
```

## Contributing

- Ensure you have [Python 3.6+](https://www.python.org/downloads/), [Node.js](https://nodejs.org), and [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) installed.
- Clone this repo.
- Create a new Python virtual environment for the template:

```
$ python3 -m venv venv  # create venv
$ . venv/bin/activate   # activate venv
$ pip install streamlit # install streamlit
```

- Initialize and run the component template frontend:

```
$ cd streamfy/frontend
$ npm install    # Install npm dependencies
$ npm run serve  # Start the Webpack dev server
```

- From a separate terminal, run the template's Streamlit app:

```
$ . venv/bin/activate  # activate the venv you created earlier
$ streamlit run streamfy/__init__.py  # run the example
```

- If all goes well, you should see something like this:
  ![Quickstart Success](images/development.png)
- Modify the frontend code at `streamfy/frontend/src/Streamfy.vue`.
  - Parameters passed by Python script are made available in `args` props.
- Modify the Python code at `streamfy/__init__.py`.

## Resources

- [Buefy Documentation](https://buefy.org/documentation/steps)
