
contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a user name"
        except ValueError:
            return "Provide both name and phone, please"
        except IndexError:
            return "Invalid command format"
    return wrapper

@input_error
def add_contact(name, phone):
    if name in contacts:
        raise ValueError("Contact already exists. Use 'change' command to update the phone number.")
    contacts[name] = phone
    return f"Contact {name} added successfully"

@input_error
def change_phone(name, phone):
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Phone number for {name} updated successfully"

@input_error
def get_phone(name):
    if name not in contacts:
        raise KeyError
    return f"The phone number for {name} is {contacts[name]}"

def show_all_contacts():
    if not contacts:
        return "No contacts available"
    result = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return result

def main():
    print("How can I help you?")

while True:
    command = input("Enter a command: ").lower()
    if command == "hello":
        print("How can I help you?")
    elif command.startswith("add"):
        try:
            _, name, phone = command.split(maxsplit=2)  
            response = add_contact(name, phone)
        except ValueError:
            response = "Invalid command format"
        print(response)
    elif command.startswith("change"):
        try:
            _, name, phone = command.split(maxsplit=2)  
            response = change_phone(name, phone)
        except ValueError:
            response = "Invalid command format"
        print(response)
    elif command.startswith("phone"):
        try:
            _, name = command.split(maxsplit=1)  
            response = get_phone(name)
        except ValueError:
            response = "Invalid command format"
        print(response)
    elif command == "show all":
        print(show_all_contacts())
    elif command in ["good bye", "close", "exit"]:
        print("Good bye!")
        break
    else:
        print("Invalid command. Please try again")

if __name__ == "__main__":
    main()




