from typing import List, Dict


class ResearcherAgent:
    """A simple researcher that drafts key points and a short summary.

    This version is deterministic and does not call external LLMs.
    """

    def run(self, topic: str) -> Dict[str, object]:
        normalized_topic = topic.strip().rstrip("?.!")

        key_points: List[str] = [
            f"What is {normalized_topic}?",
            f"Why {normalized_topic} matters",
            f"Common challenges with {normalized_topic}",
            f"Best practices to apply {normalized_topic}",
            f"Getting started resources for {normalized_topic}",
        ]

        summary_sentences: List[str] = [
            f"{normalized_topic} is an area focused on practical application and impact.",
            "It benefits from clear goals, tight feedback loops, and iterative improvement.",
            "Key challenges usually include ambiguity, evaluation, and integration into existing systems.",
            "A lightweight plan with measurable checkpoints helps de-risk execution.",
        ]
        summary = " ".join(summary_sentences)

        return {
            "topic": normalized_topic,
            "key_points": key_points,
            "summary": summary,
        }


class WriterAgent:
    """A simple writer that turns research notes into a brief article."""

    def run(self, topic: str, research: Dict[str, object]) -> str:
        normalized_topic = topic.strip().rstrip("?.!")
        key_points = research.get("key_points", [])
        summary = research.get("summary", "")

        intro = (
            f"An ultra-brief primer on {normalized_topic}.\n\n"
            f"{summary}\n\n"
        )

        bullets = "\n".join(f"- {point}" for point in key_points)

        closing = (
            "\n\nPutting it into practice:\n"
            f"1) Pick a small {normalized_topic} task.\n"
            f"2) Write down success criteria.\n"
            f"3) Iterate with short feedback loops.\n"
        )

        return intro + bullets + closing
