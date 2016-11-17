def rawWriter(url,i, show = "bachelorette"):

    name = requests.get(url)

    with open("/Users/jamesbain/Desktop/bachelor/data/raw/{}{}.html".format(show,i), "wb") as f:
        f.write(name.content)

# example
# -------
# rawWriter('https://en.wikipedia.org/wiki/The_Bachelor_(season_1)',1,show = "bachelor")



if __name__ == '__main__':
    main()
