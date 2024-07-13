from openai import OpenAI
import typer
from rich import print
from rich.table import Table

def main():

    client = OpenAI(
        api_key = "REPLACE-ME"
    )

    context = [{"role" : "system",
                "content" : "Eres un asistente muy útil."}]

    messages =context

    table = Table("Comando","Descripción")
    table.add_row("exit","Salir de la aplicación")
    table.add_row("new","Crear una nueva conversación")

    print(table)

    print("[bold green]ChatGPT api en Python [/bold green]")

    while True:
        content = input("Sobre que quieres hablar? ")

        if content == "exit":
            print("👋 ¡Hasta luego!")
            break;
        elif content == "new":
            messages = context
            response_content = ""
            print("🆕 Nueva conversación creada")
            content = input("Sobre que quieres hablar? ")

        messages.append({"role" : "user", "content" : content})

        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = messages
        )

        response_content = completion.choices[0].message.content

        messages.append({"role" : "assistant", "content" : response_content})

        print(response_content)

if __name__ == "__main__":
    typer.run(main)