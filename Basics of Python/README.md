**Following are some of the important features of Python**:

1. **Python is open source**: The Python implementation is under an open source license that makes it freely usable and distributable, even for commercial use.

2. **Python is interpreted**: Python is a high level language which is interpreted by a Python interpreter.

3. **Python is cross platform compatible**: Python can be executed on all major platforms like Windows, Linux/Unix, OS/2, Mac and others.

4. **Python is Object-Oriented**: In Python, we encapsulate data within the objects as it supports the object-oriented style of programming.

5. **Python is a great choice for new learners**: Python is easy to learn and follows a simple syntax, so it is a good choice for beginner programmers. Python also supports wide range of application development.

6. **Python is extensible**: Python has a wide range of libraries and built-in functions which helps in easy and rapid development of applications.

7. **Python is interactive**: Python users are provided a command prompt where they can interact directly with the interpreter to write programs.

8. **Database connectivity**: Python provides interfaces required to connect to all major databases like Oracle, MySQL, PostgreSQL and others.

**Identifiers**:

In Python, variables, functions, classes, modules and objects are identified using a name known as an identifier. An identifier can start with an uppercase or lowercase character or an underscore (_) followed by any number of underscores, letters and digits. All identifiers in Python are case sensitive.

Example: weight=10

In the above example, weight is an identifier.

**Keywords**:

Keywords are the **reserved words** in Python. So, keywords cannot be used as identifiers or to name variables and functions. Few of the keywords are listed below.

Example: if, else, elif, for, where, break, continue

**Variables** are like containers for data (i.e. they hold the data) and the value of the variable can vary throughout the program.

**Declaring a variable**:

Syntax: var_name = literal_value

where var_name is the name given to the container holding the value specified as literal_value in the syntax above.

Example: weight=10

In the above example, weight is the container holding the value 10  which can change during the execution of the program.

**Data Type in Python**:
1. **Numeric**:
    1. **int**: 123
    2. **long**: 12345678912345678

2. **Numeric with decimal point**:
    1. **float**: 123.45
    2. **double**: 123123.32345324

3. **Alphanumeric**:
    1. **char**: 'A'
    2. **string**: "Hello World"

4. **Boolean**:True, False

**Python is a dynamically typed language**!

In the above example(weight=10), no datatype was mentioned at the time of declaring variable. In Python, the datatype of a variable is decided automatically at the time of execution based on the value assigned to it. This is called as **dynamic typing**.

**The input() function**:
Python provides the **input()** built-in function to read an input from the user using the standard input device (i.e. keyboard). The input() function always returns string data irrespective of the type of data entered through the keyboard.

**Syntax**: var_name = input([“interactive statement”])

where,

**var_name** is the variable assigned with the string value which is read using input method.

**Interactive statement** is the statement displayed to the user expecting the response from them

**The print() function**:
Python provides the **print()** built-in function to display the output onto the standard output device (i.e. Monitor)

**Syntax**: print(“var_name1, var_name2, …”, [end=”value1”, sep=”value2”])

where,

**var_name1**, **var_name2** are the variable names or the literals you want to print or output

**end** is used to specify the separator between two print statements which is ‘\n’ by default

**sep** is used to specify the separator between multiple variables displayed using a single print statement

**Type Conversion in Python**
When we perform any operation on variables of different datatypes, the data of one variable will be converted to a higher datatype among the two variables and the operation is completed. This conversion is done by interpreter automatically and it is known as implicit type conversion. But Python does not support implicit type conversion and it will throw an error.

**Example**:
num1=10
num2="20"
result=num1+num2
print(result)

**Output**:
Traceback (most recent call last):
  File "D:\Neon\Deepu\src\test.py", line 3, in <module>
    result=num1+num2
TypeError: unsupported operand type(s) for +: 'int' and 'str'

If we have to avoid this, then we have to explicitly convert the datatype of one variable into the required datatype to complete the operation. This is known as **explicit type conversion**.

**Example**:
num1=10
num2="20"
result=num1+int(num2)
print(result)

**Output**:
30

**Note**:
Programming languages define their own rules for implicit and explicit conversions. These rules do change from language to language.

Similarly, one has to be careful in explicit conversions as well. For example,

1. Converting a floating point value to integer would result in loss of decimal point values

2. A larger data type if converted to smaller data type will result in loss of data as the number will be truncated


