{

class Node{
    constructor(value){
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class DoublyLinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    push(value){
        var newNode = new Node(value)
        if (this.length===0){
            this.head = newNode;
            this.tail = this.head;
        }
        else{
            this.tail.next = newNode;
            newNode.prev = this.tail;
            this.tail = newNode;
        }
        this.length++;
        return this;
    }

    pop(){
        if (this.length===0) return undefined;
        var poppedNode = this.tail;
        if (this.length===1){
            this.head = null;
            this.tail = null;
        }
        else{
        this.tail = poppedNode.prev;
        this.tail.next = null;
        poppedNode.prev = null;
        }
        this.length--;
        return poppedNode;
    }

    shift(){
        if(this.length === 0) return undefined;
        var oldHead = this.head;
        if(this.length === 1){
            this.head = null;
            this.tail = null;
        } else{
            this.head = oldHead.next;
            this.head.prev = null;
            oldHead.next = null;
        }
        this.length--;
        return oldHead;
    }

    unshift(value){
        var newNode = new Node(value);
        if (this.length === 0){
            this.head = newNode;
            this.tail = newNode;
        } else{
            this.head.prev = newNode;
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
        return this;
    }

    get(idx){
        if(idx<0 || idx>=this.length) return null;
        var counter = 0;
        var currentNode = this.head;
        if(idx<=Math.floor(this.length/2)){
            while(counter!==idx){
                currentNode = currentNode.next;
                counter++;
            }
        } else{
            counter = this.length-1;
            currentNode = this.tail;
            while(counter!==idx){
                currentNode = currentNode.prev;
                counter--;
            }
        }
        return currentNode;
    }

    set(idx, value){
        var current_node = this.get(idx)
        if(current_node===null) return false;
        current_node.value = value;
        return true;
    }

    insert(idx, value){
        if(idx <0 || idx >this.length) return false;
        if(idx===0) return !!this.unshift(value);
        if(idx === this.length) return !!this.push(value);

        var newNode = new Node(value);
        var prev_node = this.get(idx-1);
        var next_node = prev_node.next;
        
        prev_node.next = newNode;
        newNode.prev = prev_node;
        newNode.next = next_node;
        next_node.prev = newNode;
        this.length++;
        return true;

    }
}

var list = new DoublyLinkedList();
list.push(14);
list.push(25);
list.push(61);
list.push(70);
list.push(18);
}

