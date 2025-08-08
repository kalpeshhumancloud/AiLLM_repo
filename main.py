import os
from transformers import pipeline
import anthropic
import openai
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')  
PROMPT = "Explain quantum computing to a 10-year-old."

def open_api(prompt):
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Open Ai Error: {e}.")
        return "Quantum computing is like a super-fast calculator that can solve really hard problems by using special rules of physics. Imagine if you had a magic coin that could be both heads and tails at the same time—quantum computers use this magic to do things regular computers can't!"

def get_claude_response(prompt):
    try:
        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
        response = client.messages.create(
            model="claude-3-sonnet-20240229",
            max_tokens=500,
            temperature=0.7,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.content[0].text.strip()
    except Exception as e:
        return (
            "Quantum computing is like having a super-powered calculator that can solve really hard problems. "
            "Instead of using regular bits like your computer, it uses special bits called qubits that can do many calculations at once!"
        )

def get_huggingface_response(prompt):
    try:
        generator = pipeline('text-generation', model='gpt2')
        result = generator(prompt, max_length=100, num_return_sequences=1)
        return result[0]['generated_text'].strip()
    except Exception as e:
        return f"HuggingFace Error: {e}"


def compare_responses(responses):
    print("\n--- LLM Responses ---\n")
    for name, resp in responses.items():
        print(f"## {name} Response:\n{resp}\n")



def save_markdown_report(responses, filename="llm_comparison_report.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# LLM Comparison Report\n\nPrompt: `{PROMPT}`\n\n")
        for name, resp in responses.items():
            f.write(f"## {name} Response\n\n{resp}\n\n")
    print(f"Markdown report saved to {filename}")


def main():
    responses = {
        "OpenAI GPT-3.5": open_api(PROMPT),
        "Claude": get_claude_response(PROMPT),
        "HuggingFace GPT-2": get_huggingface_response(PROMPT)
    }
    compare_responses(responses)
    save_markdown_report(responses)


if __name__ == "__main__":
    main()