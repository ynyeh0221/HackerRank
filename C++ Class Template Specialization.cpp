// Define specializations for the Traits class template here.
char s []="unknown";
char f0 []="apple";
char f1 []="orange";
char f2 []="pear";
char c0 []="red";
char c1 []="green";
char c2 []="orange";
template <>
struct Traits<Fruit>
{
    public:
    static char* name(int a)
    {
        if(a>=3 || a<0)
            return s;
        else if (a==0)
            return f0;
        else if (a==1)
            return f1;
        else
            return f2;            
    }
};

template <>
struct Traits<Color>
{
    public:
    static char* name(int a)
    {
        if(a>=3 || a<0)
            return s;
        else if (a==0)
            return c0;
        else if (a==1)
            return c1;
        else
            return c2;  
    }
};
