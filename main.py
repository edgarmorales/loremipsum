from loremipsum import loremipsum


def main():

    lorem_ipsum_text = loremipsum.generate_text()
    print("Generated: {}" .format(lorem_ipsum_text))


if __name__=="__main__":
    main()