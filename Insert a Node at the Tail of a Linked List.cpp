/*
  Insert Node at the end of a linked list 
  head pointer input could be NULL as well for empty list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* Insert(Node *head,int data)
{
  // Complete this method
    Node *temp = head;
    Node *newnode = (Node *)malloc(sizeof(Node));
    newnode->data = data;
    newnode->next = NULL;
    if(temp==NULL){
        head= newnode;
        return head;
    }
    else {
        while (temp->next!= NULL)
            temp = temp->next;
        temp->next=newnode;
        return head;
    }   
}
