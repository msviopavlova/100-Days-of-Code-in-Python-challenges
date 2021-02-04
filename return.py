def format_name(f_name, l_name):
    name = f_name.title()
    last_name  = l_name.title()
    return f"{name} {last_name}"

formatted_string = format_name("violEtTa", "wHaTeveR")
print(formatted_string)