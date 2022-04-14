import textwrap
def main():
    long_string = "This is a really really long string! I am happy to making video again --  I am only have a short window of time to do it, but I will when I can. "
    wrapped_line = textwrap.wrap(long_string)
    print(wrapped_line)
    for line in wrapped_line:
        print(len(line),line)
    print(textwrap.fill(long_string))
if __name__ == '__main__':
    main()