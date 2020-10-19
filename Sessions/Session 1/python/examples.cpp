#include<iostream>
using namespace std;

void say_my_name(string name, int n)
{
    //no docstring :(
    while (n > 0)
    {
        cout<<name<<endl;
        n--;
    }
}

int main()
{
    say_my_name("kvector", 3);
    return 0;
}