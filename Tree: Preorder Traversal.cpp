/* you only have to complete the function given below.  
Node is defined as  

struct node
{
    int data;
    node* left;
    node* right;
};

*/

void Preorder(node *root) {
    
    if(root==NULL) return;
    printf("%d ", root->data);
    Preorder(root->left);
    Preorder(root->right);
}
