# Houdini Parameter Interface:

## Table Of Content
- [Houdini Parameter Interface:](#houdini-parameter-interface)
  - [Table Of Content](#table-of-content)
  - [1. Disable and Hide Param](#1-disable-and-hide-param)
    - [1.1 When Another Param change values:](#11-when-another-param-change-values)
    - [1.2 Base on Input change, parameter name:](#12-base-on-input-change-parameter-name)
    - [1.3 reference](#13-reference)


## 1. Disable and Hide Param

### 1.1 When Another Param change values:

- Disable/Hide Param When
  
| `{ parm1 == 1 }` |
|--|

| `{ parm1 > 10 }` |
|--|

| :warning: Note: <br> You must put spaces around the comparison operator, otherwise Houdini will not accept the rule.|
|---|

- __And__ (`&&`) statement syntax

|`{ enablefeature == 1 count > 10 }`|
|---|

- __Or__(`||`) statement syntax

|`{ type == 1 } { count > 10 }`|
|---|


### 1.2 Base on Input change, parameter name:

Input Count:

- `ninputs()`
   > The highest wired input number. This may be more than the number of wires if inputs in the middle are not connected. It also counts subnet inputs that may not be wired in the parent node.

Has Input: (plugged)

- `hasinput(n)`
    > Returns 1 if the given input number is connected, or 0 if not. This does not count an input wired into a subnet input if that input is not also wired in the parent node.

| `{ hasinput(1) == 1 }` |
|---|

| :warning: Note Again!!: <br> You must put _`spaces`_ around the comparison operator, otherwise Houdini will not accept the rule.|
|---|

- `isparm(parmname)` 
  > Returns 1 if this parameter’s name is parmname. This is meant for use with multiparm items.

### 1.3 reference
> https://www.sidefx.com/docs/houdini19.0/ref/windows/optype.html#conditions