**List**:

 List can be used to store a group of elements together in a sequence.

 List of letters:

 ![image](https://programmathically.com/wp-content/uploads/2021/05/list.png)

 
 **Storage of element**:

 In case of having different variables for each ticket number, variables will be stored in separate memory locations. Whereas in case of list, the elements will be stored in contiguous memory locations.

![image](https://www.bookofnetwork.com/images/python-images/list1.png)


**List Index**:

Each element in the list has a position in the list known as an index.
The list index starts from zero. 

![image](https://prepbytes-misc-images.s3.ap-south-1.amazonaws.com/assets/1671778764801-list%20program%20in%20python2.png)

1. Suppose, instructor 2nd taught C++,student can directly go to instructor 2nd without having to go to other instructor. Similarly, index positions actually help us to **directly access** a value from the list. 

**list_name[index]** can be used to directly access the list element at the mentioned index position.

2. Suppose we have to allocate different course to instructor 1st, we can do it using **course_list[1]="Ruby"**. Thus, in addition to using the index to access an element directly, we can also use it to **directly modify** an element in the list.

3. Just like how we cannot allocate 4th course to student in an institute of 3 course, we cannot access values beyond the total number of elements in the list.

For example: print(course_list[3]) will result in **index out of bound error**. 