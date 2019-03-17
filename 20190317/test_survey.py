import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self): # 設計測試實例並存成屬性使用
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Japanese']

    def test_store_single_response(self):
        """Test that a single response is stores properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

# python 會自動執行 test_ 開頭的方法
unittest.main()
# 每完成單元測試時python會印出一個 "." ，測試未通過則印出"E"字元，若測試引起assert方法失敗時印出"F"字元