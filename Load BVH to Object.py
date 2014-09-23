# Program Aimed at Iterating to each Shape Key to Add A Driver. 
import bpy
selectedObj= bpy.context.object
selectedObjShapeKeys= selectedObj.data.shape_keys
selectedObjShapeKeysNameArray= selectedObjShapeKeys.key_blocks
k=0
for each in selectedObjShapeKeysNameArray:
    print(each)
    x=1
    if k==0:
        #print(each)
        x=1
    else:
        driverData= bpy.data.shape_keys['Key.001'].key_blocks[k].driver_add("value",-1)
        drv= driverData.driver
        drv.type="SCRIPTED"
        drv.expression="var*-2/pi"#one can modifiy this to lessen the empact of the specifed driver.
        var= drv.variables.new()
        var.name="var"
        var.type="TRANSFORMS"
        targ= var.targets[0]
        # This is where one replaces the one in the bracket with the name of the 
	# bvh file; 
        val=bpy.data.objects['rotFinalBasicCheck']
        targ.id=val
        blendList=("EyeBlink_L","EyeBlink_R","EyeSquint_L","EyeSquint_R","EyeDown_L","EyeDown_R","EyeIn_L","EyeIn_R","EyeOpen_L","EyeOpen_R","EyeOut_L","EyeOut_R","EyeUp_L","EyeUp_R","BrowsD_L","BrowsD_R","BrowsU_C","BrowsU_L","BrowsU_R","JawFwd","JawLeft","JawOpen","JawChew","JawRight","MouthLeft","MouthRight","MouthFrown_L","MouthFrown_R","MouthSmile_L","MouthSmile_R","MouthDimple_L","MouthDimple_R","LipsStretch_L","LipsStretch_R","LipsUpperClose","LipsLowerClose","LipsUpperUp","LipsLowerDown","LipsUpperOpen","LipsLowerOpen","LipsFunnel","LipsPucker","ChinLowerRaise","ChinUpperRaise","Sneer","Puff","CheekSquint_L","CheekSquint_R")
        targ.bone_target=blendList[k-1] # Must Set these to Bone
        targ.transform_type="ROT_Z"
    k= k + 1
