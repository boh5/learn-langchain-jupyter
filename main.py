def main():
    from langchain.chat_models import init_chat_model
    from dotenv import load_dotenv

    load_dotenv()

    model = init_chat_model(
        model="gpt-4o",
        model_provider="openai",
        temperature=0,
        base_url="https://new-api-latest-m0yh.onrender.com",
    )

    model.invoke("你好")


if __name__ == "__main__":
    main()
from langchain_core.runnables.history import RunnableWithMessageHistory
