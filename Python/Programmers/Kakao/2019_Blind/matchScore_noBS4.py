"""
a. Data
 1. 기본 점수    : 해당 웹 페이지의 텍스트 중 검색어가 등장하는 횟수(대소문자 무시)
 2. 외부 링크 수 : 다른 외부 페이지로 연결된 링크의 수
 3. 링크 점수    : 해당 페이지로 링크가 걸리는 모든 페이지의 (기본점수 % 외부 링크 수)의 총합
 4. 매칭 점수    : 기본 점수 + 링크 점수

b. Output
 1. 매칭점수가 가장 높은 웹페이지의 Index (동일 점수 시 작은 Index)

c. Constract
 1. pages : string array (length : 1 ~ 20)
    page : string (length 1 ~ 1500)
        index, page index : 0 ~
        in url  : head > meta > content
        out url : a > href
        url : "https://*"
    word : english word (length : 1 ~ 12)
    search : 단어 단위 비교, 대소문자 무시
    동일 점수 시 작은 Index 출력
d. Input Exmaple
    word : blind
    pages :
        <html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">
            <head>
              <meta charset="utf-8">
              <meta property="og:url" content="https://a.com"/>
            </head>
            <body>
            Blind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit.
            <a href="https://b.com"> Link to b </a>
            </body>
        </html>

        <html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">
            <head>
              <meta charset="utf-8">
              <meta property="og:url" content="https://b.com"/>
            </head>
            <body>
            Suspendisse potenti. Vivamus venenatis tellus non turpis bibendum,
            <a href="https://a.com"> Link to a </a>
            blind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.
            <a href="https://c.com"> Link to c </a>
            </body>
        </html>

        <html lang="ko" xml:lang="ko" xmlns="http://www.w3.org/1999/xhtml">
            <head>
              <meta charset="utf-8">
              <meta property="og:url" content="https://c.com"/>
            </head>
            <body>
            Ut condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind
            <a href="https://a.com"> Link to a </a>
            </body>
        </html>
"""


class pageInfo:
    def __init__(self, inUrl, outUrl, baseScore):
        self.inUrl = inUrl
        self.outUrl = outUrl

        self.baseScore = baseScore # 기본 점수
        self.outLinkNum = len(outUrl) # 외부 링크 수

        self.inLinkScore = float(self.baseScore) / float(self.outLinkNum)# 내부 링크 점수

        self.LinkScore = 0 # 링크 점수
        self.matchingScore = baseScore # 매칭 점수 (기본 점수 + 링크 점수)

import re

def solution(word, pages):
    answer = 0
    pageinfos = {}
    for page in pages:
        metaParser = re.compile('<meta property="og:url" content="(.+?)/>').findall(page)
        hrefParser = re.compile('<a href="(.+?)">').findall(page)


        bodyParser = re.compile('<body(.+?)>')  # <meta property="og:url" content="

        print(1)

    return answer




# print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))
print(solution("Muzi", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]))