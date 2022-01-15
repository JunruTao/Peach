# VEX include script

Include external script into vex:

1. create an `add` node, create 2 points in there. Then, create a point `wrangle` node, append it to the `add` node
2. write following:
   
    ```c
    #include "$HIP/something.vfl"
    i@v = Foo(@ptnum);
    printf("hey%d\n", i@v);
    ```
    also works with `<>`
    ```c
    #include <$HIP/something.vfl>
    i@v = Foo(@ptnum);
    printf("hey%d\n", i@v);
    ```
3. in your `$HIP` location, create file `something.vfl`. write:
    ```c
    int Foo(int var)
    {
        printf("Foo: %d\n", var);
        return var * 3;
    }
    ```

you should be able to get results in console:
```
>>> Foo: 0
>>> Foo: 1
>>> hey0
>>> hey3
```