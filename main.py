# Fizz BUzz
#Reverse string
#count vowels
#check if palindrome - racecar - racecar




class Strings:

    def main(self):
        word=self.toReverse()
        self.countVowels(word[0])




    def toReverse(self):
        palindrome= False
        answer = input('Enter a string to be reversed >')
        answer.strip()
        reversed = answer[::-1]
        if answer == reversed:
            palindrome =True

        if palindrome:
            print(answer + " reversed is " + reversed + ", it is a Palindrome")
        else:
            print(answer + " reversed is " + reversed + ", it is not a Palindrome")
        word = [answer,reversed]
        return word

    def countVowels(self, word):
        vowels =["a","o","i",'e','u']
        arrWords = [x for x in word]
        print(arrWords)
        vowelCount=0
        for i in arrWords:
            if i in ["a","o","i",'e','u']:
                vowelCount+=1

        print("The number of vowels is " + str(vowelCount))
if __name__ == "__main__":
    ma= Strings()
    ma.main()