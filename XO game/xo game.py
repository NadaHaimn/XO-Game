import random
import os
def clear_screen():
    os.system("cls")

class Player :
    def __init__(self) :
        self.name =""
        self.symbol =""
    
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only) : ")
            if name.isalpha():
                self.name = name
                break
            else:
                print("Invalid name. Please use letters only")

    def choose_Symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (a single letter only) : ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            else:
                print("Invalid symbol. Please choose a single letter only.")

class Menu:
    def __init__(self) :
        self.choice=""

    def display_main_menu(self):
        print("Welcome to XO game \nHow many players will play \n1. Two players \n2. one player ")
        self.validate_choice()
        return self.choice
        
    def display_endgame_menu(self):
        print("End of Game \n1. Restart game \n2. Quit game ")
        self.validate_choice()
        return self.choice

    def validate_choice(self):
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == "1" or choice == "2":
               self.choice=choice
               print("-"*30)
               break
            else:
                print("please enter 1 or 2 only")
            
class Board:
    def __init__(self) :
        self.board = [str(i) for i in range(1,10)] # --> list comprehension

    def display_board(self):
        board =f"""
________________    
| {self.board[0]}  |  {self.board[1]}  | {self.board[2]}  |
|____|_____|____|    
| {self.board[3]}  |  {self.board[4]}  | {self.board[5]}  |
|____|_____|____|   
| {self.board[6]}  |  {self.board[7]}  | {self.board[8]}  |
|____|_____|____|

"""
        print(board)
    
    def update_board(self, choice , symbol):
        clear_screen()
        if self.is_valid_move(choice):
            self.board[choice-1]= symbol
            return True
        else:
            return False

    def is_valid_move(self , choice):
        number=self.board[choice-1]
        return number.isdigit()
    
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]
    
class Game:
    def __init__(self) :
        self.board = Board()
        self.players = [Player(),Player()]
        self.menu= Menu()
        self.current_player_index = 0   # first player is in indix 0 so we start with 0

    def start_game(self):
        choice = self.menu.display_main_menu()
        clear_screen()
        if choice =="1" :
            self.setup_players()
            self.play_game()
        else:
            self.auto_player()
            self.play_game()

    def setup_players(self):
        for number ,player in enumerate(self.players,start=1):
            print(f"Player {number}, enter your details : ")
            player.choose_name()
            player.choose_Symbol()
            print("-"*30)
        clear_screen()

    def auto_player(self):
        print(f"Player 1, enter your details : ")
        self.players[0].choose_name()
        self.players[0].choose_Symbol()
        print("-"*30)
        self.players[1].name ="Comp"
        if(self.players[0].symbol.upper()=="X"):
            self.players[1].symbol="O"
        else:
            self.players[1].symbol="X"
        print(f"Player 2 name is '{self.players[1].name}' and his symbol is '{self.players[1].symbol}' ")
        print("-"*30)
        clear_screen()

    def quit_game(self):
        print("Goodbye til another game ")

    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win():
                if self.current_player_index == 0:
                    self.current_player_index =2

                print(f"PLAYER {self.current_player_index } WINS !")
                choice = self.menu.display_endgame_menu()
                if choice =="1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
            elif self.check_draw():
                print("NO one wins")
                choice = self.menu.display_endgame_menu()
                if choice =="1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    def play_turn(self):
        if self.menu.choice=="1":
           self.play_logic()
        else:
            if self.current_player_index ==0:
                self.play_logic()
            else:
                player =self.players[1]
                self.board.display_board()
                print(f"{player.name}'s turn ({player.symbol})")
                while True:
                    cell_choice =random.randint(0,9)
                    if cell_choice<=9 and cell_choice >=1 and self.board.update_board(cell_choice , player.symbol):
                            break
                print(f"He choice number {cell_choice}")
                self.switch_player()
    
    def play_logic(self):
            player =self.players[self.current_player_index]
            self.board.display_board()
            print(f"{player.name}'s turn ({player.symbol})")
            while True:
                try:
                    cell_choice = int(input("Choose a cell (1-9) : "))
                    if cell_choice<=9 and cell_choice >=1 and self.board.update_board(cell_choice , player.symbol):
                        break
                    else:
                        print("Invalid move, try again")
                except ValueError:
                    print("Please enter a number between 1 and 9.")
            self.switch_player()
    def switch_player(self):
        self.current_player_index= 1 - self.current_player_index
    
    def check_win(self):
        if (self.board.board[0]==self.board.board[1]==self.board.board[2]or self.board.board[3]==self.board.board[4]==self.board.board[5]or self.board.board[6]==self.board.board[7]==self.board.board[8] or self.board.board[0] == self.board.board[3]==self.board.board[6] or self.board.board[1]==self.board.board[4]==self.board.board[7] or self.board.board[2]==self.board.board[5]==self.board.board[8]or self.board.board[0]==self.board.board[4]==self.board.board[8] or self.board.board[2]==self.board.board[4]==self.board.board[6]):
            self.board.display_board()
            return True
        return False
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board) 

    def restart_game(self):
        clear_screen()
        self.board.reset_board()
        self.current_player_index=0
        self.start_game()

game = Game()
game.start_game()