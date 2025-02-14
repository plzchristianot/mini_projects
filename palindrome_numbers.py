#Check if the integer given is palindrome or not and return True or False
def isPalindrome(self, x: int) -> bool:
    if str(x) == str(x)[::-1] :
        return True
    return False