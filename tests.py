from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def main():
    # calc = get_files_info("calculator", ".")
    # print(calc)
    # calc_pkg = get_files_info("calculator", "pkg")
    # print(calc_pkg)
    # calc_bin = get_files_info("calculator", "/bin")
    # print(calc_bin)
    # calc_upper = get_files_info("calculator", "../")
    # print(calc_upper)

    #lorem = get_file_content("calculator", "lorem.txt")
    #print(lorem)
    
    calc_main = get_file_content("calculator", "main.py")
    print(calc_main)
    calc_pkg = get_file_content("calculator", "pkg/calculator.py")
    print(calc_pkg)
    calc_bin = get_file_content("calculator", "/bin/cat")
    print(calc_bin)


if __name__ == "__main__":
    main()