
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box
class Box
{
  private:
    int l=0;
    int b=0;
    int h=0;
  public:
    int getLength() const
    {
        return l;
    }
    int getBreadth() const
    {
        return b;
    }
    int getHeight() const
    {
        return h;
    }
    long long CalculateVolume ()
    {
        return (long long)l*b*h;
    }
    Box()
    {
        BoxesCreated++;
    }
    Box(int length, int breadth, int height)
    {
        l=length;
        b=breadth;
        h=height;
        BoxesCreated++;
    }
    Box(const Box& B)
    {
        l=B.l;
        b=B.b;
        h=B.h;
        BoxesCreated++;
    }
    ~Box()
    {
        BoxesDestroyed++;
    }
    bool operator<(const Box &B)
    {
        int ll=B.getLength();
        int bb=B.getBreadth();
        int hh=B.getHeight();
        if(l < ll || (b < bb && l==ll) || (h < hh && b==bb && l==ll))
            return true;
        else
            return false;
    }

};
    ostream& operator<<(ostream& out, Box B)
    {
        int l=B.getLength();
        int b=B.getBreadth();
        int h=B.getHeight();
        return out<<l<<' '<<b<<' '<<h;
    }
// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);

// Destructor
// ~Box()
// {

// }

// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box &b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box B)



