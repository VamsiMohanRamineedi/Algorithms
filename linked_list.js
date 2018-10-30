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

    shift(){
        if(!this.head) return undefined;
        var currentHead = this.head;
        this.head = currentHead.next;
        this.length--;
        if(this.length === 0){
            this.tail = null;
        }
        return currentHead;
    }

    unshift(val){
        var newNode = new Node(val);
        if(!this.head) {
            this.head = newNode;
            this.tail = this.head;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
        return this;
    }

    get(idx){
        if(idx<0 || idx>=this.length) return null;
        var current = this.head;
        var count = 0;
        while(count<idx){
            current = current.next;
            count++;
        }
        return current;
    }

    set(idx, val){
        var current_node = this.get(idx)
        if(current_node===null) return false;
        current_node.val = val;
        return true;
    }

    insert(idx, val){
        if(idx < 0 || idx > this.length) return false;
        if(idx===this.length){
            this.push(val);
        }
        else if(idx===0){
            this.unshift(val);
        }
        else{
        var previous_node = this.get(idx-1);
        var moved_node = previous_node.next;
        var new_node = new Node(val);
        previous_node.next = new_node;
        new_node.next = moved_node;
        this.length++;
        }
        return true;
    }

    remove(idx){
        if(idx<0 || idx>=this.length) return undefined;
        if(idx===0) return this.shift(idx);
        else if(idx===this.length-1) return this.pop();
        else{
            var previous_node = this.get(idx-1);
            var removed_node = previous_node.next;
            previous_node.next = removed_node.next;
            this.length--;
            return removed_node;
        }

    }
}

var list = new SinglyLinkedList();
list.push(4)
list.push(5)
list.push(6)
list.push(9)
list.push(16)

}
