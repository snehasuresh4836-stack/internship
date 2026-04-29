FILE = "students.txt"

def write_student(data):
    with open(FILE, "w") as f:
        for item in data:
            line = item[0] + "," + item[1] + "," + str(item[2]) + "," + str(item[3]) + "," + str(item[4])
            f.write(line + "\n")


def read_student():
    data = []
    
    try:
        with open(FILE, "r") as f:
            for line in f:
                t = line.strip().split(",")
                data.append((t[0], t[1], int(t[2]), int(t[3]), int(t[4])))
    except:
        pass
    
    return data