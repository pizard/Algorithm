def solution(words, queries):

    queriesAlignment = {}
    for query in queries:
        if not len(query) in queriesAlignment.keys():
            queriesAlignment[len(query)] = {}  # 길이 dict 생성
        if not "num" in queriesAlignment.keys():
            if query[0] != "?": # prefix : 앞에 단어
                queriesAlignment[len(query)][query] = {"num": 0, "regex": keywordToregex(query), "prefix" : True}  # query dict 생성
            else: #suffix
                queriesAlignment[len(query)][query] = {"num": 0, "regex": keywordToregex(query), "prefix" : False}  # query dict 생성

    for word in words:
        for queryAlignment in queriesAlignment[len(word)].values():
            if queryAlignment["regex"] == "":
                queryAlignment["num"] = queryAlignment["num"] + 1
            else:
                if queryAlignment["prefix"] == True:
                    if word[0:len(queryAlignment["regex"])] == queryAlignment["regex"]:
                        queryAlignment["num"] = queryAlignment["num"] + 1
                else:
                    if word[len(word) - len(queryAlignment["regex"]):len(word)] == queryAlignment["regex"]:
                        queryAlignment["num"] = queryAlignment["num"] + 1

    answer = []
    for query in queries:
        answer.append(queriesAlignment[len(query)][query]["num"])

    return answer


def keywordToregex(query):
    regex = query.replace("?", "")
    return regex




solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["?????", "fro??", "????o", "fr???", "fro???", "pro?"])

# if re.match('\?', query):  # 접두사, prefix
#     queriesAlignment[len(query)]["prefix"][query] = 0
# else:  # 접미사, suffix
#     queriesAlignment[len(query)]["suffix"][query] = 0
