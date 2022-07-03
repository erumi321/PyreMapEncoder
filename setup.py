   
"""setup.py: setuptools control."""
 
 
import re
from setuptools import setup 
 
# with open("README.md", "rb") as f:
#     long_descr = f.read().decode("utf-8")
 
 
setup(
    name = "pyre_map_encoder",
    packages = ["pyre_map_encoder"],
    entry_points = {
        "console_scripts": ['pyre_map_encoder = pyre_map_encoder.cli:main']
        },
    version = "1.0",
    description = "Pack JSON into game usable map binaries for Pyre",
    #long_description = long_descr,
    author = "erumi321",
    author_email = "erumi321@gmail.com",
    url = "",
    )