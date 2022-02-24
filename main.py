import graphviz

def main():
    file_target = input("target file > ")
    tags = []
    dot = graphviz.Digraph()

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

    for tuple in tags:
        dot.edge(tuple[0], tuple[1])

    with open(f"{file_target}.gv", "w", encoding="utf8") as file:
        file.write(dot.source)


if __name__ == "__main__":
    main()
