from groq import Groq
import groq
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
import os

console = Console()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

console.print("[bold green]Engineering Dictionary Active.[/bold green] Press Ctrl+C to exit.\n")

while True:
    try:
        user_input = input("Enter the concept: ")
        if not user_input.strip():
            continue

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are a professional engineering analyst. For every concept, follow this EXACT structure:\n\n"
                        "1. **Summary Paragraph**: A 2-3 sentence overview of the system/concept and its primary cycle or physics principle.\n"
                        "2. **Core Components**: A list of the 4-5 most vital parts. Each must have a bold name followed by a colon and a 1-2 sentence technical explanation.\n"
                        "3. **Auxiliary Components**: A list of supporting systems or subsystems that improve efficiency or operation, with 1-sentence explanations.\n"
                        "4. **Efficiency/Conclusion**: A final sentence regarding typical thermal efficiency, output ranges, or a key performance metric.\n\n"
                        "DO NOT include intros like 'Here is the info'. Get straight to the text."
                    )
                },
                {
                    "role": "user",
                    "content": "Explain: {}".format(user_input)
                }
            ],
            temperature=0.2, # LOWER temperature = LESS repetition
            max_tokens=500,  # Limits the response length
            stream=True
        )

        full_response = ""
        
        with Live(console=console, refresh_per_second=10, vertical_overflow="visible") as live:
            for chunk in completion:
                content = chunk.choices[0].delta.content or ""
                full_response += content
                live.update(Markdown(full_response))

        print("\n" + "—" * 20 + "\n") 

    except KeyboardInterrupt:
        console.print("\n[bold red]Shutting down... Bye![/bold red]")
        break
    except groq.APIConnectionError:
        console.print("\n[bold red]Error: Check your connection and try again.")
        break # Changed exit() to break to be cleaner
