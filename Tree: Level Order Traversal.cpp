#include <queue>
/*
struct node
{
    int data;
    node* left;
    node* right;
}*/

void LevelOrder(node * root)
{
    queue<node*> q;
    q.push(root);
    while (!q.empty())
    {
        node* p = q.front(); q.pop();
        cout << p->data <<" ";
        if (p->left)  q.push(p->left);
        if (p->right) q.push(p->right);
    }  
}
