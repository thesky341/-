
with open("结果.txt", "a") as book:
    with open("测试.txt", "r") as reade:
        for line in reade:
            if(line[1] != "<"): book.write("    " + line + "\n")