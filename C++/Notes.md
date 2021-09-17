## BUILD

**g++** for C++ exclusively

**gcc** for C and C++

    g++ -o program program.cpp 

`g++` is the name of the compiler and
`-o` is the option needed for creating a .o file.
`program` (without .cpp suffix) is the exe file and 
`program.cpp` is your source file that you want to compile.

    gcc -o program program.cpp -l stdc++ 

Would need explicit linking with `-l stdc++` when using `gcc`;

`g++` links the standard library by default.

Use :

    gcc -o program program.cpp -l stdc++ && program.exe

for a quick run

## MAIN

The return value for `main` indicates how the program exited. Normal exit is represented by a 0 return value from `main`. Abnormal exit is signaled by a non-zero return, but there is no standard for how non-zero codes are interpreted. As noted by others, `void main()` is prohibited by the C++ standard and should not be used. The valid C++ `main` signatures are:

    int main()

and

    int main(int argc, char* argv[])

which is equivalent to

    int main(int argc, char** argv)

It is also worth noting that in C++, `int main()` can be left without a return-statement, at which point it defaults to returning 0. This is also true with a C99 program. Whether `return 0;` should be omitted or not is open to debate. The range of valid C program main signatures is much greater.  

Efficiency is not an issue with the `main` function. It can only be entered and left once (marking the program's start and termination) according to the C++ standard. For C, re-entering `main()` is allowed, but should be avoided.

## OOP

Child classes dont inherit constructors.