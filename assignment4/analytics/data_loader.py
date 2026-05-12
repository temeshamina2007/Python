import csv


class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.students = list(reader)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

        except Exception as e:
            print(f"Error while loading data: {e}")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)

        for student in self.students[:n]:
            print(
                f"{student.get('student_id', 'N/A')} | "
                f"{student.get('age', 'N/A')} | "
                f"{student.get('gender', 'N/A')} | "
                f"{student.get('country', 'N/A')} | "
                f"GPA: {student.get('GPA', 'N/A')}"
            )

        print("-" * 30)