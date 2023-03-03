#sever
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
    message = connectionSocket.recv(20).decode('ascii')
    print(message)
    if message == "Fun Times":
        A.printStats()
        return False
    if message == "Play Again":
        A.resetGameBoard()
        return True

    
serverAddress = input("please create the serverIP:")
port = int(input("please input the serverport:"))
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverAddress,port))
print("server created, waiting for connections")
serverSocket.listen(5)
connectionSocket,connectionAddress = serverSocket.accept()
print("Client connected from: ",connectionAddress)
P1_name = connectionSocket.recv(20).decode('ascii')
print("opponent:",P1_name)
connectionSocket.sendall(b'player2')
A = gameboard.BoardClass(P1_name, "player2")
while True:
    P1_move = int(connectionSocket.recv(20).decode('ascii'))
    A.updateGameBoard("x",P1_move)
    A.updateuser(P1_name)
    checkstatus(A)
    if A.checkifgameover():
        T = aftergameover(A)
        if T == True:
            continue
        else:
            break
    while True:
        P2_move = input("please input your move using integer 1 through 9, enter m to see the number reference.")
        while True:
            if P2_move == "m":
                print(f"1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9")
            try:
                P2_move = int(P2_move)
                if (P2_move < 1 or P2_move > 9):
                    print("number out of range. please try again")
                    P2_move = input("please input your move using integer 1 through 9:")
                else:
                    break
            except:
                print("invalid entry given, please try again.")
                P2_move = input("please input your move using integer 1 through 9:")
        if A.checkifrepeat(P2_move):
            continue
        else:
            break
    A.updateGameBoard("o",P2_move)
    A.updateuser("player2")
    checkstatus(A)
    print("waiting for player1's response...")
    connectionSocket.sendall(str(P2_move).encode('ascii'))
    if A.checkifgameover():
        T = aftergameover(A)
        if T == True:
            continue
        else:
            break
connectionSocket.close()
