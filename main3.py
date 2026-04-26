import os
import csv
import json


class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")

        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder="output"):
        print("Checking output folder...")

        if os.path.exists(folder):
            print(f"Output folder already exists: {folder}/")
        else:
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")


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
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
            return []

        except Exception as e:
            print(f"Error while loading data: {e}")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)

        for student in self.students[:n]:
            print(
                f"{student['student_id']} | "
                f"{student['age']} | "
                f"{student['gender']} | "
                f"{student['country']} | "
                f"GPA: {student['GPA']}"
            )

        print("-" * 30)


class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        valid_students = []

        for student in self.students:
            try:
                float(student["final_exam_score"])
                float(student["GPA"])
                valid_students.append(student)

            except ValueError:
                print(f"Warning: could not convert value for student {student['student_id']} — skipping row.")
                continue

            except KeyError:
                print("Warning: required column is missing — skipping row.")
                continue

        top10 = sorted(
            valid_students,
            key=lambda student: float(student["final_exam_score"]),
            reverse=True
        )[:10]

        top_10_list = []

        for i in range(len(top10)):
            student = top10[i]

            top_10_list.append({
                "rank": i + 1,
                "student_id": student["student_id"],
                "country": student["country"],
                "major": student["major"],
                "final_exam_score": float(student["final_exam_score"]),
                "GPA": float(student["GPA"])
            })

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": top_10_list
        }

        return self.result

    def print_results(self):
        print("-" * 30)
        print("Top 10 Students by Exam Score")
        print("-" * 30)

        for student in self.result["top_10"]:
            print(
                f"{student['rank']}. "
                f"{student['student_id']} | "
                f"{student['country']} | "
                f"{student['major']} | "
                f"Score: {student['final_exam_score']} | "
                f"GPA: {student['GPA']}"
            )

        print("-" * 30)

        print("=" * 30)
        print("ANALYSIS RESULT")
        print("=" * 30)
        print(f"Analysis : {self.result['analysis']}")
        print(f"Total students : {self.result['total_students']}")
        print("Top 10 saved to output/result.json")
        print("=" * 30)

    def lambda_map_filter(self):
        print("-" * 30)
        print("Lambda / Map / Filter")
        print("-" * 30)

        try:
            top_scorers = list(filter(lambda s: float(s["final_exam_score"]) > 95, self.students))
            gpa_values = list(map(lambda s: float(s["GPA"]), self.students))
            good_assignments = list(filter(lambda s: float(s["assignment_score"]) > 90, self.students))

            print(f"final_exam_score > 95 : {len(top_scorers)}")
            print(f"GPA values (first 5) : {gpa_values[:5]}")
            print(f"assignment_score > 90 : {len(good_assignments)}")

        except ValueError:
            print("Warning: could not convert one of the values.")

        except KeyError:
            print("Warning: one of the required columns is missing.")

        print("-" * 30)


class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as file:
                json.dump(self.result, file, indent=4)

            print(f"Result saved to {self.output_path}")

        except Exception as e:
            print(f"Error while saving result: {e}")


def main():
    filename = "students.csv"
    output_path = "output/result.json"

    file_manager = FileManager(filename)

    if not file_manager.check_file():
        print("Stopping program.")
        return

    file_manager.create_output_folder()

    data_loader = DataLoader(filename)
    data_loader.load()
    data_loader.preview()

    analyser = DataAnalyser(data_loader.students)
    analyser.analyse()
    analyser.print_results()
    analyser.lambda_map_filter()

    saver = ResultSaver(analyser.result, output_path)
    saver.save_json()

    wrong_loader = DataLoader("wrong_file.csv")
    wrong_loader.load()


main()