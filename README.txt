@author Marina Oberwegner
Refering to report on the project.

To get the project working you need:

- projectModel_withBvh.blend   which contains the model

- animate_model_noBvhImport.py this script should be run to get all the connections in the blend file. Then you can play the animation from the blend file opened.

- build.gradle  run task runBlender

Please make sure you change the path in the python script!!

Note: In this version you can import another bvhFile manually in the .blend file. Please make sure you use: axis_forward='Z', axis_up='Y'.