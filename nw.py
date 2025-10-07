py_content = """def main():
    pass


if __name__ == \"__main__\":
    main()

    """

c_content = """int main(int argc, char *argv[]) {
    return 0;
}"""


def get_content(extension: str):
    match extension:
        case "py":
            return py_content
        case "c":
            return c_content
        case _:
            return ""


def main(filename: str, extension: str):
    content = get_content(extension)

    with open(f"{filename}.{extension}", "w", encoding="utf-8") as f:
        rc: int = f.write(content)
        if rc > 0:
            print("done")


if __name__ == "__main__":
    import sys
    import os
    import html

    filename = html.escape(sys.argv[1])
    extension = html.escape(sys.argv[2])

    main(filename, extension)
    os.system(f"nvim {filename}.{extension}")
