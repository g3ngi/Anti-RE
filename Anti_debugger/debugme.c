#include <stdio.h>
#include <stdlib.h>
#include <sys/ptrace.h>

void prize(){
    if(ptrace(PTRACE_TRACEME, 0, 1, 0)){
        puts("Woops, no debugger allowed!");
    }

    char prize[50];
    strcpy(prize, "testing");


}

int main(){
    
    return 0;
}