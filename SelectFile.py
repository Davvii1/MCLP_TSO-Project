import os

def GetCandidateAndDemand():
    # Validate selected file

    def validateS(files, text=""):
        while True:
            try:
                value = int(input(text))
            except ValueError:
                print("Enter a valid value")
                continue
            else:
                if 0 < value <= files:
                    return value
                else:
                    print("Select an existing file")


    # Get the instances files

    i_arr = os.listdir(os.path.dirname(__file__) + '/instances')

    for x in range(len(i_arr)):
        print(str(x + 1) + '.- ' + i_arr[x])
    s_file = i_arr[validateS(len(i_arr), 'Enter the number of the selected file: ') - 1]
    o_file = open(os.path.dirname(__file__) + '/instances/' + s_file, "r")


    # Get values to export to heuristics

    s_data = o_file.readline().strip().split(' ')
    p = int(s_data[0])
    f = int(s_data[1])
    sf = int(s_data[2])
    r = int(s_data[3])
    data = []

    for line in o_file.readlines():
        data.append([int(x) for x in line.strip().split(' ')])

    export_candidate = data[:f]
    export_points = data[f:]

    print("Selected file:", s_file)

    return export_candidate, export_points, p, f, sf, r