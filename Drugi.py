
# Python program to demonstrate
# command line arguments
print("Hello Jasio")

import sys
import requests


 
# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)
 
# Arguments passed
# print("\nName of Python script:", sys.argv[0])
 
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")
print("\n")   
response = requests.get(sys.argv[i])
print(response)