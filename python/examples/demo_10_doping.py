# [RMS] This file demos some spatial query functions:
#    - get bounding box of selected object
#    - find ray/surface intersection
#    - find nearest point on surface to query point
#    - conversion between Scene and World coordinates

import mmapi
from mmRemote import *
import mm
from mm.mm_math import *

# initialize connection
r = mmRemote()
r.connect()


numberOfRaysHorizontal = 10
numberOfRaysVerticle = 10

(fMin,fMax) = mm.get_selected_bounding_box(r)

fMinW = mm.to_world(r, fMin)
fMaxW = mm.to_world(r, fMax)

width = fMaxW[2] - fMinW[2]
height = fMaxW[0] - fMinW[0]



# construct a ray from far-away-pt through center of bbox, along +Z axis
center = lerpv3(fMin, fMax, 0.5)
diag = subv3(fMax, fMin)
ray_dir = (0.0,0.0,1.0)
ray_origin = subv3(center, mulv3s(ray_dir, 25.0*max(diag)))


(bOK,hitFrames) = mm.find_ray_hit_all(r, ray_origin, ray_dir)

if not bOK:
    r.shutdown()

if len(hitFrames) %2 == 1:
    print 'not a solid object'
    r.shutdown()

r.shutdown()



