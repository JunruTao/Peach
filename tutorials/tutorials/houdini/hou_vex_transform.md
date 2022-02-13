# Vex Transforms

## Packed Transforms:

- set transforms:
```c
matrix M = maketransform(XFORM_SRT, XFORM_XYZ, v@T, v@R, v@S * f@pscale, {0,0,0}); 
packedtransform(0, @primnum, M);
```

- get transfroms:
```c
matrix M = getpackedtransform(0, @primnum);
v@t;v@r;v@s;
cracktransform(XFORM_SRT, XFORM_XYZ, {0,0,0}, M, v@t, v@r, v@s);
```
