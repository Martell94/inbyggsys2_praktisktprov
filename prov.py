#Author: Jacob Martell
#Date: 2023-10-13

res_list = []

def main():
    print("Ei22 - Praktiskt prov HT23")
    value = 0
    while True:
        resistors = input("Ange resistorer:")
        res_list = (resistors.split(' '))
        
        for i in range (0, len(res_list)):
            value = int(res_list[i])
            res_list[i] = value
        break
        
    calc_series(res_list)
    calc_parallell(res_list)


def calc_series(resistances):
    sum = 0
    for i in range(0, len(resistances)):
        sum += resistances[i]
    print(f"Serieresistans: {sum}")
    
def calc_parallell(resistances):
    rtot_p = 0
    for i in range(0, len(resistances)):
        rtot_p += (1/resistances[i])            
    print(f"Parallellresistans: {(1/rtot_p)}")

main()