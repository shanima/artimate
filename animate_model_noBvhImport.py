#python code for creating a model dependent on the bvh input.
#Marina Oberwegner

# imports
import os, sys, re
#import "C:\\Users\\Marina\\Documents\\artimate\\src\\____model.blend"

# import blender modules
try:
    import bpy
    from mathutils import Vector
except ImportError:
    sys.exit("This script must be run with blender, not python!")
    
# check poll() to avoid exception.
#if bpy.ops.object.mode_set.poll():
#    bpy.ops.object.mode_set(mode='EDIT')


# import custom modules
sys.path.append("${project.build.outputDirectory}")


# imports .bvh file into .blend project
def readBvh(bvhFilename):
    bpy.ops.object.select_all(action='DESELECT')
    bvhFilepath = "C:\\Users\\Marina\\Documents\\artimate\\src\\"
    if bvhFilename is "":
        bvhFilename = "msak0_001"
    bpy.context.scene.objects.active
    bpy.ops.import_anim.bvh(filepath=r'C:\Users\Marina\Documents\artimate\src\msak0_001.bvh', axis_forward='Z', axis_up='Y')
        
# load model by opening .blend file containing the model
def loadModel():
    bpy.ops.wm.open_mainfile(filepath="C:\\Users\\Marina\\Documents\\artimate\\src\\projectModel_withBvh.blend")
    
# connect bvh input to model objects
def trackBvh(bvhFilename): 
    if bvhFilename is "":
        bvhFilename = "msak0_001"
    #bvh 
    bpy.ops.object.select_all(action='DESELECT')
    bvh = bpy.data.objects.get(bvhFilename) 
    bvh.select  = True #selects bvhInput object
    bpy.data.objects[bvhFilename].parent = bpy.data.objects['Empty'] #put the imported file into correct position
    bpy.ops.object.select_all(action='DESELECT')
    #armature tongue tip
    armature_tt = bpy.data.objects.get("armature_tt")
    armature_tt.select = True
    constraint_tt = armature_tt.constraints.new('COPY_LOCATION')
    bpy.data.objects['armature_tt'].constraints["Copy Location"].target = bpy.data.objects[bvhFilename]
    bpy.data.objects['armature_tt'].constraints["Copy Location"].subtarget = "tt"
    bpy.ops.object.select_all(action='DESELECT')
    #armature tongue blade
    armature_tb = bpy.data.objects.get("armature_tb")
    armature_tb.select = True
    constraint_tb = armature_tb.constraints.new('COPY_LOCATION')
    bpy.data.objects['armature_tb'].constraints["Copy Location"].target = bpy.data.objects[bvhFilename]
    bpy.data.objects['armature_tb'].constraints["Copy Location"].subtarget = "tb"
    bpy.ops.object.select_all(action='DESELECT')
    #armature tongue dorsum
    armature_td = bpy.data.objects.get("armature_td")
    armature_td.select = True
    constraint_td = armature_td.constraints.new('COPY_LOCATION')
    bpy.data.objects['armature_td'].constraints["Copy Location"].target = bpy.data.objects[bvhFilename]
    bpy.data.objects['armature_td'].constraints["Copy Location"].subtarget = "td"
    # track mandible to the jaw
    bpy.ops.object.select_all(action='DESELECT')
    mandible = bpy.data.objects.get("Mandible")
    mandible.select = True
    constraint_mandible = mandible.constraints.new('TRACK_TO')
    bpy.data.objects['Mandible'].constraints["Track To"].target = bpy.data.objects[bvhFilename]
    bpy.data.objects['Mandible'].constraints["Track To"].subtarget = "li" #jaw
    bpy.data.objects['Mandible'].constraints["Track To"].track_axis = 'TRACK_X'
    bpy.data.objects['Mandible'].constraints["Track To"].up_axis = "UP_Z"
    # bone for jaw movement
    bpy.ops.object.select_all(action='DESELECT')
    armature_jawRotation = bpy.data.objects.get("Armature_jawRotation")
    armature_jawRotation.select = True
    constraint_jawRotation = armature_jawRotation.constraints.new('LOCKED_TRACK')
    bpy.data.objects['Armature_jawRotation'].constraints["Locked Track"].target = bpy.data.objects[bvhFilename]
    bpy.data.objects['Armature_jawRotation'].constraints["Locked Track"].subtarget = "li"
    constraint_jawRotation = armature_jawRotation.constraints.new('CHILD_OF')
    bpy.data.objects['Armature_jawRotation'].constraints["Child Of"].target = bpy.data.objects["Mandible"]
    bpy.ops.object.select_all(action='DESELECT')
    
if __name__ == '__main__':
    bvhFilename = ""    
    # new code added
    #bvhFilename = raw_input('Please enter the name of the bvh file')
    if bvhFilename is "":
        bvhFilename = "msak0_001"
    loadModel()  
    #readBvh(bvhFilename)
    trackBvh(bvhFilename)
