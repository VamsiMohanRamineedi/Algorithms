{

class Node{
    constructor(value){
        this.value = value;
        this.right = null;
        this.left = null;
    }
}

class BST{
    constructor(){
        this.root = null;
    }

    insert(value){
        var newNode = new Node(value);
        if(!this.root){
            this.root = newNode;
            return this.root
        }
        var currentNode = this.root;
        while(true){
            if(newNode.value === currentNode.value) return undefined;
            if(newNode.value > currentNode.value){
                if(!currentNode.right){
                    currentNode.right = newNode;
                    return this;
                }
                currentNode = currentNode.right;
            }
            else{
                if(!currentNode.left){
                    currentNode.left = newNode;
                    return this;
                }
                currentNode = currentNode.left;
            }
        }                        
    }

    contains(value){
        if(this.root === null) return false;
        var currentNode = this.root;
        while(true){
            if(value === currentNode.value) return true
            else if(value > currentNode.value){
                if(!currentNode.right) return false;
                currentNode = currentNode.right;
            }
            else{
                if(!currentNode.left) return false;
                currentNode = currentNode.left;
            }         
        }
    }
}

var bst = new BST();
bst.insert(7);
bst.insert(-1);
bst.insert(19);
bst.insert(3);
bst.insert(71);
bst.insert(40);
bst.insert(21);
}