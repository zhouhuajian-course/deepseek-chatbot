import requests
import json

url = "https://api.deepseek.com/chat/completions"

payload = json.dumps({
  "messages": [
    # {
    #   "content": "You are a software developer",
    #   "role": "system"
    # },
    {
      "content": "Hi",  # Hello! How can I assist you today? 😊
      "role": "user"    # 你好！很高兴见到你。你今天想学些什么中文呢？
    }                   # Hello! How can I assist you today? Are you working on a coding project, or do you have a question about software development? Let me know! 😊
  ],
  "model": "deepseek-chat",
  "n": 1,
  "stream": True
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer sk-492ec2acc35c4d20b6ab2c9490fcef0d'
}

response = requests.request("POST", url, headers=headers, data=payload, stream=True)
print(response.status_code)
print(response.headers['Content-Type'])
# print(response.text)
# robot_message = response.json()['choices'][0]['message']['content']

for line in response.iter_lines():
    # print(line)
    if not line:
        continue
    if line == b'data: [DONE]':
        print("DONE")
    else:
        chunk = json.loads(line[6:])['choices'][0]['delta']['content']    
        if not chunk:
            continue
        print(chunk)



"""
data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"Hello"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"!"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" How"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" can"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" I"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" assist"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" you"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" today"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":"?"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":" 😊"},"logprobs":null,"finish_reason":null}]}

data: {"id":"2da1725d-8eec-4612-a8da-e76cd896052b","object":"chat.completion.chunk","created":1742954476,"model":"deepseek-chat","system_fingerprint":"fp_3d5141a69a_prod0225","choices":[{"index":0,"delta":{"content":""},"logprobs":null,"finish_reason":"stop"}],"usage":{"prompt_tokens":4,"completion_tokens":11,"total_tokens":15,"prompt_tokens_details":{"cached_tokens":0},"prompt_cache_hit_tokens":0,"prompt_cache_miss_tokens":4}}

data: [DONE]


"""










# for line in response.iter_lines():
#     # print(line)
#     if not line:
#         continue
#     if line == b'data: [DONE]':
#         print("DONE")
#     else:
#         chunk = json.loads(line[6:])['choices'][0]['delta']['content']    
#         if not chunk:
#             continue
#         print(chunk)
