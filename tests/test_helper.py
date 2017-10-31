from models.map import Map

def get_map():
    str_map =  "46B E59 EA C1F 45E 63 899 FFF 926 7AD C4E FFF E2E 323 6D2 976 83F C96 9E9 A8B 9C1 461 F74 D05 EDD E94 5F4 D1D D03 DE3 89 925 CF9 CA0 F18 4D2"
    return Map(str_map)

def get_str_map():
    return "46B E59 EA C1F 45E 63 899 FFF 926 7AD C4E FFF E2E 323 6D2 976 83F C96 9E9 A8B 9C1 461 F74 D05 EDD E94 5F4 D1D D03 DE3 89 925 CF9 CA0 F18 4D2"

def get_2x2_map():
    return Map("11 20 35 40")

def get_3x3_map():
    return Map("0 0 4 4 0 4 4 0 0")

def create_map(self):
    return [["46B", "E59", "EA", "C1F", "45E", "63"],
            ["899", "FFF", "926", "7AD", "C4E", "FFF"],
            ["E2E", "323", "6D2", "976", "83F", "C96"],
            ["9E9", "A8B", "9C1", "461", "F74", "D05"],
            ["EDD", "E94", "5F4", "D1D", "D03", "DE3"],
            ["89", "925", "CF9", "CA0", "F18", "4D2"]]
