def demo():
    a = "HELLO WORLD"
    b = "Hello World"
    dic = {"value1": a, "Value": b}
    return dic


if __name__=='__main__':
    demo()
    f = open("file_demo.txt",'w')
    f.write(f"{demo()}")
    print("File Appended")
    f.close()
