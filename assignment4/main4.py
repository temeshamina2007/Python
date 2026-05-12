from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import TopStudentsAnalyser, GpaAnalyser


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

    top_students_analyser = TopStudentsAnalyser(data_loader.students)
    gpa_analyser = GpaAnalyser(data_loader.students)

    print("-" * 30)
    print("Running all analysers:")
    print("-" * 30)

    analysers = [top_students_analyser, gpa_analyser]

    for analyser in analysers:
        print(analyser)
        analyser.analyse()
        analyser.print_results()

    saver = ResultSaver(top_students_analyser.result, output_path)
    report = Report(top_students_analyser, saver)
    report.generate()

    wrong_loader = DataLoader("wrong_file.csv")
    wrong_loader.load()


if __name__ == "__main__":
    main()