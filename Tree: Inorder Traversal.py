/* you only have to complete the function given below.  
Node is defined as  

struct node
{
    int data;
    node* left;
    node* right;
};

*/

void Inorder(node *root) {
    if(root==NULL) return;
    Inorder(root->left);
    printf("%d ", root->data);
    Inorder(root->right);
}
