#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

__attribute__((always_inline)) inline void flag() {
    printf("hello where's the flag?\n");
}

__attribute__((always_inline)) inline void opaque_predicate() {
    int x = rand() % 100;
    int y = x + 1;
    if ((x - y) != -1) {
        flag();
    }
}

__attribute__((always_inline)) inline void inline_assembly() {
    int a = 5, b = 10, c;
    __asm__ __volatile__ (
        "add %1, %2\n\t"
        "mov %0, %2\n\t"
        : "=r" (c)
        : "r" (a), "r" (b)
    );
    if (c == 15) {
        opaque_predicate();
    }
}

int main() {
    srand(time(0));  
    inline_assembly();
    return 0;
}

