import openai
from random import randint
from time import sleep

# API KEY
openai_api_key = "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"
openai.api_key = openai_api_key


# path
output_path = "/Users/kimgeunyoung/2학년 2학기/GPT/ex_after.txt"

# import 요약 전 이유 txt file path
f = open('/Users/kimgeunyoung/2학년 2학기/GPT/ex.txt')

# 변수 준비
summary = ''
n=0

for x in f.readlines():
    #sleep(randint(5,10))
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[{"role": "user", "content": "{}원문에서 주요 정보 잘 요약하고 한 문장으로 정리해서 저장해줘. 그리고 문어체 사용해줘".format(x)}]
    )
    print(response.choices[0].message.content)
    summary += response.choices[0].message.content
    summary += "\n"
    n+=1

with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write(summary)