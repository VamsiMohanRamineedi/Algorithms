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

    dfs_recursive(starting_vertex){
        let results = [];
        let visited = {};
        const adjacencyList = this.adjacencyList;

        function dfs(starting_vertex){
            if (!starting_vertex) return null;
            visited[starting_vertex] = true;
            results.push(starting_vertex);
            for(let adj_vertex of adjacencyList[starting_vertex]){
                if(!visited[adj_vertex]) dfs(adj_vertex);
            }           
        }

        dfs(starting_vertex);
        return results;
    }
}

var g = new Graph();
g.addVertex('A');
g.addVertex('B');
g.addVertex('C');
g.addVertex('D');
g.addVertex('E');
g.addVertex('F');
g.addEdge('A','B');
g.addEdge('A','C');
g.addEdge('B','D');
g.addEdge('C','E');
g.addEdge('D','E');
g.addEdge('D','F');
g.addEdge('E','F');
//g.dfs_recursive('A');

}

