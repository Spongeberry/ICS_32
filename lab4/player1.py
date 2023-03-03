#client
import socket
import gameboard


def checkstatus(self) -> None:
    """check if the game is over and do the following steps.
    """
    self.printboard()
    self.isWinner()
    self.boardIsFull()


def aftergameover(self) -> bool:
    """things to operate after the game is over for p1.

    Return:
        True if p1 wants to play again.
        False if p1 dont wants to play again.
    """
    print("gameover, enter y/Y to send \"Play Again\" to player 2:")
    print("or enter n/N to send \"Fun Times\" to player 2 and end the game.")
    response = input()
    if response == "y" or response == "Y":
        connectionSocket.sendall(("Play Again").encode('ascii'))
        A.resetGameBoard()
        return True
    elif response == "n" or response == "N":
        connectionSocket.sendall(("Fun Times").encode('ascii'))
        return False
        

serverAddress = input("please provide server IP:")
serverPort = int(input("please provide port:"))
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        connectionSocket.connect((serverAddress,serverPort))
        break
    except ConnectionRefusedError:
        user_int = input("connection not found, enter y to find another serveraddress and port, enter n to end the program and see stats")
        if user_int == "y":
            serverAddress = input("please input player2 IP again:")
            serverPort = int(input("please provide port:"))
        elif user_int == "n": 
            quit()


user_name = input("please input your user name or press g to send the computer/'s name")
if user_name == "g":
    connectionSocket.sendall(socket.gethostname().encode('ascii'))
    user_name = socket.gethostname()
else:
    connectionSocket.sendall(user_name.encode('ascii'))
B = connectionSocket.recv(20).decode('ascii')
print("opponent:",B)
print(f"1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9")
A = gameboard.BoardClass(user_name,"player2")

while True:
    P1_move = input("please input your move using integer 1 through 9:")
    while True:
        try:
            P1_move = int(P1_move)
            if (P1_move < 1 or P1_move > 9):
                print("number out of range. please try again")
                P1_move = input("please input your move using integer 1 through 9:")
            else:
                break
        except:
            print("invalid entry given, please try again.")
            P1_move = input("please input your move using integer 1 through 9:")
    if A.checkifrepeat(P1_move):
        continue
    else:
        pass
    A.updateGameBoard("x",P1_move)
    A.updateuser(user_name)
    checkstatus(A)
    connectionSocket.sendall(str(P1_move).encode('ascii'))
    if A.checkifgameover():
        T = aftergameover(A)
        if T == True:
            continue
        else:
            break
    print("waiting for player2's response...")
    P2_move = connectionSocket.recv(20).decode('ascii')
    P2_move = int(P2_move)
    A.updateGameBoard("o",P2_move)
    A.updateuser("player2")
    checkstatus(A)
    if A.checkifgameover():
        T = aftergameover(A)
        if T == True:
            continue
        else:
            break
A.printStats()
connectionSocket.close()
