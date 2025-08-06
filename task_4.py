def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено."
        except ValueError:
            return "Введіть ім'я та номер телефону через пробіл."
        except IndexError:
            return "Введіть команду та аргументи."
    return wrapper


def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, args


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "Контактів немає."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            print("Введіть команду.")
            continue

        try:
            command, args = parse_input(user_input)
        except ValueError:
            print("Невірна команда.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()