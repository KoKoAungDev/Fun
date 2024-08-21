class MarsRover:
    def __init__(self, x, y, direction):
        self.x = x  # x-coordinate on the grid
        self.y = y  # y-coordinate on the grid
        self.direction = direction  # current direction the rover is facing
        self.directions = ['N', 'E', 'S', 'W']  # possible directions

    def turn_left(self):
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index - 1) % 4]  # turn left

    def turn_right(self):
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index + 1) % 4]  # turn right

    def move_forward(self):
        if self.direction == 'N':
            self.y += 1  # move north (increase y-coordinate)
        elif self.direction == 'E':
            self.x += 1  # move east (increase x-coordinate)
        elif self.direction == 'S':
            self.y -= 1  # move south (decrease y-coordinate)
        elif self.direction == 'W':
            self.x -= 1  # move west (decrease x-coordinate)

    def execute_commands(self, commands):
        for command in commands:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'F':
                self.move_forward()
            else:
                raise ValueError(f"Invalid command: {command}")

    def get_position(self):
        return self.x, self.y, self.direction


# Simulation example
if __name__ == "__main__":
    # Initial position (0, 0) facing North ('N')
    rover = MarsRover(0, 0, 'N')
    
    # Command sequence: Move forward, turn right, move forward, turn left, move forward
    commands = "FRFLF"
    
    # Execute the commands
    rover.execute_commands(commands)
    
    # Get the final position and direction
    position = rover.get_position()
    
    print(f"Rover's final position: (x={position[0]}, y={position[1]}), facing {position[2]}")
