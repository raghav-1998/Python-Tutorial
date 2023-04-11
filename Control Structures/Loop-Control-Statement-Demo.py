for passenger in "A","A", "FC", "C", "FA", "SP", "A", "A":
    if(passenger=="FC" or passenger=="FA"):
        print("No check required")
        continue
    if(passenger=="SP"):
        print("Declare emergency in the airport")
        break
    if(passenger=="A" or passenger=="C"):
        print("Proceed with normal security check")
    print("Check the person")
    print("Check for cabin baggage")

"""
Output:

Proceed with normal security check
Check the person
Check for cabin baggage
Proceed with normal security check
Check the person
Check for cabin baggage
No check required
Proceed with normal security check
Check the person
Check for cabin baggage
No check required
Declare emergency in the airport

"""


num=10
count=0
while(count <= num):
    if(count%2 == 0):
        pass
    else:
        print(count)
    count+=1


"""
Output:

1
3
5
7
9
"""