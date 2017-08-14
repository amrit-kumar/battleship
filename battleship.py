from random import randint
# import numpy

class Battleship():

    def define_ocean(self):
            #ocean_size = input("give your ocean size!!").split(',')
            ocean_matrix = []
            # n=int(input("enter number of row:"))
            # m=int(input("enter number of column:"))
            for i in range(1, 100, 10):
                row_matrix = []
                for k in range(i, i + 10, 1):
                    row_matrix.append(k)
                    # print("row_matrix",row_matrix)
                ocean_matrix.append(row_matrix)
            print("ocean_matrix",ocean_matrix)

            # Matrix = [[0 for x in range(10)] for y in range(10)]
            # ship_start_point=input("enter starting point coordinates of ship seperated by comma:").split(',')
            # ship_end_point=input("enter end point coordinates of ship seperated by comma:").split(',')

            ocean_matrix_A=ocean_matrix
            ocean_matrix_B=ocean_matrix

            ship1=[12,13,14,15,16]
            ship2=[31,41,51,61]
            ship3=[79,79,80]
            ship_list_a=ship1+ship2+ship3

            shipb1=[22,23,24,25,26]
            shipb2=[32,42,52]
            shipb3=[51,61,71,81]
            ship_list_b=shipb1+shipb2+shipb3

            a_is_attacker=True

            while len(ship_list_b)!=0 and len(ship_list_a)!=0:
                if a_is_attacker:

                    ship_attack_point = input(
                        " Hi 'A' enter attack point coordinates of ship seperated by comma:").split(',')
                    x = int(ship_attack_point[0])
                    y = int(ship_attack_point[1])

                    value = ocean_matrix_B[x][y]
                    print("value", value)

                    if value in ship_list_b:
                        print("attack successful")
                        ship_list_b.remove(value)
                        if not ship_list_b:
                            print("A IS THE WINNER!!!!!!!!!!!!!")
                            break
                    else:
                        a_is_attacker=False

                else:
                    ship_attack_point = input(
                        " Hi 'B' enter attack point coordinates of ship seperated by comma:").split(',')
                    x = int(ship_attack_point[0])
                    y = int(ship_attack_point[1])

                    value = ocean_matrix_A[x][y]
                    print("value", value)

                    if value in ship_list_a:
                        print("attack successful")
                        ship_list_a.remove(value)
                        if not ship_list_a:
                            print("B IS THE WINNER!!!!!!!!!!!!!")
                            break
                    else:
                        a_is_attacker=True


b_obj=Battleship()
b_obj.define_ocean()