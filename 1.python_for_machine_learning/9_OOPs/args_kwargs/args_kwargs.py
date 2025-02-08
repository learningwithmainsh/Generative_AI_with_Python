# Combine args # kwargs

def display_info(name, *args, **kwargs):
    print(f"Name:{name}")
    print("Other Details:", args)
    print("Additional Info:",kwargs)

display_info("john", 25, "Engineer", location = "New York", status = "Active")