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
    
    if not phone.isdigit():
        raise ValueError("Phone must be a numeric value.")
    
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

    commands = {
        "hello": lambda: print("How can I help you?"),
        "add": lambda args: add_contact(*args),
        "change": lambda args: change_phone(*args),
        "phone": lambda args: get_phone(*args),
        "show all": lambda: print(show_all_contacts()),
        "good bye": lambda: print("Good bye!") or exit(),
        "close": lambda: print("Good bye!") or exit(),
        "exit": lambda: print("Good bye!") or exit(),
    }

    while True:
        command = input("Enter a command: ").lower()
        try:
            command, *args = command.split()
            response = commands.get(command, lambda: print("Invalid command. Please try again"))(args)
            print(response)
        except ValueError as e:
            print(str(e))

if __name__ == "__main__":
    main()




