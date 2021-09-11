'''
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's
not easy building a doomsday device and ordering the bunnies around at the same time, after all! In order to make sure
that everyone is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman
dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order
to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight.
Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday
device!

To help yourself get to and from your bunk every day, write a function called solution(src, dest) which takes in two
parameters: the source square, on which you start, and the destination square, which is where you need to land to solve
the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to
travel from the source square to the destination square using a chess knight's moves (that is, two squares in any
direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the
source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example
chessboard below:

-------------------------
| 0| 1| 2| 3| 4| 5| 6| 7|
-------------------------
| 8| 9|10|11|12|13|14|15|
-------------------------
|16|17|18|19|20|21|22|23|
-------------------------
|24|25|26|27|28|29|30|31|
-------------------------
|32|33|34|35|36|37|38|39|
-------------------------
|40|41|42|43|44|45|46|47|
-------------------------
|48|49|50|51|52|53|54|55|
-------------------------
|56|57|58|59|60|61|62|63|
-------------------------
'''









class KnightMoves:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
        self.children = []                  # list of "next steps" we can take
        self.steps = []                     # number of steps from src
        self.board = {}                     # dict of i: (x,y) values where i is the board #, x is the row, and y is the column
        self.done = False
        self.childIndex = 0
        # self.fillBoard(8)
    def fillBoard(self, n):
        self.children.append(self.src)
        self.steps.append(0)
        for i in range(n * n):
            row = i // n
            col = i % n
            self.board[i] = (row, col)
    def nextStepsDriver(self):
        self.nextSteps(self.children[self.childIndex])
        self.childIndex = self.childIndex + 1
    def nextSteps(self, position):
        row = self.board[position][0]
        col = self.board[position][1]
        parentIndex = self.children.index(position)
        parentStep = self.steps[parentIndex]
        a = (row - 2, col - 1)
        b = (row - 2, col + 1)
        c = (row - 1, col + 2)
        d = (row + 1, col + 2)
        e = (row + 2, col + 1)
        f = (row + 2, col - 1)
        g = (row + 1, col - 2)
        h = (row - 1, col - 2)
        self.validPt(a, parentStep)
        self.validPt(b, parentStep)
        self.validPt(c, parentStep)
        self.validPt(d, parentStep)
        self.validPt(e, parentStep)
        self.validPt(f, parentStep)
        self.validPt(g, parentStep)
        self.validPt(h, parentStep)
    def validPt(self, new_point, parentStep):
        for key, value in self.board.items():
            if (value == new_point):
                self.addToChildren(key, parentStep)
    def addToChildren(self, item, parentStep):
        if item not in self.children:
            self.children.append(item)
            self.steps.append(parentStep + 1)
            self.areWeThereYet(item)
    def printChildren(self):
        for i in range(len(self.children)):
            print(self.children[i], "\t", self.steps[i])
    def areWeThereYet(self, item):
        if item == self.dest:
            ansIndex = self.children.index(item)
            self.step = self.steps[ansIndex]     # this is the answer
            print("ok ", self.step)
            self.done = True


def solution(src, dest):
    # Your code here
    if src == dest:
        return 0
    bunnyHop = KnightMoves(src, dest)
    bunnyHop.fillBoard(8)
    while (bunnyHop.done != True):
        bunnyHop.nextStepsDriver()
    return bunnyHop.step


def main():
    n = solution(0, 0)



main()