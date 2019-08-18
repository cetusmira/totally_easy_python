#section_02.py

from collections import Counter

wordDict = Counter()
with open('KakaoTalkChats.txt', 'r', encoding='utf-8') as f:

    chatline = f.readlines()
    chatline = [x.strip() for x in chatline]
    chatline = [x for x in chatline if x]

    for count in range(len(chatline)):
        if count < 2:               # 첫 두 줄 제거
            continue

        wordlist = chatline[count].split(':')
        if len(wordlist) == 2 :     # 매일 대화시작 시간 제거
            continue

        if len(wordlist) == 1 :     # 엔터[Enter]가 삽입된 경우
            for word in wordlist[0].strip().split():
                wordDict[word] += 1
        else:
            for x in range(2, len(wordlist)):   # ‘:’가 있는 경우
                for word in wordlist[x].strip().split():
                    wordDict[word] += 1

print('단어 \t\t 빈도수')
for word, freq in wordDict.most_common(50):
    print('{0:10s} \t: {1:3d}'.format(word, freq))
