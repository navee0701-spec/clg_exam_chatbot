import re

FAQ = [
    (
        [{"revaluation"}, {"recheck"}],
        "Check the official revaluation notice for the application "
        "process, fee, eligibility, and deadline."
    ),
    (
        [{"hall", "ticket"}, {"admit", "card"}],
        "Check the student portal or contact the examination office "
        "for hall ticket availability and collection instructions."
    ),
    (
        [{"result"}, {"results"}],
        "Check the official college results portal or examination "
        "office announcements for published results."
    ),
    (
        [{"missed", "exam"}, {"absent", "exam"}, {"arrear"}],
        "Contact the examination office about the applicable "
        "arrear or next-attempt procedure."
    ),
    (
        [
            {"exam", "schedule"},
            {"exam", "date"},
            {"exam", "dates"},
            {"semester", "exams"},
            {"exam", "timetable"}
        ],
        "Refer to the official examination timetable for "
        "confirmed dates and timings."
    ),
    (
        [{"exam", "fee"}, {"exam", "fees"}],
        "Refer to the official examination fee notice for "
        "the amount, payment method, and last date."
    )
]


def tokenize(text):
    return set(re.findall(r"[a-z]+", text.lower()))


def answer(question):
    words = tokenize(question)

    if not words:
        return "Please enter an examination-related question."

    if words in ({"hi"}, {"hello"}, {"hey"}):
        return "Hello! Ask me about college examinations."

    for patterns, response in FAQ:
        if any(pattern <= words for pattern in patterns):
            return response

    return (
        "I could not match that question. Try exam dates, "
        "hall tickets, results, revaluation, or exam fees. "
        "For other queries, contact the examination office."
    )


def main():
    print("Bot: Welcome to the Examinations FAQ Chatbot.")
    print("Bot: Type exit, quit, or bye to stop.")

    while True:
        question = input("Student: ").strip()

        if question.lower() in {"exit", "quit", "bye"}:
            print("Bot: Thank you. Goodbye!")
            break

        print("Bot:", answer(question))


if __name__ == "__main__":
    main()
