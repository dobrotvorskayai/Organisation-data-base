from work import show_d_b, find_pos, change_pos, add_pos, del_pos, read_all
from check import check_new_data

def menu():
    read_all()
    while True:
        type = input("Chose option, please:\n"
                    "1 - Show Data base\n"
                    "2 - Find position\n"
                    "3 - Change position\n"
                    "4 - Add position\n"
                    "5 - Delete position\n"
                    "0 - Exit\n")
        match type:    
            case "1":
                show_d_b()
            case "2":
                find_pos(input("Enter id: "), read_all())
            case "3":
                show_d_b()
                id_change = input(f"Enter the id: ")
                if find_pos(id_change, read_all()) and (answer := edit_menu()):
                    change_pos(answer, id_change)
                
            case "4":
                add_pos(add_menu())
            case "5":
                del_pos(input("Enter id: "))
            case "0":
                break
            case _:
                print("Enter number from 0 to 5, please")

def add_menu():
    add_dict = {"id": "1", "name": "", "surname": "", "department": "", "position": ""}
    for i in add_dict:
        if i != "id":
            add_dict[i] = check_new_data(i)
    
    return add_dict

def edit_menu():
    add_dict = {"1": "name", "2": "surname", "3": "department", "4": "position"}
    while True:
        print("\nChanging:")
        change = input("1. name\n"
                       "2. surname\n"
                       "3. department\n"
                       "4. position\n"
                       "0. exit\n")

        match change:
            case "1" | "2" | "3" | "4":
                type_date = add_dict[change]
                return type_date, check_new_data(type_date)
            case "0":
                return 0
            case _:
                print("Enter number from 0 to 4, please")