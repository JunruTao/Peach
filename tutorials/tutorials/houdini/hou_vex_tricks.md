# Vex Tricks:

## Content:
- [Vex Tricks:](#vex-tricks)
  - [Content:](#content)
  - [Get a primitive(polyline) length:](#get-a-primitivepolyline-length)
  - [Check if its closed polygon](#check-if-its-closed-polygon)

## Get a primitive(polyline) length:
```c
//run over primitive
float len = primuvconvert(0, 1, @primnum, PRIMUV_UNIT_TO_LEN);
//-------------------->(geo, uv, prim number,  mode[enum]   )
```

## Check if its closed polygon

```c
//run over prim
int closed = primintrinsic(geoself(), "closed", @primnum);
```