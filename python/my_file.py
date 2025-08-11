# read file
def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "file not found"
    except PermissionError:
        return "permission denied"


# write file
def write_file(filename, content):
    with open(filename, 'w', encoding='utf-8')as file:
        file.write(content+'\n')

# append file


def append_file(filename, content):
    with open(filename, 'a', encoding='utf-8')as file:
        file.write(content+'\n')


# test
if __name__ == "__main__":
    file_name = "myfile.txt"
    print(read_file(file_name))
    write_file(file_name, "Hello, this is from python side.")
    print(read_file(file_name))
