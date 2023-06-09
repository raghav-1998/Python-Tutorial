**Control Structures**:

Control Structures are used to control the flow of execution in a Python program. Sometimes, it is required to skip execution of few statements based on the logic and in some cases, a set of statements may be needed to get executed repeatedly for a finite number of times or based on the value of the variable.

![image](https://docs.oracle.com/cd/A57673_01/DOC/server/doc/PLS23/image009.gif)

**Selection Statements**:

During the execution of the program, we may not wish to execute all set of statements sequentially. Sometimes, we may wish to select between various set of statements based on some conditions. Depending on the test condition evaluation, the flow is determined within the program. Let’s have look at few of them.

1. **if (simple if)**:

It is a conditional statement used for decision making in Python. In if statement, the test condition is evaluated and the statements inside the if block are executed only if the evaluated condition is True. In the below if statement, we have only one set of statements to select based on the test condition. So, it is also called as one-way selection statement.

Below is the syntax of the simple if statement:

![image](https://files.realpython.com/media/t.78f3bacaa261.png)

2. **if-else**:
It is a conditional statement used for selection between two set of statements based on the evaluation of test condition. The statements inside the if block are executed only if the evaluated condition is True. Otherwise statements inside the else block are executed. As we have two set of statements to select based on the test condition, it is also called as two-way selection statement.

Below is the syntax of if-else statement:

![image](https://facingissuesonitcom.files.wordpress.com/2021/03/if-else-statement.jpg)

3. **else-if ladder**:
It is a conditional statement used for selection between multiple set of statements based on multiple test conditions. The various test conditions are provided inside each **if-elif** statement. Whenever the test condition is evaluated as True, the statements inside the corresponding block are executed and the control comes out of the else-if ladder. If none of the test conditions are evaluated as True, the statements inside the **else** block are executed. As we have multiple set of statements to select based on the test conditions, it is also called as **multi-way selection** statement.

In else-if ladder, the conditions are evaluated from the top of the ladder downwards. As soon as a True condition is found, the set of statements associated with it get executed skipping the rest of the ladder.

Below is the syntax of else-if ladder statement:

![image](https://facingissuesonitcom.files.wordpress.com/2021/03/python-else-if-statement.jpg?w=624)

4. **Nested If**:

An **if** statement within another **if** statement is known as **nested if statement**. Similarly, any decision logic can be written within an else statement too.

![image](https://dotnettutorials.net/wp-content/uploads/2021/07/word-image-192.png)



**Looping Statements**:
Looping statements are used to execute the same block of code multiple times in Python based on the test condition


1. **while loop**:

The **while loop** is used to execute a piece of code as long as the test condition is **True**. The while loop is preferred whenever the **number of iterations is not known**.

Syntax:

![image](https://pynative.com/wp-content/uploads/2021/06/while-loop-in-python.png)

2. **for loop**:

In Python, the **for** loop allows the loop to run over a **specific sequence of values**. In other words, for every value in the sequence, the loop runs once. Thus, we can avoid **infinite loops** by using a for loop.

Syntax:

![image](https://pynative.com/wp-content/uploads/2021/06/for-loop-in-python.png)

3. **Nested Loop**:

A loop within a loop is known as a nested loop.

![image](https://pynative.com/wp-content/uploads/2021/06/python-nested-loop.png)


**Loop Control Statements**:

The flow inside looping statements are controlled using the looping control statements like **pass**, **break** and **continue**.

1. When we want to stop a loop or break out of it, we can use the **break** statement.

2. When we want to skip the remaining statements in the current loop and continue with the next iteration, we can use **continue** statement.

3. In Python, **pass** is a null statement which is used to do create empty blocks. When **pass** is executed, it results in no-operation and the control will move to the next statement applicable. 