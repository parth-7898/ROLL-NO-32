def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("=" * 60)
        print("DYNAMIC REPORT GENERATOR".center(60))
        print("=" * 60)

        func(*args, **kwargs)

        print("=" * 60)
        print("END OF REPORT".center(60))
        print("=" * 60)

    return wrapper


class Report:

    company_name = "INFOSYS Pvt. Ltd."

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.contents = []

    def add_content(self, text):
        self.contents.append(text)

    @classmethod
    def change_company(cls, new_company):
        cls.company_name = new_company

    @staticmethod
    def line():
        print("-" * 60)

    def __str__(self):
        return f"Report Title : {self.title}\nAuthor       : {self.author}"

    def __len__(self):
        return len(self.contents)

    @report_decorator
    def display_report(self):

        print("Company :", Report.company_name)
        print(self)

        Report.line()

        print("Report Contents:")

        for i, item in enumerate(self.contents, start=1):
            print(f"{i}. {item}")

        Report.line()

        print("Total Sections :", len(self))

r1 = Report("Advanced Python Practical", "Parth")

r1.add_content("Completed Experiment No. 2.")
r1.add_content("Implemented Decorators.")
r1.add_content("Implemented Class Method.")
r1.add_content("Implemented Static Method.")
r1.add_content("Implemented Magic Methods.")

r1.display_report()

print("\nChanging Company Name...\n")

Report.change_company("MICROSOFT Pvt. Ltd.")

r2 = Report("Faculty Demonstration", "Parth")

r2.add_content("Decorator concept explained.")
r2.add_content("Class Method explained.")
r2.add_content("Magic Methods explained.")
r2.add_content("Practical completed successfully.")

r2.display_report()