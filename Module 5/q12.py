"""
question:  Describe a scenario where using a tuple would be preferable over a list.
Answer: In building a program to represent geographical coordinates of points on a map. we need to
        store a point's latitude and longitude values, and these values should never change 
        during the program's execution because they represent fixed locations.
        
        In this case tuple is more preferable over lists because Once a tuple is created, 
        its contents cannot be modified. This ensures that the coordinates (latitude and 
        longitude) cannot be accidentally changed during the program's execution, which 
        helps maintain the integrity of the data.

"""       