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
            if(newNode.value < currentNode.value){
                if(!currentNode.left){
                    currentNode.left = newNode;
                    return this;
                }
                currentNode = currentNode.left;
            }
        }                        
    }
}

var bst = new BST();

}