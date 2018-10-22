function validAnagram(str1, str2){
    if (str1.length !== str2.length){
        return false;
    }

    let str1_charCount = {}
    let str2_charCount = {}
    
    for (let char of str1){
        str1_charCount[char] = (str1_charCount[char] || 0)+1
    }
    for (let char of str2){
        str2_charCount[char] = (str2_charCount[char] || 0)+1
    }

    for (let key in str1_charCount){
        if (str1_charCount[key]!==str2_charCount[key]){
            return false;
        }
    }

    return true;
}

validAnagram('iceman','cinema')