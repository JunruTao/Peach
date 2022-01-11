# Change Logs

* [>>>>> Change Logs Entry](./ChangeLog.md)

-----
## Documentation Tasks and Notes
- :yellow_square: **Documentation Tools**
    - [x] --- date-time based changeLogs auto generator. create new changeLog files according to the date, and append new changes to that date's changeLog with timestamps. <sup>(py, shell)</sup>
    - [x] --- automatically open `code` after the shell execution. open up the change log file that needed to be editied.
    - [x] --- Auto append sub change-logs to a _main_ change-log, as `Markdown/html hyperlinks`.
    (maybe override the same file each time)

    - [x] --- split change log into months, and format main change log into sub sections.


<br><br>

## Documentation Templates:
> 2022-01-11 14:39:32

Came up with some handy semi-html mardown scripts to make peach doc more readable,
Heres an example:

> key functions:
<!--///////////////////Function-Table/////////////////////-->
- <sub>`pub` `args` `return`</sub> <!--{ `TAGS` }-->
    <table>
    <tr><td> <!-- [ FUNCTIONS ] -->
    peach.pDir.<code> ls </code><sup>(path="", n=False)</sup>,<br>
    peach.pDir.<code> listdir </code></code><sup>(path="", n=False)</sup>,<br>
    peach.pDir.<code> listfiles </code></code><sup>(path="", n=False)</sup>
    </td></tr> 
    <!-- ( /END OF FUNCTIONS ) -->
    <tr><td> <!-- [ PARAMETER INPUTS ] -->
    <details> 
    <summary><i>parameters</i>: </summary>
    <!--@param-->- <code>str</code>  <b> path </b> : filepath to scan<br>
    <!--@param-->- <code>bool</code> <b> n </b> : true: return <i>names</i>; false: return <i>full path</i> 
    </detials><dv>
    </td></tr> 
    <!-- ( /END OF PARM ) -->
    <tr><td> <!-- [ RETURN VALUES ] -->
    <details> 
    <summary><i>return</i>: </summary>
    <!--@return-->- &rarr; <code>list</code> of names/paths,"<code>None</code> if directory not found.
    </detials> 
    </td></tr>
    <!-- ( /END OF RETURN ) -->
    </table>
    <!-- . . . . . . . . . . . . . . . . . . . . . . . .  -->

Code:

```html
> key functions:
<!--///////////////////Function-Table/////////////////////-->
- <sub>`pub` `args` `return`</sub> <!--{ `TAGS` }-->
    <table>
    <tr><td> <!-- [ FUNCTIONS ] -->
    peach.pDir.<code> ls </code><sup>(path="", n=False)</sup>,<br>
    peach.pDir.<code> listdir </code></code><sup>(path="", n=False)</sup>,<br>
    peach.pDir.<code> listfiles </code></code><sup>(path="", n=False)</sup>
    </td></tr> 
    <!-- ( /END OF FUNCTIONS ) -->
    <tr><td> <!-- [ PARAMETER INPUTS ] -->
    <details> 
    <summary><i>parameters</i>: </summary>
    <!--@param-->- <code>str</code>  <b> path </b> : filepath to scan<br>
    <!--@param-->- <code>bool</code> <b> n </b> : true: return <i>names</i>; false: return <i>full path</i> 
    </detials><dv>
    </td></tr> 
    <!-- ( /END OF PARM ) -->
    <tr><td> <!-- [ RETURN VALUES ] -->
    <details> 
    <summary><i>return</i>: </summary>
    <!--@return-->- &rarr; <code>list</code> of names/paths,"<code>None</code> if directory not found.
    </detials> 
    </td></tr>
    <!-- ( /END OF RETURN ) -->
    </table>
    <!-- . . . . . . . . . . . . . . . . . . . . . . . .  -->
```