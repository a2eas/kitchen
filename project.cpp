#include <iostream>
using namespace std;
struct uni{
string name;
int income;
int num_staff;
int num_student;

};
class personnel{
    private:
string name;
int age;
string id;
string address;
    public:
personnel(string n, int a,string ad){
    name = n;
    age = a;
    address = ad;
}   
};
class student: public personnel {
    private:
    int year;
    double grade;
    public:
    student(string n, int a,string ad, int y,double g):personnel(n,a,ad){
        year = y;
        grade = g;
    }
    
};
class staff: public personnel{
private:
int hours;
int Salary;
double gross_pay;
string status; //full time or part time
string job_title;
public:
staff (string n, int a,string ad,int h, int s, double gr,string st,string j):personnel(n,a,ad){
    hours = h;
    Salary = s;
    gross_pay = gr;
    status = st;
    job_title = j;
}
};


int main() {

cout<<"test";
    return 0;
}