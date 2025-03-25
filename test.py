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
  "n": 1
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer sk-492ec2acc35c4d20b6ab2c9490fcef0d'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.status_code)
print(response.text)
robot_message = response.json()['choices'][0]['message']['content']



# for line in response.iter_lines():
#     # print(line)
#     if line.startswith(b'data: '):
#         data = line[6:]
#         if data == b'[DONE]':
#             print('[DONE]') 
#         else:
#             chunk = json.loads(data)['choices'][0]['delta']['content']    
#             if chunk:
#                 print(chunk)
