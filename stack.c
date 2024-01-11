#include<stdio.h>
#define n 5
int top = -1;
int stack[n];
void push(int val){
    if(top == n - 1){
        printf("Stack overflow");
    }
    else{
        top++;
        stack[top] = val;
    }
}

void pop(){
    if(top == -1){
        printf("Stack Underflow");
    }
    else{
        printf("%d", stack[top]);
        top--;
    }
}

void peek(){
    if(top == -1){
        printf("Stack Underflow");
    }
    else{
        printf("%d", stack[top]);
    }
}
int main() {
    push(5);
    push(4);
    push(3);
    push(2);
    push(1);
    int i = 0;
    for(i = 0; i < n; i++){
        printf("%d", stack[i]);
    }

    pop();

    peek();

}