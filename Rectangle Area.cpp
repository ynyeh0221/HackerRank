class Rectangle
{
    protected:
        int height;
        int width;
    public:
        void Display()
        {
            cout<<width<<" "<<height<<endl;
        }
};

class RectangleArea: public Rectangle
{
    public:
        void Input()
        {
            int w;
            int h;
            cin>>w;
            cin>>h;
            width=w;
            height=h;
        }
        void Display()
        {
            cout<<width*height<<endl;
        }
};
