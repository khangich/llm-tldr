# llm-tldr
Short description of LLM research and development

# Papers
## Chain of Thought (Jason Wei 2023) 

Paper: [Chain Of Thought](https://proceedings.neurips.cc/paper_files/paper/2022/file/9d5609613524ecf4f15af0f7b31abca4-Paper-Conference.pdf)

A new prompting technique to improve LLM reasoning performance. 

- Example 1: 

![Screenshot 2024-05-02 at 14 00 56](https://github.com/khangich/llm-tldr/assets/1975237/70ee1c21-17ea-4269-9c4e-c0b5152e38b3=150x)


- Example 2:

![Screenshot 2024-05-02 at 14 03 15](https://github.com/khangich/llm-tldr/assets/1975237/eaf4468e-7a99-4b1e-b11b-3e010992c7c7=150x)

- Result: for Math, CoT can improve 2x solve rate


![Screenshot 2024-05-02 at 14 06 24](https://github.com/khangich/llm-tldr/assets/1975237/a05711fb-3e79-4acd-b20d-b93b2f053060=150x)

- One liner command
 ```
curl -X POST "https://api.openai.com/v1/chat/completions" \
         -H "Authorization: Bearer YOUR_API_KEY" \
         -H "Content-Type: application/json" \
         -d '{
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": "Explain the steps to find the least common multiple (LCM) of these numbers: [12, 15, 18] and provide the answer in JSON format with your thoughts and the final answer."}
                ],
                "max_tokens": 250,
                "temperature": 0.3,
                "n": 1,
                "stop": null
             }'
```


[Github Workspace][https://github.com/codespaces/new/khangich/llm-tldr]

## ReAct (Shunyu Yao 2023) 

Paper: [ReAct](https://arxiv.org/pdf/2210.03629)

- Example 1:
- Example 2:
- Result
- Weblink diagram

```
+-------------------+      +-------------------+      +-------------------+
|   Reset Env with  |      |   Generate Thought|      |   Execute Action  |
|   Question (idx)  |----->|   & Action using  |----->|   in Environment  |
|                   |      |   LLM Function    |      |   & Get Obs       |
+-------------------+      +-------------------+      +-------------------+
           |                        |                          |
           |                        |                          |
           v                        v                          v
+-------------------+      +-------------------+      +-------------------+
|   Update Prompt   |<-----|   Format Response |<-----|   Check if Done   |
|   with Question   |      |   & Handle Errors |      |   & Update Prompt |
+-------------------+      +-------------------+      +-------------------+
```
