class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        parsed_letters = ""

        for letter in ransomNote:
            if letter not in parsed_letters:
                if letter not in magazine or magazine.count(letter) < ransomNote.count(letter):
                    return False
                parsed_letters += letter
  
        return True
