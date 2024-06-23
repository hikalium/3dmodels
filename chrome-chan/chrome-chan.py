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

bpy.ops.mesh.primitive_uv_sphere_add(segments=60,ring_count=30, radius=2.0)
obj1 = bpy.context.active_object
obj1.name = "sphere"

bpy.ops.mesh.primitive_cylinder_add(vertices=3, radius=2.0, depth=4.0)
obj2 = bpy.context.active_object
obj2.name = "triangle"

bpy.ops.mesh.primitive_cylinder_add(vertices=60, radius=1.0, depth=4.0)
obj0 = bpy.context.active_object
obj0.name = "cylinder"

bpy.context.view_layer.objects.active.select_set(False)
bpy.context.view_layer.objects.active = obj1
bpy.context.view_layer.objects.active.select_set(True)
bpy.ops.transform.resize(value=(1, 1, 0.4))

bpy.context.view_layer.objects.active.select_set(False)
bpy.context.view_layer.objects.active = obj1
bpy.context.view_layer.objects.active.select_set(True)
bool1 = obj1.modifiers.new(type="BOOLEAN", name="bool1")
bool1.object = obj2
bool1.operation = 'DIFFERENCE'
bool1.solver = 'EXACT'
bpy.ops.object.modifier_apply(modifier=bool1.name)

#bpy.context.view_layer.objects.active.select_set(False)
#bpy.context.view_layer.objects.active = obj1
#bpy.context.view_layer.objects.active.select_set(True)
#bool0 = obj1.modifiers.new(type="BOOLEAN", name="bool0")
#bool0.object = obj0
#bool0.operation = 'DIFFERENCE'
#bpy.ops.object.modifier_apply(modifier=bool0.name)

bpy.context.view_layer.objects.active.select_set(False)
bpy.context.view_layer.objects.active = obj0
bpy.context.view_layer.objects.active.select_set(True)

bpy.ops.transform.resize(value=(0.8, 0.8, 0.5))
# bpy.context.object.hide_set(True)

areas  = [area for area in bpy.context.window.screen.areas if area.type == 'VIEW_3D']
for area in areas:
    with bpy.context.temp_override(
        window=bpy.context.window,
        area=area,
        region=[region for region in area.regions if region.type == 'WINDOW'][0],
        screen=bpy.context.window.screen
    ):
        bpy.ops.view3d.view_axis(type='TOP', align_active=False)
        bpy.ops.view3d.view_persportho()



# verts = []
# verts.append([1, 1, 0])
# verts.append([1, -1, 0])
# verts.append([-1, 1, 0])
# verts.append([0, 0, 1])
# edges = []
# faces = []
# faces.append([1, 2, 3])
# faces.append([1, 2, 0])
# mesh = bpy.data.meshes.new(name = "mesh0")
# mesh.from_pydata(verts, edges, faces)
# obj = bpy.data.objects.new("object0", mesh)
# bpy.context.scene.collection.objects.link(obj)
