board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def insertletter(letter, pos):
    board[pos] = letter

def freespacecheck(pos):
    return board[pos] == ' '

def pboard(b):
    print(f'{b[1]}|{b[2]}|{b[3]}\n-----\n{b[4]}|{b[5]}|{b[6]}\n-----\n{b[7]}|{b[8]}|{b[9]}\n')

def winnercheck(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playermove():
    run = True
    while run:
        move = input('where do you want to place your - X - ?')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freespacecheck(move):
                    run = False
                    insertletter('X', move)
                else:
                    print('place-occupied')
            else:
                print('num is out of range, it should be from 1-9')
        except:
            print('you typed a blank space')


def moveO():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if winnercheck(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = randomselector(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = randomselector(edgesOpen)

    return move

def randomselector(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def isboardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    pboard(board)

    while not(isboardfull(board)):
        if not(winnercheck(board, 'O')):
            playermove()
            pboard(board)
        else:
            print('computer has won this time -O- ')
            break

        if not(winnercheck(board, 'X')):
            move = moveO()
            if move == 0:
                print('tie')
            else:
                insertletter('O', move)
                print('--'*10)
                pboard(board)
        else:
            print('X is the winner')
            break

    if isboardfull(board):
        print('Tie Game!')

while True:
    answer = input('to play, press y. press any other key to quit.')
    if answer == 'y':
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        print('-----------------------------------')
        main()
    else:
        break
