import svg_modifier


def main():

    print("program start")
    # get the file path from the user
    file_path = input(
        "Please enter the file path of the SVG file you would like to modify:")

    # load the svg file
    tree, root = svg_modifier.load_svg(file_path)

    # TODO modify the svg

    # save the svg file
    svg_modifier.save_svg(tree, file_path)


if __name__ == "__main__":
    main()
