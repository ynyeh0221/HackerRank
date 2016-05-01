// Write your Student class here

class Student
{
    private:
        int grade [5];
    public:
        void input()
        {
            for(int i=0;i<5;i++)
            {
                int g=0;
                cin>>g;
                grade[i]=g;
            }
        }
        int calculateTotalScore()
        {
            int sum=0;
            for(int i=0;i<5;i++)
                sum+=grade[i];
            return sum;
        }
};
