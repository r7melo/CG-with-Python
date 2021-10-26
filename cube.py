from app import App

from OpenGL.GL import *

from vector import Vector3d


class Cube:
    def __init__(self, verticies, faces, colors):
        self.__verticies__ = verticies
        self.verticies = verticies
        self.faces = list(faces)
        self.colors = colors
        self.angle = Vector3d(0,0,0)
        self.render = list(range(len(faces)))
        self.inverte_x = True

    def rotate(self):
        new_verticies = []

        for vertex in self.__verticies__:
            vector = Vector3d(vertex[0], vertex[1], vertex[2])
            vector.rotate(self.angle, Vector3d(0,0,0))
            new_verticies.append(vector.get())
            
        self.verticies = tuple(new_verticies)

        if abs(self.angle.x) >= 360:
            self.angle.x = 0
        if abs(self.angle.y) >= 360:
            self.angle.y = 0



    def show(self):
        if 180 <= self.inverte_x and abs(self.angle.x) <= 360:
            A = self.render[0]
            B = self.render[1]
            self.render[0] = B
            self.render[1] = A
            self.inverte_x = False
        else:
            self.inverte_x = True


        glBegin(GL_QUADS)
        for face in range(len(self.faces)):
            glColor3fv(self.colors[self.render[face]])
            for vertex in self.faces[face]:
                glVertex3fv(self.verticies[vertex])
        glEnd()

        print(self.angle.get())
        



    def update(self):
        self.show()
        self.rotate()

        self.angle.y += 1
        self.angle.x += 0.2
        #self.angle.y += 0.1
        #self.angle.x += 0.1

        print(self.render)

        


cuboVerticies = (
    (0,0,0),
    (1,0,0),
    (1,1,0),
    (0,1,0),

    (0,0,-1),
    (1,0,-1),
    (1,1,-1),
    (0,1,-1),
)

cuboFaces = (
    (4,5,6,7),    #1
    (0,1,2,3),    #3
)

cuboColors = (
    (1,0,0),   
    (0,1,0),   
)



cuboFacesbc= (
    ((1,0,0),0,1,2,3),          #3
    ((1,1,0),0,1,5,4),          #4
    ((1,1,1),0,4,7,3),          #5
    ((0,1,1),3,2,6,7),          #2
    ((0,0,1),1,2,6,5),          #6
    ((0.1,0.1,0.1),4,5,6,7),    #1
)



if __name__=="__main__":
        from cartesian_plane import CartesianPlane
        app = App()
        app.screenSize = (1500,900)
        app.render.append(CartesianPlane())
        app.render.append(Cube(cuboVerticies, cuboFaces, cuboColors))
        app.run()
