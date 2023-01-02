def palindrome(i,string):
    mid = len(string)/2
    stringlen = len(string)
    
    if (i >= mid):
        return True
    if string[i] != string[stringlen-i-1]:
        return False
    return palindrome(i+1,string)
    
if __name__=="__main__":
    string = "MADIJ"
    print(palindrome(0,string))