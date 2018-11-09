// Hash Table with Separate chaining implementation
// Time complexity for Insertion - O(1), Deletion - O(1) and Access - O(1)
// Worst case time complexity - O(n) when all the keys are hashed to same index.

{
class HashTable {
  constructor(size=53){
    this.keyMap = new Array(size);
  }

  _hash(key) {
    let total = 0;
    let WEIRD_PRIME = 31;
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      let char = key[i];
      let value = Math.abs(char.charCodeAt(0) - 96);
      total = (total * WEIRD_PRIME + value) % this.keyMap.length;
    }
    return total;
  }

  set(key,value){
      var index = this._hash(key);
      if(!this.keyMap[index]){
          this.keyMap[index]=[];
      }
      this.keyMap[index].push([key,value]);
  }

  get(key){
      var index = this._hash(key);
      if(this.keyMap[index]){
          for(var i=0; i<this.keyMap[index].length; i++){
          if(this.keyMap[index][i][0]===key){
              return this.keyMap[index][i][1];
          }
      }
      }
      
      return undefined;
  }

  keys(){
      var keys = [];
      for(var i=0; i<this.keyMap.length; i++){
            if(this.keyMap[i]){
                for(var j=0; j<this.keyMap[i].length; j++){
                    if(!keys.includes(this.keyMap[i][j][0])){
                        keys.push(this.keyMap[i][j][0]);
                    }                  
                }
            }
      }
      return keys;
  }

  values(){
      var values = [];
      for(var i=0; i<this.keyMap.length; i++){
            if(this.keyMap[i]){
                for(var j=0; j<this.keyMap[i].length; j++){
                    if(!values.includes(this.keyMap[i][j][1])){
                        values.push(this.keyMap[i][j][1]);
                    }                  
                }
            }
      }
      return values;
  }
}

var ht = new HashTable(5)
ht.set('Walmart','Great Value');
ht.set('Amazon','Electronics');
ht.set('Best Buy','Discounts');
ht.set('Netflix','TV shows');
ht.set('Netflix','Movies');
ht.set('Amazon','Movies');
ht.set('Costco','Great Value');
}