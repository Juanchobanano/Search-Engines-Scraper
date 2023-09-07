from setuptools import setup, find_packages
import codecs 
import os 

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name="search_engines_kit",
    version='{{VERSION_PLACEHOLDER}}',
    description="Search Engines Scraper",
    url = "https://github.com/Juanchobanano/Search-Engines-Scraper",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=requirements,
    keywords=['search', 'browsers']
)