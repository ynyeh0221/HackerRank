    int a_num=0;
    cin>>a_num;
    int q_num=0;
    cin>>q_num;
    int **A=(int **)malloc(a_num * sizeof(int *));
    for(int i=0;i<a_num;i++)
    {
        int n=0;
        cin>>n;
        A[i]=(int *)malloc(n * sizeof(int));
        for(int j=0;j<n;j++)
        {
            int temp=0;
            cin>>temp;
            A[i][j]=temp;
        }
    }
    for(int i=0;i<q_num;i++)
    {
        int aind=0;
        cin>>aind;
        int ind=0;
        cin>>ind;
        printf("%d\n",A[aind][ind]);
    }
	return 0;
}
