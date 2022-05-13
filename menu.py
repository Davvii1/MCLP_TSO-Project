
import Rig_MCLP as rig
import SelectFile as file_select


def menu():

    option = int(input("What do you want to do?\n1.-Create instances\n2.-Run Heuristics\n"))

    if option == 1 or option == 2:
        return option
    else:
        print("Select a valid option")
        return 0