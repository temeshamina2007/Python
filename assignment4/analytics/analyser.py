class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class TopStudentsAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        valid_students = []

        for student in self.students:
            try:
                float(student["final_exam_score"])
                float(student["GPA"])
                valid_students.append(student)

            except ValueError:
                print("Warning: could not convert value — skipping row.")

            except KeyError:
                print("Warning: required column is missing — skipping row.")

        top10 = sorted(
            valid_students,
            key=lambda student: float(student["final_exam_score"]),
            reverse=True
        )[:10]

        top_10_list = []

        for i, student in enumerate(top10):
            top_10_list.append({
                "rank": i + 1,
                "student_id": student.get("student_id", "N/A"),
                "country": student.get("country", "N/A"),
                "major": student.get("major", "N/A"),
                "final_exam_score": float(student["final_exam_score"]),
                "GPA": float(student["GPA"])
            })

        high_score_students = list(
            filter(lambda s: float(s["final_exam_score"]) > 90, valid_students)
        )

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top_10_list,
            "students_with_score_above_90": len(high_score_students)
        }

        return self.result

    def print_results(self):
        print("=" * 30)
        print("TOP STUDENTS ANALYSIS REPORT")
        print("=" * 30)

        super().print_results()

        print("=" * 30)

    def __str__(self):
        return f"TopStudentsAnalyser: Top 10 Students, {len(self.students)} students"


class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        valid_gpa = []

        for student in self.students:
            try:
                valid_gpa.append(float(student["GPA"]))
            except (ValueError, KeyError):
                continue

        high_performers = list(filter(lambda gpa: gpa > 3.5, valid_gpa))

        self.result = {
            "total_students": len(self.students),
            "average_gpa": round(sum(valid_gpa) / len(valid_gpa), 2) if valid_gpa else 0,
            "max_gpa": max(valid_gpa) if valid_gpa else 0,
            "min_gpa": min(valid_gpa) if valid_gpa else 0,
            "high_performers": len(high_performers)
        }

        return self.result

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)

        super().print_results()

        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"