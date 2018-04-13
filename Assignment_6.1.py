
import numpy as np
import math 

print("Enter your vector")
s = input()
#converting all string element to integers
input_vector=list(map(int,s.split(",")))

print("Enter number of Columns in a matrix")
n=int(input())
print("-----------------------------------------")

output_matrix =np.matrix(input_vector)
#numpy transpose used for reversing col*row
output_matrix=np.transpose(output_matrix)
Boolean_value = True
for i in range(2,n+1):
    
    temp=[]
    if Boolean_value==True:
        Boolean_value=False
    else:
        Boolean_value=True
         
    for j in range(len(input_vector)):
        if Boolean_value==False:
                    #As boolean value if false putting power as N-I-1
            temp.append(math.pow(input_vector[j],(n-i-1)))
        else:
            temp.append(math.pow(input_vector[j],i))
        
    temp =np.matrix(temp) 
    temp =np.transpose(temp)
       #numpy hstack used for adding columns in a matrix
    output_matrix= np.hstack((output_matrix,temp))

print("Output matrix with columns as power of vector::")
print(output_matrix)      
print("NOTE:boolean value for EVEN column is FALSE and for ODD is TRUE")
print("------------------------------------------------")
#def Power_matrix(input_vector):
def power_matrix(vector_in,Boolean_in,n):
    matrix_out = np.matrix(vector_in)
    matrix_out = np.transpose(matrix_out)
    for i in range(2,n+1):
        temp=[]
        for j in range(len(vector_in)):
            if Boolean_in ==False:
                temp.append(math.pow(vector_in[j],(n-i-1)))
            else:
                temp.append(math.pow(vector_in[j],i))
                
        temp=np.matrix(temp)
        temp=np.transpose(temp)
        matrix_out=np.hstack((matrix_out,temp))
    return matrix_out
   
print("Increasing Boolean is False::")
print(power_matrix(input_vector,False,n))

print("Increasing Boolean is True::")
print(power_matrix(input_vector,True,n))