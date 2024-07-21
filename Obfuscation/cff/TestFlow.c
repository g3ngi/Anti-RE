#include <stdio.h>
#include <stdlib.h>

void func_0() { puts("Block A"); }
void func_1() { puts("Block B"); }
void func_2() { puts("Block C"); }

void call_dispatch_flatten() {
    void (*dispatch_table[])() = {
    func_0,
    func_1,
    func_2,
    };

    int next = 0;
    while (next >= 0) {
        if (next < sizeof(dispatch_table) / sizeof(dispatch_table[0])) {
            dispatch_table[next]();
        }
        next++;
    }
}


void before(){
    puts("Process A");
    puts("Process B");
    puts("Process C");
}


void after(){
    call_dispatch_flatten();
}

int main(){
    puts("Before CFF");
    before();
    puts("After CFF");
    after();
}