#include<stdio.h>

void printIStars(int m)
{
  for(int n=1; n<=m;n++)
  {
    printf("*");
  }
}
void printStar_Traiangle(int size)
{
  for(int m=1; m<=size; m++)
  {
    printIStars(m);
    // print "m" number of stars
    printf("\n"); 
    //print a new line for triangle;
  }
}


int main()
{
    printStar_Traiangle(6); // call the function to print star in triangle;
    return 0;
}
