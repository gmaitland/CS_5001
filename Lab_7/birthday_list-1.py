'''
    Super villains want to crash your birthday party. You're not having it!
    Load your guest list from the file and "uninvite" whoever you want.
    Then, write your updated list back to the file again
'''


def load_file(filename):
    villains = []
    try:
        with open(filename, "r") as names:
            for each in names:
                villain = {}
                villain["last"], villain["first"] = each.split(",")
                villain["last"] = villain["last"].strip()
                villain["first"] = villain["first"].strip()
                villains.append(villain)
    except IOError:
        print("A file error occurred")
    else:
        return villains

def save_file(filename, villains):
    try:
        with open(filename, "w") as names:
            for villain in villains:
                names.write(villain["last"] + ", " + villain["first"] + "\n")
    except IOError:
        print("A file error occurred")


def print_party_crashers(villains):
    print("Here are the villains trying to crash your party:")
    for each in villains:
        print(each["first"], each["last"])
        
def uninvite(villains, firstname, lastname):
    for i in range(len(villains)):
        if firstname.upper() == villains[i]["first"].upper() and \
           lastname.upper() == villains[i]["last"].upper():
            villains.pop(i)
            return True
    return False

def get_name():
    answer = input("Enter who you want to uninvite to your party :q: quits: ")
    answer = answer.strip()
    return answer


def main():
    villains = load_file("super_villains.txt")
    print_party_crashers(villains)
    answer = get_name()
    while answer.lower() != ":q:":
        if len(answer) > 0 and " " in answer:
            try:
                firstname, lastname = answer.split()
            except: # if they provide more than 1 name, ask for just 2
                print("Only firstname & lastname please! If you have " \
                      "more than 2 names, kindly use the common 2")
                answer = get_name()
                continue
        else:
            print("I need firstname lastname, please!")
            answer = get_name()
            continue
        
        if not uninvite(villains, firstname, lastname):
            print("Couldn't locate {} on the list".format(answer))
        else:
            print("{} removed from your birthday party list!\n".format(answer))
    
        answer = input("Enter someone else to uninvite :q: quits: ")

    save_file("super_villains.txt", villains)

main()
            
