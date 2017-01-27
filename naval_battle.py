# Author: Douglas Silva#

class Naval_Battle(object):
    from random import randint
    import  random

    size_board = 10
    board = []
    board_atach = []

    ships = {1 : 5, 2 : 4, 3 : 3, 4 : 2, 5 : 1}
    #ships = {5:5}
    size_ship = 0
    total_ships = 0

    axis_x = 0
    axis_y = 0
    selected_course = ''
    courses = []


    def __init__(self):
        self.loading_board(self.board)
        self.loading_board(self.board_atach)
        self.loading_ship_in_board()
        self.print_board(self.board_atach)


    def loading_board(self, board):
        for x in range(self.size_board):
            board.append([0]*self.size_board)

    def print_board(self, board):
        for row in board:
            print(row)

    def restart_vars(self):
        self.axis_x = 0
        self.axis_y = 0
        self.selected_course = ''
        self.courses = []


    def test_course(self, x, y, size_ship, course):
        test = True
        if course == "UP":
            for index in range(size_ship-1):
                if (self.board[y - 1][x] == 0):
                    y = y - 1
                else:
                    print("Deu choque")
                    test = False
        elif course == "RIGHT":
            for index in range(size_ship-1):
                if (self.board[y][x + 1] == 0):
                    x = x + 1
                else:
                    print("Deu choque")
                    test = False
        elif course == "DOWN":
            for index in range(size_ship-1):
                if (self.board[y + 1][x] == 0):
                    y = y + 1
                else:
                    print("Deu choque")
                    test = False
        elif course == "LEFT":
            for index in range(size_ship-1):
                if (self.board[y][x - 1] == 0):
                    x = x - 1
                else:
                    print("Deu choque")
                    test = False
        if test == True :
            self.courses.append(course)
            print("O caminho %s é livre" % (course))
        else:
            print("O caminho %s é inadequado" %(course))

        return test

    def position_ship_in_course(self, x, y, size_ship, course):
        if course == "UP":
            for index in range(size_ship - 1):
                self.board[y - 1][x] = size_ship
                y = y - 1
        elif course == "RIGHT":
            for index in range(size_ship-1):
                self.board[y][x+1] = size_ship
                x = x + 1
        elif course == "DOWN":
            for index in range(size_ship-1):
                self.board[y+1][x] = size_ship
                y = y + 1
        elif course == "LEFT":
            for index in range(size_ship-1):
                self.board[y][x - 1] = size_ship
                x = x - 1

    def loading_ship_in_board(self):
        for ship in self.ships:
            self.size_ship = 0;
            self.size_ship = self.ships[ship]
            self.total_ships = ship

            print("------------- Navio de Tamanho %d----------------" % (self.size_ship))

            for actual_ship in range(self.total_ships):
                self.restart_vars()
                self.position_ship(self.size_ship)

    def position_ship(self, size_ship):

        positioned = False
        count = 0

        axis_x = 0
        axis_y = 0

        while(positioned == False):
            count = count+ 1

            axis_x = self.randint(0, self.size_board - 1)
            axis_y = self.randint(0, self.size_board - 1)
            courses = []

            print("\nTentativa Nº %d (%d, %d)" %(count, axis_x, axis_y))

            if self.board[axis_y][axis_x] == 0:
                if ((axis_y - (size_ship - 1)) >= 0):
                    courses.append("UP")
                if ((axis_x + (size_ship - 1)) <= self.size_board - 1):
                    courses.append("RIGHT")
                if ((axis_y + (size_ship - 1)) <= self.size_board - 1):
                    courses.append("DOWN")
                if ((axis_x - (size_ship - 1)) >= 0):
                    courses.append("LEFT")
                if(len(courses) != 0):
                    print("Possiveis caminhos: %d" % (len(courses)))
                    print(courses)
                    for course in courses:
                        print("Testanto Caminho %s" % (course))
                        self.test_course(axis_x, axis_y, size_ship, course)
                    if (len(self.courses) > 0): positioned = True


        self.selected_course = self.random.choice(self.courses)
        print(self.courses)
        print("Caminho Escolhido: ", self.selected_course)
        print("")
        self.board[axis_y][axis_x] = size_ship
        self.position_ship_in_course(axis_x, axis_y, size_ship, self.selected_course)

        print("")
        #print("Tamanho do Navio %d (%d,%d)" % (size_ship, axis_x, axis_y))


    def atach(self):
        counter = 0
        size_limite = self.size_board
        print("Escolha um númentro entre 1 e ", size_limite)

        is_valid = True
        while(counter < 10):
            counter = counter + 1
            print("%dº Ataque"%(counter) )
            atachtX = int(input("Axis X: "))
            atachtY = int(input("Axis Y: "))
            print("")

            while (atachtX > size_limite) or (atachtX < 0) or (atachtY > size_limite) or (atachtY < 0):
                print("%dº Dados Inválidos Ataque" % (counter))
                atachtX = int(input("Axis X: "))
                atachtY = int(input("Axis Y: "))
                print("")

            if(self.board[atachtY][atachtX] != 0):
                print("You Hit: %d \n"% (self.board_atach[atachtY-1][atachtX-1]))
                self.board_atach[atachtY-1][atachtX-1] = self.board[atachtY-1][atachtX-1]
                self.print_board(self.board_atach)
            else:
                print("Shot in water!!!\n")






