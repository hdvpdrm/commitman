# commitman
Mistral AI powered CLI tool to generate commit text based on provided git diff output.

# How to use
### 1. Install required package
```bash
pip install mistralai
```
### 2. Get your own API key
To achieve this goal you need to investigate https://docs.mistral.ai/api/

### 3. Generate commit
```
git diff main.c | ./commitman YOUR_API_KEY
```
