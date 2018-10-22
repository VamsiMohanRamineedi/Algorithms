function countUniqueValues(arr){
	//edge cases
	if(arr.length===0 || arr.length===1){
		return arr.length
	}

	//take two pointers and a counter
	let i = 0
	let j = i+1
	let count = 1
	//check if adjacent values are equal
	while(arr[i]!==arr[j] && j<=(arr.length-1)){
	//increment counter if not equal, and move pointers to right
		count ++;
		i++;
		j++;
	}

	return count
}

countUniqueValues([1,2,3,4,4,4,7,7,12,12,13])