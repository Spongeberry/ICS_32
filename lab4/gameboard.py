class BoardClass:
    """A simple class to store any information about the Board of tic tac toe.

    Attributes:
        Players_user_name1 (str): Player 1's username.
        Players_user_name2 (str): Player 1's username.
        User_name_of_the_last_player_to_have_a_turn (str): last player to have the turn.
        P1_wins (int): account for P1's wins.
        P2_wins (int): account for P2's wins.
        Number_of_ties (int): number of ties.
        P1_losses (int): account for P1's losses.
        P2_losses (int): account for P2's losses.
        gamesplayed (int): account for games played.
        actualgame (list): the game itself as a list.
        roundsplayed (int): account for how many rounds are played.
        gameover (bool): True if game end. Flase if game continues.
    """

    __Players_user_name1__ = ''
    __Players_user_name2__ = ''
    __User_name_of_the_last_player_to_have_a_turn__ = ''
    __P1_wins__ = 0
    __P2_wins__ = 0
    __Number_of_ties__ = 0
    __P1_losses__ = 0
    __P2_losses__ = 0
    __gamesplayed__ = 0
    __actualgame__ = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    __roundsplayed__ = 0
    __gameover__ = False

    
    def __init__(self, P1_username: str, P2_username: str) -> None:
        """Make a BoardClass.

        Args:
            P1_username: Player 1's username.
            P2_username: Player 2's username.            
        """
        self.__Players_user_name1__ = P1_username
        self.__Players_user_name2__ = P2_username


    def updateGamesPlayed(self) -> None:
        """Keeps track how many games have started.
        """
        #I only print the gamesplayed without incrementing it because I put keep track of it in the isWinner() and boardIsFull() function.
        #The result is accurate when testing.
        print(self.__gamesplayed__)


    def resetGameBoard(self) -> None:
        """Clear all the moves from game board.
        """
        print("board resetted.")
        self.__gameover__ = False
        self.__actualgame__ = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        

    def updateGameBoard(self, x_or_o: str = " ", playernum : int = 0) -> None:
        """Updates the game board with the player's move

        Args:
            x_or_o: player's chess representor.
            playernum: player's entered number.
        """
        if playernum == 0 or x_or_o == " ":
            pass
        elif playernum > 9 or playernum < 0:
            print("invalid movement, please enter another positional number.")
        else:
            programnum = playernum - 1
            self.__actualgame__[programnum] = self.__actualgame__[programnum].replace(" ", x_or_o.upper())

    
    def isWinner(self) -> None:
        """Checks if the latest move resulted in a win. Updates the wins and losses count
        """
        
        if (self.__actualgame__[0] == self.__actualgame__[1] == self.__actualgame__[2] == "X") or (self.__actualgame__[3] == self.__actualgame__[4] == self.__actualgame__[5] == "X") or (self.__actualgame__[6] == self.__actualgame__[7] == self.__actualgame__[8] == "X"):
            print("P1 wins!")
            self.__P1_wins__ += 1
            self.__P2_losses__ += 1
            self.__gamesplayed__ += 1
            self.__gameover__ = True
        if (self.__actualgame__[0] == self.__actualgame__[1] == self.__actualgame__[2] == "O") or (self.__actualgame__[3] == self.__actualgame__[4] == self.__actualgame__[5] == "O") or (self.__actualgame__[6] == self.__actualgame__[7] == self.__actualgame__[8] == "O"):
            print("P2 wins!")
            self.__P1_losses__ += 1
            self.__P2_wins__ += 1
            self.__gamesplayed__ += 1
            self.__gameover__ = True
        if (self.__actualgame__[0] == self.__actualgame__[3] == self.__actualgame__[6] == "X") or (self.__actualgame__[1] == self.__actualgame__[4] == self.__actualgame__[7] == "X") or (self.__actualgame__[2] == self.__actualgame__[5] == self.__actualgame__[8] == "X"):
            print("P1 wins!")
            self.__P1_wins__ += 1
            self.__P2_losses__ += 1
            self.__gamesplayed__ += 1
            self.__gameover__ = True
        if (self.__actualgame__[0] == self.__actualgame__[3] == self.__actualgame__[6] == "O") or (self.__actualgame__[1] == self.__actualgame__[4] == self.__actualgame__[7] == "O") or (self.__actualgame__[2] == self.__actualgame__[5] == self.__actualgame__[8] == "O"):
            print("P2 wins!")
            self.__P1_losses__ += 1
            self.__P2_wins__ += 1
            self.__gamesplayed__ += 1
            self.__gameover__ = True
        if (self.__actualgame__[0] == self.__actualgame__[4] == self.__actualgame__[8] == "X") or (self.__actualgame__[2] == self.__actualgame__[4] == self.__actualgame__[6] == "X"):
            print("P1 wins!")
            self.__P1_wins__ += 1
            self.__P2_losses__ += 1
            self.__gamesplayed__ += 1
            self.__gameover__ = True
        if (self.__actualgame__[0] == self.__actualgame__[4] == self.__actualgame__[8] == "O") or (self.__actualgame__[2] == self.__actualgame__[4] == self.__actualgame__[6] == "O"):
            print("P2 wins!")
            self.__P1_losses__ += 1
            self.__P2_wins__ += 1
            self.__gamesplayed__ += 1
            self.__gameover__ = True

    
    def boardIsFull(self) -> None:
        """Checks if the board is full (I.e. no more moves to make - tie) Updates the ties count
        """
        for space in self.__actualgame__:
            if space == ' ':
                self.__roundsplayed__ += 0
            elif space != ' ':
                self.__roundsplayed__ += 1
        if self.__roundsplayed__ == 9:
            self.__Number_of_ties__ += 1
            print("tie game")
            self.__gamesplayed__ += 1
            self.__gameover__ = True
        else:
            self.__roundsplayed__ = 0

    
    def printStats(self) -> None:
        """Prints the information of the game's played
        """
        print("player1's username:", self.__Players_user_name1__, "player2's username:", self.__Players_user_name2__)
        print("last player to have a turn:", self.__User_name_of_the_last_player_to_have_a_turn__)
        print("number of games played:", self.__gamesplayed__)
        print("player1 win/s:", self.__P1_wins__, "player2 wins:", self.__P2_wins__)
        print("player1 loss/es:", self.__P1_losses__, "player2 loss/es:", self.__P2_losses__)
        print("number of ties:", self.__Number_of_ties__)


    def printboard(self) -> None:
        """print the gameboard.
        """
        print(f"{self.__actualgame__[0]}|{self.__actualgame__[1]}|{self.__actualgame__[2]}\n-+-+-\n{self.__actualgame__[3]}|{self.__actualgame__[4]}|{self.__actualgame__[5]}\n-+-+-\n{self.__actualgame__[6]}|{self.__actualgame__[7]}|{self.__actualgame__[8]}")

        
    def checkifgameover(self) -> bool:
        """check if the game is over.

        Returns:
            True if the game is over. False if the game is not over.
        """
        if self.__gameover__ == True:
            return True
        if self.__gameover__ == False:
            return False

        
    def updateuser(self, playerID: str = "") -> None:
        """updates the user ID.

        Args:
            playerID: last player to have the turn identifier.
        """
        self.__User_name_of_the_last_player_to_have_a_turn__ = playerID


    def checkifrepeat(self, playermove: int) -> bool:
        """check if the step is repetitive.

        Returns:
            True if the game is over. False if the game is not over.
        """
        if self.__actualgame__[playermove - 1] != ' ':
            print("space occupied, please try again")
            return True
        else:
            return False

    
