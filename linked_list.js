{
class Node{
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class SinglyLinkedList{
    constructor(){
        this.head=null;
        this.tail=null;
        this.length=0;
    }

    push(val){
        var new_node = new Node(val);
        if(this.head===null){
            this.head = new_node;
            this.tail = new_node;
        }
        else{
            this.tail.next = new_node;
            this.tail = new_node;
        }
        this.length += 1;
        return this;
    }

    pop(){
        if(this.length===0) return undefined;
        if(this.length===1){
            var head = this.head;
            this.head = null;
            this.tail = null;
            this.length--;
            return head;
        }
        var current = this.head;
        var pre = current;
        while(current.next){
            pre = current;
            current = current.next;
        }
        this.tail = pre;
        this.tail.next = null;
        this.length--;
        
        return current;
    }
}

var list = new SinglyLinkedList();
list.push(4)
list.push(5)
list.push(6)

}
