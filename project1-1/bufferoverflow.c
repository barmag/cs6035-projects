#include<stdio.h>
#include<string.h>
// #include "passwords.h"

int main(int argc, char* argv[])
{
    // char adminpass[8] = "adminpa";
    char two[8] = "two";
    char one[5] = "one";
    int access = 0;
    char password[8];

    printf("please enter a password: ");
    scanf("%s", password);

    if(strncmp(password, "adminp", 8) == 0)
        access = 1;

    if (access > 0)
        printf("Access Granted\n");
    else
        printf("Access Denied: %d\n", access);
    return 0;
}