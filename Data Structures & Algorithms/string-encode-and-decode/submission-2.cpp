class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string = "";
        for (string str : strs){
            encoded_string.append(to_string(str.length()) +"#" + str);
        }
        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> strs;
        string buffer;
        
        int i = 0;

        while (i < s.length()){
            int j = i;

            while (s[j] != '#'){
                j++;
            }
            int length = stoi(s.substr(i, j -i));

            buffer = s.substr(j+1, length);

            strs.push_back(buffer);

            i = j + length + 1;

        }

        return strs;

    }
};
