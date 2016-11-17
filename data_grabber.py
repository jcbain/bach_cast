from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import html5lib

class RawProcessor:



    def rawWriter(url,i, show = "bachelorette"):
        name = requests.get(url)

        with open("/Users/jamesbain/Desktop/bachelor/data/raw/{}{}.html".format(show,i), "wb") as f:
            f.write(name.content)

    # example
    # -------
    # rawWriter('https://en.wikipedia.org/wiki/The_Bachelor_(season_1)',1,show = "bachelor")

    def rawReader(file):

        with open(file, "rb") as f:
            soup = BeautifulSoup(f, "lxml")
        return soup

    # example
    # -------
    #soup = rawReader("/Users/jamesbain/Desktop/bachelor/data/raw/bachelor11.html")
