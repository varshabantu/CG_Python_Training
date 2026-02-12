import logging

#Logging configuration
logging.basicConfig(
    filename="exam.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class Exam:
    # class variable
    pass_marks = 40
    def __init__(self, student_id, total_questions, correct_answers):
        self.student_id = student_id
        self.total_questions = total_questions
        self.correct_answers = correct_answers
        self.started = False
        self.submitted = False
        logging.info("Exam object created for student %s", self.student_id)

    # object method to start exam
    def start_exam(self):
        if self.started:
            logging.warning("Exam already started for student %s", self.student_id)
        else:
            self.started = True
            logging.info("Exam started for student %s", self.student_id)

    # object method to submit exam
    def submit_exam(self):
        if not self.started:
            logging.error("Submit failed. Exam not started for student %s", self.student_id)
        elif self.submitted:
            logging.warning("Exam already submitted for student %s", self.student_id)
        else:
            self.submitted = True
            logging.info("Exam submitted for student %s", self.student_id)

    # object method to calculate score
    def calculate_score(self):
        if not self.submitted:
            logging.error(
                "Score calculation failed. Exam not submitted for student %s",
                self.student_id
            )
            return None
        score = self.correct_answers
        if score >= Exam.pass_marks:
            result = "PASS"
        else:
            result = "FAIL"
        logging.info(
            "Score calculated for student %s | Score: %s | Result: %s",
            self.student_id, score, result
        )
        return score, result

    # class method to update pass marks
    @classmethod
    def update_pass_marks(cls, new_marks):
        cls.pass_marks = new_marks
        logging.info("Pass marks updated to %s", new_marks)

e1 = Exam(101, 50, 42)
e1.start_exam()
e1.submit_exam()
result = e1.calculate_score()
logging.info("Returned value from calculate_score(): %s", result)
Exam.update_pass_marks(45)
result = e1.calculate_score()
logging.info("Returned value after pass marks update: %s", result)