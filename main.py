from agents import ResearcherAgent, WriterAgent


def run_demo(topic: str) -> str:
    researcher = ResearcherAgent()
    writer = WriterAgent()

    research = researcher.run(topic)
    article = writer.run(topic, research)
    return article


if __name__ == "__main__":
    demo_topic = "Agentic AI"
    print(run_demo(demo_topic))
