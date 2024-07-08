import cv2

gradient = []

parameters = {}
parameters_file = open("Parameters/parameters.txt", "r")
for line in parameters_file.readlines():
    if line[0] != "$":
        parameter = line[0:4]
        if not "\n" in parameter:
            if not "grad" in parameter:
                parameters[parameter] = line.split("~")[1]
            else:
                gradient.append(line.split("~")[1])

parameters["auto"] = int(parameters["auto"])

if gradient == []:
    gradient = [" .:!/r(l1Z4H9W8$@", " :"]

if parameters["auto"] == 0:
    gradient_mode = int(input("Gradient Mode: "))
else:
    gradient_mode = int(parameters["grmd"])

symbol_width = int(parameters["sywd"])
symbol_heiht = int(parameters["syhg"])
symbol_ratio = symbol_heiht // symbol_width

if parameters["auto"] == 0:
    filename = str(input("Filename: "))
    extension = "." + str(input("Extension: "))
else:
    filename = parameters["file"]
    extension = "." + parameters["extn"]

image = cv2.imread(parameters["phph"] + filename + extension)
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

result = [["" for k in range(len(image[l]) * symbol_ratio)] for l in range(len(image))]


for y in range(len(image)):
    for x in range(len(image[y])):
        for d in range(symbol_ratio):
            symbol_index = int(image[y][x][2] // (255 // len(gradient[gradient_mode])))
            if symbol_index > len(gradient[gradient_mode]) - 1:
                symbol_index = len(gradient[gradient_mode]) - 1
            result[y][x * symbol_ratio + d] = gradient[gradient_mode][symbol_index]

file = open(parameters["phtx"] + filename + ".txt", "w")

for i in range(len(result)):
    for j in range(len(result[i])):
        file.write(result[i][j])
    file.write("\n")

file.close()

print("Success!")
input()

