''' https://leetcode.com/problems/word-ladder/
'''

class Solution:    
    def ladderLength(self, beginWord, endWord, wordList):

        def one_letter_away(word1, word2):
            ''' Check if those 2 words are 1 letter apart
            '''
            mismatches = 0
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    mismatches += 1
                    if mismatches == 2:
                        return False
            return True

        # Set for faster lookup
        wordlist_set = set(wordList)

        # Final word not in the list: impossible
        if endWord not in wordlist_set:
            return 0
        
        # with 1 letter words it is 2
        if len(beginWord) == 1:
            return 2

        # Words we just reach (use to look for the next step)
        just_reached = set([beginWord])
        # Seen words (can ignore)
        seen = set([beginWord])

        # Subsets by first and last letters
        first = {ch:[] for ch in "abcdefghijklmnopqrstuvwxyz"}
        last = {ch:[] for ch in "abcdefghijklmnopqrstuvwxyz"}
        for word in wordList:
            first[word[0]].append(word)
            last[word[-1]].append(word)

        # count steps
        steps = 1

        # With every step expand out reach into the words
        while True:

            steps += 1

            # Track new reach
            new_reached = set()

            # Look at every word we have
            for word in just_reached:

                # And see if we can move to the next one
                for potential_reach in first[word[0]] + last[word[-1]]:

                    # No need to check if we alreacy reached this word
                    if potential_reach in seen:
                        continue

                    if one_letter_away(word, potential_reach):
                        new_reached.add(potential_reach)

            if endWord in new_reached:
                return steps
            if len(new_reached) == 0:
                return 0

            just_reached = new_reached
            seen.update(just_reached)


def main():
    ''' Test ladderLength
    '''
    solution = Solution()

    test_cases = [
        ("hit", "cog", ["hot","dot","dog","lot","log","cog"]), #5
        ("hit", "cog", ["hot","dot","dog","lot","log"]), #0
        ("cet", "ism", ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim"]),

    ]
    for beginWord, endWord, wordList in test_cases:
        result = solution.ladderLength(beginWord, endWord, wordList)
        print(beginWord, endWord, wordList, result)


if __name__ == "__main__":
    main()
