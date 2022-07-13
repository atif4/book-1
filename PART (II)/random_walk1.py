from random import choice
class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1])
            x_distance = choice([0,1,2,3,4,5,6,7,8])
            x_step = x_direction * x_distance
            #print(x_step)
            #print(x_direction)
            #print(x_distance)
            y_direction = choice([1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            # Calculate the next x and y values.
            next_x = self.x_values[1] + x_step
            next_y = self.y_values[1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
#a = RandomWalk()
#print(a)
#print(a.fill_walk())