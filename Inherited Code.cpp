/* Define the exception here */
class BadLengthException : public exception {
public:
    BadLengthException(int length)
    {
        len=length;
    }

    virtual const int what()
    {
        return len;
    }
private:
    int len=0;
};
