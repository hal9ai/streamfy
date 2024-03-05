import setuptools
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="streamfy",
    version="0.3.2",
    author="Javier Luraschi",
    author_email="jluraschi@gmail.com",
    description="Modern frontend web components based on Buefy for Streamlit.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/hal9ai/streamfy",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
