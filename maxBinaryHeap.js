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
}

var heap = new MaxBinaryHeap();
heap.insert(5);
heap.insert(9);
heap.insert(11);
heap.insert(0);
heap.insert(7);
heap.insert(15);
}