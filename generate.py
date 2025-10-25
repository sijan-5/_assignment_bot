import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
for x in range(5):
    for y in range(5):
        initial_length = 1
        initial_width = 1
        initial_height = 1
        z = initial_height / 2
        for i in range(10):
            pyrosim.Send_Cube(name="box", pos=[x, y, z], size=[initial_length, initial_width, initial_height])
            z += initial_height
            initial_length *= 0.9
            initial_width *= 0.9
            initial_height *= 0.9

pyrosim.End()


