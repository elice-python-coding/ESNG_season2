class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [word for word in re.sub(r'[^\w]', " ", paragraph).lower().split() if word not in banned]
        dic = {}
        for i in paragraph:
            dic[i] = 0
        for i in paragraph:
            dic[i] += 1
        answer = [k for k, v in dic.items() if max(dic.values()) == v]

        return (answer[0])
