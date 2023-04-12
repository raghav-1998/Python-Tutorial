**Functions**

**Functions** are set of instructions to perform a specific task. Below is the syntax of functions in Python.

**Syntax**:

def function_name([arg1,...,argn]):

    #statements 
    [return value] 
    
variable_name = function_name([val1,...,valn])

Note: Anything enclosed in [ ] (square bracket) is optional.

**Example**:

![image](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzEmGr-AXvAs1zEKLqlAaeVrMjYoYelepF-w&usqp=CAU)

**Argument Passing in Python**:

In programming, there are two ways in which arguments can be passed to functions: 

1. pass by value 

2. pass by reference

Some languages use pass by value by default while others use pass by reference. Some languages support both and allow you to choose.

In Python, we don't have to think about pass by value and pass by reference as it does that automatically for you. To emulate this using Python, we use the concept of **mutability**. If the argument passed is **immutable** then it follows **pass by value**, else if the argument passed is **mutable** then it follows **pass by reference**.

Note: Till now we have seen int, float, string data types which are immutable. Mutable data types will be discussed later in this course.

![image](https://i0.wp.com/www.realpythonproject.com/wp-content/uploads/2021/03/pass-by-reference-vs-pass-by-value-animation.gif?fit=500%2C270&ssl=1)

