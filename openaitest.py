import os
import openai
from config import apikey
print(apikey)
openai.api_key = apikey
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation\n",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)
#Sample Response
#
# {
#   "id": "cmpl-7Wpu0qiJUjbPtUMCbcssqFieDUqeV",
#   "object": "text_completion",
#   "created": 1688060364,
#   "model": "text-davinci-003",
#   "choices": [
#     {
#       "text": "\nSubject: Resignation \n\nDear [Boss's Name], \n\nI am writing to inform you that I have decided to resign from my position as [Position] with [Company].\n\nAlthough my time at [Company] has been enjoyable, I feel that it is now time for me to pursue other opportunities. I am grateful for the support and direction you have provided me over the past [time worked with company]. \n\nI will be sure to have all of my work up-to-date and will also be available to offer assistance in the transition period.\n\nThank you again for the opportunity and for the valuable experience I have gained here at [Company].\n\nSincerely, \n\n[Your Name]",
#       "index": 0,
#       "logprobs": null,
#       "finish_reason": "stop"
#     }
#   ],
#   "usage": {
#     "prompt_tokens": 9,
#     "completion_tokens": 153,
#     "total_tokens": 162
#   }
# }