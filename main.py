def main():
    file_target = input("target file > ")
    tags = []
    output = ""

    sequence = 0
    append = []
    with open(file_target, "r", encoding="utf8") as file:
        for line in file:
            if sequence == 4:
                tags.append(append)
                append = []
                sequence = 1
            else:
                sequence += 1

            if sequence == 1 or sequence == 3:
                append.append(line[:-1])

    output += "digraph {\n"
    for tuple in tags:
        output += "    " + "\"" + tuple[0] + "\"" + " -> " + "\"" + tuple[1] + "\"" + "\n"
    output += "}\n"

    with open(f"{file_target}.gv", "w", encoding="utf8") as file:
        file.write(output)


if __name__ == "__main__":
    main()
