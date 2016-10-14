#include <iostream>
#include <queue>
using namespace std; 
/*
struct node
{
    int data;
    node* left;
    node* right;
};

*/

// level-order

void top_view(node * root)
{
    queue <node*> nodes;
    nodes.push(root);
    queue <int> levels;
    levels.push(1);
    vector <int> res;
    res.push_back(root->data);
    int curind = 0;
    while (!nodes.empty())
    {
        node * n = nodes.front();
        nodes.pop();
        int l = levels.front();
        levels.pop();
        if (n->left)
        {
            if (curind == 0)
                res.insert(res.begin(), n->left->data);
            nodes.push(n->left);
            levels.push(l+1);
        }
        curind ++;    
        if (n->right)
        {
            nodes.push(n->right);
            levels.push(l+1);
            if (curind == pow(2, l)-1)
            {
                res.push_back(n->right->data);
                curind = 0;
                continue;
            }
        }
        curind ++;
    }
    for (int i = 0; i < res.size(); i++)
        cout<<res[i]<<' ';
    return;
}
