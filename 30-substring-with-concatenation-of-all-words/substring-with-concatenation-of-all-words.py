from collections import defaultdict

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
        
        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        
        word_frequency = defaultdict(int)
        for word in words:
            word_frequency[word] += 1
        
        result = []
        
        for i in range(word_length):
            left = i
            right = i
            window_frequency = defaultdict(int)
            count = 0
            
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                
                if word in word_frequency:
                    window_frequency[word] += 1
                    if window_frequency[word] <= word_frequency[word]:
                        count += 1
                    
                    while window_frequency[word] > word_frequency[word]:
                        left_word = s[left:left + word_length]
                        window_frequency[left_word] -= 1
                        if window_frequency[left_word] < word_frequency[left_word]:
                            count -= 1
                        left += word_length
                    
                    if count == word_count:
                        result.append(left)
                else:
                    window_frequency.clear()
                    count = 0
                    left = right
        
        return result
