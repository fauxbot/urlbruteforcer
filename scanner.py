# Python 3 program to print all
# possible strings of length k
     
# The method that prints all
# possible strings of length k.
# It is mainly a wrapper over
# recursive function printAllKLengthRec()

import requests

def printAllKLength(set, k):
 
    n = len(set)
    printAllKLengthRec(set, "", n, k)
 
# The main recursive method
# to print all possible
# strings of length k
def printAllKLengthRec(set, prefix, n, k):
     
    # Base case: k is 0,
    # print prefix
    modstring = prefix[:2] + "-" + prefix[2:]
    if (k == 0) :
        url = ('http://test.com/' + modstring + '/restofurl')
        r = requests.get(url)
        size = len(r.content)
        if (size != 2804) :
            print(url)
        return
 
    # One by one add all characters
    # from set and recursively
    # call for k equals to k-1
    for i in range(n):
 
        # Next character of input added
        newPrefix = prefix + set[i]
         
        # k is decreased, because
        # we have added a new character
        printAllKLengthRec(set, newPrefix, n, k - 1)
 
# Driver Code
if __name__ == "__main__":
     
    set1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    k = 9
    printAllKLength(set1, k)
     
 
# This code is contributed
# by ChitraNayal

