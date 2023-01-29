import csv
from os import path
from check import matching_rec

all_data = {}
last_id = 0
name_db = "Base.csv"

def read_all():
    global all_data, last_id

    if path.exists(name_db):
        with open(name_db, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            all_data = [i for i in csv_reader]
            last_id = all_data[-1]["id"]
            return all_data
    else:
        print("The data base isn't found")

def show_d_b ():
    for_output = [" ".join(k.values()) for k in all_data]
    print(*for_output, sep="\n", end=f"\n{'-' * 20}\n\n")

def find_pos(data_find, all_info):
    candidates = [" ".join(i.values()) for i in all_info if data_find in i.values()]
    if candidates:
        print(*candidates, sep="\n", end="\n\n")
        return [n[0] for n in candidates]
    else:
        print("Id not found.\n")
        return 0

def change_pos(data_change, id_change):
    global all_data
    key, value = data_change

    if find_pos(id_change, all_data):
        for i, v in enumerate(all_data):
            if v["id"] == id_change:
                v[key] = value
                all_data[i] = v

        with open(name_db, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "surname", "department", "position"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_data)
            print("Data changed\n")
    else:
        print("Id not found.\n")

def add_pos(data):
    global last_id

    if all(data.values()) and matching_rec(data, all_data):
        last_id = int(last_id) + 1
        data["id"] = last_id

        with open(name_db, "a", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "surname", "department", "position"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow(data)
            print("Data added to the base")
    else:
        print("The data is already present in the database")

def del_pos(data_del):
    global all_data

    id_cand = find_pos(data_del, all_data)
    if id_cand:
        id_del = input(f"Enter the id: ")
        
        if id_del in id_cand:
            all_data = [k for k in all_data if k["id"] != id_del]
            with open(name_db, "w", encoding="utf-8", newline="") as file:
                fieldnames = ["id", "name", "surname", "department", "position"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(all_data)
                print("Data deleted\n")
        else:
            print("Id not found.\n")