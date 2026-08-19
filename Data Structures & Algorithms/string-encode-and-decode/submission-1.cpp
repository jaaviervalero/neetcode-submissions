class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string = "";
        for (string str : strs){
            encoded_string.append(str + "-");
        }
        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> strs;
        string buffer;
        stringstream fd(s);
        
        while (getline(fd, buffer, '-')){
            strs.push_back(buffer);
        }

        return strs;

    }
};
