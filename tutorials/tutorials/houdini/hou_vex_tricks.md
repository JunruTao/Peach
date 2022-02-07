# Vex Tricks:

## Content:
- [Vex Tricks:](#vex-tricks)
  - [Content:](#content)
  - [Get a primitive(polyline) length:](#get-a-primitivepolyline-length)

## Get a primitive(polyline) length:
```c
//run over primitive
float len = primuvconvert(0, 1, @primnum, PRIMUV_UNIT_TO_LEN);
//-------------------->(geo, uv, prim number,  mode[enum]   )
```