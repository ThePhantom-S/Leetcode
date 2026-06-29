class Solution {
public:
    int numOfStrings(vector<string>& patterns, string word) {
        int count = 0;
        for(std::string i: patterns){
            if (word.find(i) != std::string::npos){
                count++;
            }
        }
        return count;
    }
};