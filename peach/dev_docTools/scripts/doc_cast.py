from audioop import add
import os
from re import sub
from unicodedata import name


def get_value(line=""):
    return line.split(":==:")[1]

tags = ""
parent = ""
subject = ""
is_class = 0

function_name = ""
args = ""
comment_area = ""
add_quote = False

class Parm(object):
    def __init__(self, name, type, comment):
        self.name = name
        self.type = type
        self.comment = comment
    
    def print(self):
        print("Parm Name: ", self.name)
        print("Parm Type: ", self.type)
        print("Parm comment: ", self.comment)
        
    def get_format(self):
        return "    <!--@param-->- <code>{type}</code>  <b> {name} </b> : {cmt}<br>\n".format(type=self.type,
                                                                                          name=self.name,
                                                                                          cmt=self.comment.rstrip())
        
parm_list = []
return_type = ""
return_comment = ""
class_def = False
final_str = ""


parm_template="""
    <tr><td> <!-- [ PARAMETER INPUTS ] -->
    <details> 
    <summary><i>parameters</i>: </summary>
{parms}    </detials>
    </td></tr> 
    <!-- ( /END OF PARM ) -->"""

return_template="""
    <tr><td> <!-- [ RETURN VALUES ] -->
    <details> 
    <summary><i>return</i>: </summary>
    <!--@return-->&rarr; <code>{type}</code>{comment}
    </detials> 
    </td></tr>
    <!-- ( /END OF RETURN ) -->"""

template = """
<!--///////////////////Function-Table/////////////////////-->
- <sub>{tags}</sub> <!-- `TAGS` -->
    <table>
    <tr><td> <!-- [ FUNCTIONS ] -->
    <sup>{parent}.</sup> {module}.<code> {function} </code>{ag}<br><br>
    <blockquote>
    {main_comment}
    </blockquote>
    </td></tr>
    <!-- ( /END OF FUNCTIONS ) -->{parm}{rtr}
    </table>
    <!-- . . . . . . . . . . . . . . . . . . . . . . . .  -->
"""

class_template = """
<!--///////////////////Class-Table/////////////////////-->
<sub>Inherit &rarr; `{inher}` </sub> <!-- `TAGS` -->
    <table>
    <tr><td> <!-- [ CLASS ] -->
    <big><sup>{parent}.</sup> {module}.<code> {cls} </code><sup>class</sup><br></h4>
    </td></big> 
    <!-- ( /END OF CLASS ) -->
    </table>
    <!-- . . . . . . . . . . . . . . . . . . . . . . . .  -->"""



# read file:
with open("./file_in.py", "r") as f:
    func_started=False
    comment_started = False
    function_count = 0
    for line in f:
        if not func_started and function_count:
            function_count = 0
            print("[Construct] {}".format(function_name))
            # call append final str
            if is_class:
                if "__init__" in function_name:
                    tags = "`constructor`"
                    function_name = "__init__"
                elif function_name.startswith("get"):
                    tags = "`getter`"
                elif function_name.startswith("set"):
                    tags = "`setter`"
                else:
                    tags = "`pub` `member`"
                    if return_type:
                        tags += " `return`"
            if len(parm_list):
                tags += " `args`"
            if return_type and not is_class:
                tags += " `return`"

            if not add_quote:
                comment_area = ""

            parm_str = ""
            if len(parm_list):
                for p in parm_list:
                    parm_str += p.get_format()
                parm_str = parm_template.format(parms=parm_str)

            return_str = ""
            if return_type:
                return_str=return_template.format(type=return_type, comment=return_comment.rstrip())
                
            out_str = ""
            if class_def:
                out_str = class_template.format(inher=args,
                                                parent=parent,
                                                module=subject,
                                                cls=function_name)
            else:
                if len(args):
                    args = "<sup>({})</sup>".format(args)    
                else:
                    function_name += "()"
                out_str = template.format(tags=tags,
                                        parent=parent,
                                        module=subject,
                                        function=function_name,
                                        ag=args,
                                        main_comment=comment_area,
                                        parm=parm_str,
                                        rtr=return_str)
                
            final_str += out_str + "\n"
            # reset all per object info
            function_name = ""
            args = ""
            comment_area = ""
            parm_list = []
            return_type = ""
            return_comment = ""
            class_def = False
            
        if func_started:
            while line.startswith(' '):
                line = line[1:]
            if line.startswith("\"\"\""):
                comment_started = not comment_started
                if not comment_started:
                    func_started = 0
            elif comment_started:
                
                line.rstrip()
                if line.startswith("@param"):
                    #is parameter:
                    line = line.replace("@param ", "")
                    parm, line= line.split(":")
                    while line.startswith(' '):
                        line = line[1:]
                    type, comment = (line.replace("(","")).split(")")
                    parm_list.append(Parm(parm, type, comment))
                elif line.startswith("@return:"):
                    #is return:
                    line = line.replace("@return:", "")
                    if "(" in line:
                        return_type, return_comment = (line.replace("(","")).split(")")
                    else:
                        return_type = line
                else:
                    line = line.rstrip()
                    comment_area += line

        line = line.rstrip()
        if line.startswith("#parent"):
            parent = get_value(line)
        if line.startswith("#tag"):
            tags = get_value(line)
        if line.startswith("#module_or_class"):
            subject = get_value(line)
        if line.startswith("#class"):
            is_class = int(get_value(line))
        if line.startswith("#add_quote"):
            add_quote = int(get_value(line))
        
        while line.startswith(' '):
            line = line[1:]
        if line.startswith("def"):
            func_started=True
            function_count = 1
            line = line.replace("def ", "")
            function_name, args= line.split("(")
            args = args.replace("):", "")
            
        if line.startswith("class"):
            func_started=True
            class_def = True
            function_count = 1
            line = line.replace("class ", "")
            function_name, args= line.split("(")
            args = args.replace("):", "")
            func_started=False
            function_count = 1
            is_class = 1
                
    f.close()
    
import pyperclip
pyperclip.copy(final_str)