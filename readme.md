# Chat bot using langchain and langgraph

## Example usage

```
User: hi whats your name?
Assistant: Hello! I'm an AI assistant and I don't have a personal name, but you can call me Assistant. How can I help you today?
User: My name is James
Assistant: Nice to meet you, James! How can I assist you today?
User: Can you lookup my name to see how much loan I have left?
Assistant:
Search tool invoked
Assistant: [Document(id='f109074b-21b6-41d9-87e1-562ea8f4cd05', metadata={'id': 'c82e4930-68b0-4787-9614-47fc7101e28a', 'name': 'James Martinez', ...
Assistant: I found some information regarding a loan under the name James Martinez. Here are the details:

- **Total Loan Amount**: $87,220
- **Remaining Loan Balance**: $62,619
- **Monthly Payment**: $4,846
- **Date of Loan**: June 11, 2023
- **Monthly Payment Date**: 8th of each month

If this matches your details, then this is your loan information. If it doesn't, please let me know, and we can try another search or verify the details.
User: q
Goodbye!
```

## Prerequisites

### Dependencies

```sh
pip install -r requirements.txt
```

### Database

We will use postgres with pgvector extension

```sh
docker run --name pgvector-container \
  -e POSTGRES_USER=langchain \
  -e POSTGRES_PASSWORD=langchain \
  -e POSTGRES_DB=langchain \
  -p 6024:5432 \
  -d pgvector/pgvector:pg16
```

### Environment variables

Example .env file is located at [.env.example](./.env.example):

```
OPENAI_API_KEY=sk-...

# For customers lookup
DATABASE_URL=postgresql+psycopg://langchain:langchain@localhost:6024/langchain

# For web search
TAVILY_API_KEY=tvly-...
COMPANY_DOMAIN=https://www.acme.com
```
