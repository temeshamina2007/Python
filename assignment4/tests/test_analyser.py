import unittest
from analytics.analyser import TopStudentsAnalyser


class TestAnalyser(unittest.TestCase):

    def setUp(self):
        self.sample = [
            {"student_id": "1", "GPA": "3.8", "country": "USA", "major": "CS", "final_exam_score": "95"},
            {"student_id": "2", "GPA": "2.5", "country": "India", "major": "Business", "final_exam_score": "72"},
            {"student_id": "3", "GPA": "3.9", "country": "USA", "major": "CS", "final_exam_score": "98"},
            {"student_id": "4", "GPA": "1.8", "country": "Canada", "major": "Math", "final_exam_score": "55"},
            {"student_id": "5", "GPA": "3.5", "country": "India", "major": "Law", "final_exam_score": "88"},
        ]

    def test_result_is_not_empty(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertNotEqual(analyser.result, {})

    def test_total_students(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        self.assertIn("top_10", analyser.result)

    def test_analyse_twice(self):
        analyser = TopStudentsAnalyser(self.sample)
        analyser.analyse()
        result1 = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, result1)


if __name__ == "__main__":
    unittest.main()