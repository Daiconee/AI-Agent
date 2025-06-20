from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

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
    
    #calc_main = get_file_content("calculator", "main.py")
    #print(calc_main)
    #calc_pkg = get_file_content("calculator", "pkg/calculator.py")
    #print(calc_pkg)
    #calc_bin = get_file_content("calculator", "/bin/cat")
    #print(calc_bin)
    
    calc_lorem = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(calc_lorem)
    calc_pkg = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(calc_pkg)
    calc_tmp = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(calc_tmp)




if __name__ == "__main__":
    main()