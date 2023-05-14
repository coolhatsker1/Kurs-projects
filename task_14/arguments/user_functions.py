from system_helpers import get_data_from_file, write_to_file

USERS_FILE_PATH = "C:/Mein_Kamph/kurs/git_basics/task_14/arguments/database/users.json"


def save_user(first_name, last_name, email):
    data = get_data_from_file(USERS_FILE_PATH)
    new_obj = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    if len(data) >= 1:
        new_obj["id"] = len(data) + 1
    else:
        new_obj["id"] = 1
    data.append(new_obj)
    write_to_file(USERS_FILE_PATH, data)


def get_all_users():
    data = get_data_from_file(USERS_FILE_PATH)
    for obj in data:
        print(obj["id"])
        print(obj["first_name"])
        print(obj["last_name"])
        print(obj["email"])
        print("================================")


def get_user_by_id(id):
    data = get_data_from_file(USERS_FILE_PATH)
    for obj in data:
        if id == obj["id"]:
            print(obj["id"])
            print(obj["first_name"])
            print(obj["last_name"])
            print(obj["email"])


def delete_user(id):
    data = get_data_from_file(USERS_FILE_PATH)
    for i in range(len(data)):
        if data[i]["id"] == id:
            del data[i]
            break
    write_to_file(USERS_FILE_PATH, data)


def redact_user(first_name, last_name, email, identifier):
    data = get_data_from_file(USERS_FILE_PATH)
    for obj in data:
        if int(identifier) == obj.get("id"):
            obj.update({"first_name": first_name, "last_name": last_name, "email": email})
            write_to_file(USERS_FILE_PATH, data)
            return
    raise KeyError("User not found")