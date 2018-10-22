// Count unique values in an array

// Runtime = O(n)

function countUniqueValues(arr){
	//edge cases
	if(arr.length===0 || arr.length===1){
		return arr.length
	}

	//take two pointers and a counter
	let i = 0
	let j = i+1
	let count = 1
	while(j<=(arr.length-1)){
	    //increment counter if not equal, and move pointers to right
	    if (arr[i]!==arr[j]){
		  count ++
	    }
	    i++
	    j++
	}

	return count
}
	
//countUniqueValues([1,2,3,4,4,4,7,7,12,12,13])
//countUniqueValues([1,1,1,1,1,2])
//countUniqueValues([])
//countUniqueValues([-2,-1,-1,0,1])