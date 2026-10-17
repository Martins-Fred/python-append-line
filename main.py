
def append_line(path, line):
    """Add one line to the end of a file.

    Input:   path, as above; line, a string.
    Output:  nothing (None). After the call the file holds what it held
             before, then line, then "\n". If the file did not exist, it is
             created. Assume an existing file ends with a line ending, as
             every file written by write_lines does.

        append_line(p, "c") on a file holding "a\nb\n" -> "a\nb\nc\n"
    """
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")  # Add the string followed by a newline
    return None


# Set up a test file with two lines.
# We use "w" here only to reset our test file.
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("a\nb\n")


# Test 1: Append a new line
append_line("sample.txt", "c")

# Read the file to check the result
with open("sample.txt", encoding="utf-8") as f:
    print(repr(f.read()))


# Test 2: Append another line
append_line("sample.txt", "d")

with open("sample.txt", encoding="utf-8") as f:
    print(repr(f.read()))
