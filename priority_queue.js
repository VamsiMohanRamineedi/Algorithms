// Priority Queue with minBinaryHeap
// Insertion and Removal - O(log n)

{
class PriorityQueue{
    constructor(){
        this.values = [];
    }

    enqueue(value, priority){
        var newNode = new Node(value, priority);
        this.values.push(newNode);
        var value_index = this.values.length - 1;
        var parent_index = Math.floor((value_index - 1)/2);
        var temp;
        while(value_index > 0 && this.values[value_index].priority < this.values[parent_index].priority){
            temp = this.values[value_index];
            this.values[value_index] = this.values[parent_index];
            this.values[parent_index] = temp;
            value_index = parent_index;
            parent_index = Math.floor((value_index - 1)/2);
        }
        return this.values;
    }

    dequeue(){
        function swap(arr, idx1, idx2){
            var temp = arr[idx1];
            arr[idx1] = arr[idx2];
            arr[idx2] = temp;
        }
        if(this.values.length===0) return 'empty heap';
        swap(this.values, 0, this.values.length-1);
        var min = this.values.pop();

        var parent_index = 0;
        var left_index;
        var right_index;
        var smallest_child_index;
        var parent_element;
        var left_child;
        var right_child;
        var smallest_child;
        
        while(true){
            left_index = 2*parent_index + 1;
            right_index = 2*parent_index + 2;

            if(left_index > this.values.length-1) break;
            else if(right_index > this.values.length-1) smallest_child_index = left_index;
            else {
                left_child = this.values[left_index];
                right_child = this.values[right_index];
                smallest_child_index = left_child.priority < right_child.priority ? left_index : right_index;
            }
            parent_element = this.values[parent_index];            
            smallest_child = this.values[smallest_child_index];

            if(smallest_child.priority < parent_element.priority){
                swap(this.values, smallest_child_index, parent_index);
                parent_index = smallest_child_index;
            }else{
                break;
            }
        }

        return min;
    }
}

class Node{
    constructor(val, priority){
        this.val = val;
        this.priority = priority;
    }
}

var heap = new PriorityQueue();
heap.enqueue('carry laptop',5);
heap.enqueue('switch off stove',1);
heap.enqueue('do assignments',4);
heap.enqueue('go to class',3);
heap.enqueue('carry food',2);
}