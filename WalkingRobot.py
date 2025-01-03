class WalkingRobot:
    """
    Problem: Given a robot which can only move in four directions, UP(U), DOWN(D), LEFT(L), RIGHT(R).
    Given a string consisting of instructions to move.
    Output the coordinates of a robot after executing the instructions.
    Initial position of robot is at origin(0, 0).

    Logic: Just count the numbers of U,L,D and R in the given string. The final x-coordinate will be
    countRight - countLeft and final y-coordinate will be countUp - countDown. We can also run
    a loop through the string and check every character and then update our x & y
    """

    def walkingRobot1(self, instructions) -> list[int]:
        x, y = 0, 0
        for char in instructions:
            if char=='U':
                y += 1
            elif char=='D':
                y -= 1
            elif char=='R':
                x += 1
            else:
                x -= 1

        res = [x,y]
        return res

    def walkingRobot2(self, instructions) -> list[int]:
        left, right, up, down = 0,0,0,0
        for char in instructions:
            if char=='U':
                up += 1
            elif char=='D':
                down += 1
            elif char=='L':
                left += 1
            else:
                right += 1

        res = [right-left, up-down]
        return res

    def main(self):
        instructions = "UDDLRL"
        print(self.walkingRobot1(instructions))
        print(self.walkingRobot2(instructions))


robot = WalkingRobot()
robot.main()
