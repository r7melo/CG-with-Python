class Vector3d:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def sum(self, vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def get(self):
        return (self.x, self.y, self.z)
