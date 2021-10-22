import math

class Vector3d:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def sum(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def rotate(self, anglev):
        if abs(anglev.x) > 0:
            self.y = (self.y * math.cos((anglev.x/180)*math.pi)) - (self.z * math.sin((anglev.x/180)*math.pi))
            self.z = (self.y * math.sin((anglev.x/180)*math.pi)) + (self.z * math.cos((anglev.x/180)*math.pi))
        if abs(anglev.y) > 0:
            self.x = (self.x * math.cos((anglev.y/180)*math.pi)) - (self.z * math.sin((anglev.y/180)*math.pi))
            self.z = (self.z * math.sin((anglev.y/180)*math.pi)) + (self.z * math.cos((anglev.y/180)*math.pi))
        if abs(anglev.z) > 0:
            self.x = (self.x * math.cos((anglev.z/180)*math.pi)) - (self.y * math.sin((anglev.z/180)*math.pi))
            self.y = (self.x * math.sin((anglev.z/180)*math.pi)) + (self.y * math.cos((anglev.z/180)*math.pi))

    def get(self):
        return (self.x, self.y, self.z)
