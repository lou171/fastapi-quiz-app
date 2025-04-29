class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_current_question(self):
        if self.still_has_questions():
            return self.question_list[self.question_number]
        return None

    def check_answer(self, user_answer):
        correct_answer = self.question_list[self.question_number].answer.lower()
        if user_answer.lower() == correct_answer:
            self.score += 1
        self.question_number += 1

    def feedback_text(self, score):
        if score <= 2:
            return "Looks like you’re just getting started. Keep practicing and try again!"
        elif score <= 5:
            return "Not bad, but there’s room for improvement. Give it another go!"
        elif score <= 8:
            return "Good job! You’ve got a solid understanding, just a little more to go!"
        elif score <= 11:
            return "Great work! You’re really close to perfect. Excellent effort!"
        else:
            return "Outstanding! You got a perfect score. You really know your stuff!"

