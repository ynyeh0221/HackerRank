#include <iostream> 
using namespace std; 
/*
struct node
{
    int data;
    node* left;
    node* right;
};

*/

static void t1(node* root)
{
    if (!root)
        return;
    t1(root->left);
    cout << root->data << " ";
}

static void t2(node* root)
{
    if (!root)
        return;
    cout << root->data << " ";
    t2(root->right);
}

void top_view(node * root)
{
    t1(root);
    t2(root->right);
}
