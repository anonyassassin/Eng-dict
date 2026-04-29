from groq import Groq
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
import os

# Initialize components
console = Console()
# Ensure your API key is set in your environment variables
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
                    "role": "user",
                    "content": "Act as a technical dictionary. Explain the following engineering concept in brief sentences for a student's notebook. If it has primary parts, also explain them briefly in one sentence. Concept: {}".format(user_input)
                }
            ],
            temperature=0.7, # Lowered slightly for more consistent "dictionary" style
            stream=True
        )

        full_response = ""
        
        # Use Live to render Markdown as it streams
        with Live(console=console, refresh_per_second=8, vertical_overflow="visible") as live:
            for chunk in completion:
                content = chunk.choices[0].delta.content or ""
                full_response += content
                # This line converts the accumulated text into formatted Markdown
                live.update(Markdown(full_response))

        print("\n") # Add space before the next prompt

    except KeyboardInterrupt:
        console.print("\n[bold red]Shutting down... Bye![/bold red]")
        break
