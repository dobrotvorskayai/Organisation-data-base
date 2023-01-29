def check_new_data(num):
    answer = input(f"Enter a {num}: ")
    while True:
        if answer.isalpha():
            break
        answer = input(f"Data is incorrect!\n"
                       f"Use only the letters"
                       f" of the alphabet\n"
                       f"Enter a {num}: ")
    return answer

def matching_rec(new_entry: dict, all_info):
    value = list(new_entry.values())[1:]
    all_values = [list(k.values())[1:] for k in all_info]
    return value not in all_values