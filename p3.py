class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
            a = [list(i.split(" ")) for i in logs]
            digit =[]
            string = []
            for i in a:
                if i[1].isdigit():
                    digit.append(" ".join(i))
                else:
                    string.append(i)
            string.sort(key=lambda x:(x[1:],x[0]))
            string = [" ".join(i) for i in string]
            return string + digit