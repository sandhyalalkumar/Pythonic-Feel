from itertools import izip
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morsecode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        alphamap = dict(izip(alphabets, morsecode))

        morsewords = set([])
        for w in words:
            mstr = ""
            for c in w:
                mstr = mstr + alphamap[c]
            morsewords.add(mstr)
        return len(morsewords)

if __name__ == "__main__":

    s = Solution()
    words = ["gin", "zen", "gig", "msg"]
    print s.uniqueMorseRepresentations(words)



