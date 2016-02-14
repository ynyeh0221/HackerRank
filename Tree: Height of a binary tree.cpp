#include <queue>
/*The tree node has data, left child and right child 
struct node
{
    int data;
    node* left;
    node* right;
};

*/
int height(node * root)
{
    if (root == NULL)
        return 0;
    queue<node *> q;
    q.push(root);
    int h=0;
    while (1)
    {
        int nodeCount=q.size();
        if (nodeCount==0)
            return h;
        h++;
        while(nodeCount>0)
        {
            node *node=q.front();
            q.pop();
            if (node->left!=NULL)
                q.push(node->left);
            if (node->right!=NULL)
                q.push(node->right);
            nodeCount--;
        }
    }
}
  
