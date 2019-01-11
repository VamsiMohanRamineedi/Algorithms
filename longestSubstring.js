// Time complexity - O(n)
// Space complexity - O(n)

function findLongestSubstring(str) {
    let start = 0
    let end = 0
    let max_length = 0
    let distinct_chars = {}
    let char

    while(end < str.length) {
        char = str[end]
        if(!distinct_chars[char]) {
            distinct_chars[char] = 1
            max_length = Math.max(max_length, end - start + 1)
        } else {
                // move 'start' to the position pointing to the char next to the old position of the char at 'end'
                // for ex: 'longestsubstring' - if end=7 (i.e) char='s', make start=6
                while(str[start] !== str[end]) {
                    delete distinct_chars[str[start]]
                    start++
                }
                start++
        }
        end++
    }
    return max_length
}

//findLongestSubstring('rithmschool')
//findLongestSubstring('thisisawesome')
//findLongestSubstring('thisishowwedoit')
//findLongestSubstring('longestsubstring')



