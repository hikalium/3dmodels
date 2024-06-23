# $ blender --version
# Blender 3.4.1
# blender -P chrome-chan.py

import bpy
import math
import mathutils

# Prevent showing splash screen
bpy.context.preferences.view.show_splash = False

while(len(bpy.data.meshes)):
    bpy.data.meshes.remove(bpy.data.meshes[0])

while(len(bpy.data.objects)):
    bpy.data.objects.remove(bpy.data.objects[0])

print("hello");

verts = []
verts.append([1, 1, 0])
verts.append([1, -1, 0])
verts.append([-1, 1, 0])
verts.append([0, 0, 1])
edges = []
faces = []
faces.append([1, 2, 3])
faces.append([1, 2, 0])

mesh = bpy.data.meshes.new(name = "mesh0")
mesh.from_pydata(verts, edges, faces)
obj = bpy.data.objects.new("object0", mesh)
bpy.context.scene.collection.objects.link(obj)
