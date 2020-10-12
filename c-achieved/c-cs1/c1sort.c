#include <stdio.h>
 
// c sorting algorithm for float numbers // least to largest.

int main()
{
    printf("Please input data, use space for next:\n");
    
    int i;
    int j;
    int size = 4; // the total number of data inputed/
    float temp,array[size]; 
    // the type of the temp vairable and array should be float
   
   
    for(i = 0; i < size; i++)
    scanf("%f",&array[i]);
  
    for(i = 0; i < size; i++)
    {
        for(j = i + 1; j < size; j++)            
        {
            if(array[i]>array[j])
            {
                temp=array[i];
                array[i]=array[j];
                array[j]=temp;
            }
        }
    }
    printf("Result from smallest to largest is:\n");
    for(i = 0; i < size; i++)
    printf("%g\n",array[i]);
    return 0;
}
