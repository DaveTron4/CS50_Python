from fpdf import FPDF, Align

def main():
    shirtificate(input("Name: "))

def shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", "", 50)
    pdf.ln(20)
    pdf.cell(text = "CS50 Shirtificate", center = True)
    pdf.ln(90)
    pdf.image("shirtificate.png", x = Align.C, y = 70, w = 200, h = 200)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "", 30)
    pdf.cell(text = f"{name} took CS50", center = True)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()