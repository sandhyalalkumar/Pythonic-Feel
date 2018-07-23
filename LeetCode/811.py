class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domap = {}
        for ele in cpdomains:
            value, key = ele.split()
            domap.update({key:int(value)})

        ndomap = {}
        for key, value in domap.iteritems():
            ndomap.update({key : value})
            words = key.split(".")
            if len(words) == 2:
                if words[1] in ndomap:
                    ndomap.update({words[1]:ndomap[words[1]]+value})
                else:
                    ndomap.update({words[1]:value})
            if len(words) == 3:
                if words[2] in ndomap:
                    ndomap.update({words[2]:ndomap[words[2]]+value})
                else:
                    ndomap.update({words[2]: value})

                if words[1]+"."+words[2] in ndomap:
                    ndomap.update({words[1]+"."+words[2]: ndomap[words[1]+"."+words[2]]+value})
                else:
                    ndomap.update({words[1] + "." + words[2]: value})

        domaincounts = []
        for key, value in ndomap.iteritems():
            domaincounts.append(str(value)+ " " + key)
        return domaincounts



if __name__ == "__main__":

    s = Solution()
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    cpdomains = ["9001 discuss.leetcode.com"]
    cpdomains = ["1001 google.com"]
    print s.subdomainVisits(cpdomains)

    #['50 yahoo.com', '901 mail.com', '900 google.mail.com', '5 wiki.org', '1 intel.mail.com', '5 org', '951 com']
    #["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]
    ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]