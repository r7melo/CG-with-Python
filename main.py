from app import App
from vector import Vector3d

app = App()

app.display = (800,800)
app.fovy = 45
app.z_near = 1
app.z_far = 100
app.translation = Vector3d(0, 0, -5)
app.run()