from fpdf import FPDF
import pandas as pd
data = pd.read_csv("data.csv")
summary = data.describe(include="all")
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Data Report", border=False, ln=True, align="C")
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")
    def add_table(self, dataframe):
        self.set_font("Arial", "B", 10)
        col_width = self.w / (len(dataframe.columns) + 1)
        for col in dataframe.columns:
            self.cell(col_width, 10, str(col), border=1, align="C")
        self.ln()
        self.set_font("Arial", "", 9)
        for i in range(len(dataframe)):
            for col in dataframe.columns:
                self.cell(col_width, 10, str(dataframe.iloc[i][col]), border=1, align="C")
            self.ln()
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, "Summary Statistics", ln=True)
summary_reset = summary.reset_index()
pdf.add_table(summary_reset)
pdf.output("report.pdf")
print("PDF report generated successfully: report.pdf")
