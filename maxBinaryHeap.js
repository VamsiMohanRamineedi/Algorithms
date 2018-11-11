{
class MaxBinaryHeap{
    constructor(){
        this.values = [];
    }

    insert(value){
        this.values.push(value);
        var value_index = this.values.length - 1;
        var parent_index = Math.floor((value_index - 1)/2);
        var temp;
        while(value_index > 0 && this.values[value_index] > this.values[parent_index]){
            temp = this.values[value_index];
            this.values[value_index] = this.values[parent_index];
            this.values[parent_index] = temp;
            value_index = parent_index;
            parent_index = Math.floor((value_index - 1)/2);
        }
        return this.values;
    }

    extractMax(){
        function swap(arr, idx1, idx2){
            var temp = arr[idx1];
            arr[idx1] = arr[idx2];
            arr[idx2] = temp;
        }
        if(this.values.length===0) return 'empty heap';
        swap(this.values, 0, this.values.length-1);
        var max = this.values.pop();

        var parent_index = 0;
        var left_index;
        var right_index;
        var largest_child_index;
        var parent_element;
        var left_child;
        var right_child;
        var largest_child;
        
        while(true){
            left_index = 2*parent_index + 1;
            right_index = 2*parent_index + 2;

            if(left_index > this.values.length-1) break;
            else if(right_index > this.values.length-1) largest_child_index = left_index;
            else {
                left_child = this.values[left_index];
                right_child = this.values[right_index];
                largest_child_index = left_child > right_child ? left_index : right_index;
            }
            parent_element = this.values[parent_index];            
            largest_child = this.values[largest_child_index];

            if(largest_child > parent_element){
                swap(this.values, largest_child_index, parent_index);
                parent_index = largest_child_index;
            }else{
                break;
            }
        }

        return max;
    }
}

var heap = new MaxBinaryHeap();
heap.insert(5);
heap.insert(9);
heap.insert(11);
heap.insert(0);
heap.insert(7);
heap.insert(15);
heap.insert(3);
}