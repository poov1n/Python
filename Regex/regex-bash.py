def print_banner(text):
    print("*" * (len(text) + 4))
    print(f"* {text} *")
    print("*" * (len(text) + 4))

banner_text = "Escape REGEX"
print_banner(banner_text)

print("_________________________________________________________")

def str_conv(string):
    spec_chars = ['+',')','(','}','{']
    add_esc = ['\\'+ char for char in spec_chars]
    for char in add_esc:
        string = string.replace(char[1:],char)
    return string
 
print("Provide the normal string to convert")
input_str= input("String = ")

out_str = str_conv(input_str)
print("The equivalent Bash/VIM Regex string is "+ out_str)
