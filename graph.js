{
class Graph{
    constructor(){
        this.adjacencyList = {};
    }

    addVertex(vertex){
        if(!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
    }

    addEdge(v1, v2){
        this.adjacencyList[v1].push(v2);
        this.adjacencyList[v2].push(v1);
    }

    removeEdge(v1,v2){
        let index_in_v1 = this.adjacencyList[v1].indexOf(v2);
        let index_in_v2 = this.adjacencyList[v2].indexOf(v1);
        this.adjacencyList[v1].splice(index_in_v1, 1);
        this.adjacencyList[v2].splice(index_in_v2, 1); 
    }

    removeVertex(vertex){
        for(let v2 of this.adjacencyList[vertex]){
            this.removeEdge(vertex,v2);
        }
        delete this.adjacencyList[vertex];
        
    }
}

var g = new Graph();
g.addVertex('Hyd');
g.addVertex('Kolkata');
g.addVertex('Pune');
g.addEdge('Hyd','Pune');
g.addEdge('Pune','Kolkata');
}

