import requests
import html


def fetch_questions(amount):
    url = f"https://opentdb.com/api.php?amount={amount}&type=boolean"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if "results" not in data or len(data["results"]) == 0:
            print("No questions available. Please try again later.")
            return []

        question_data = []
        for item in data["results"]:
            question_text = html.unescape(item["question"])
            question_answer = item["correct_answer"]
            question_data.append({"text": question_text, "answer": question_answer})

        return question_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
        return []
    except ValueError:
        print("Error decoding response data. Please try again later.")
        return []

