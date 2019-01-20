import io
import time
from datetime import date
import datetime
import pdfrw
from reportlab.pdfgen import canvas

date = (date.today())
dt = datetime.datetime.strptime(str(date), '%Y-%m-%d')
print('{0}.{1}.{02}'.format(dt.month, dt.day, dt.year))
print(date)


def run():
    canvas_data = get_overlay_canvas()
    form = merge(canvas_data, template_path=r'C:\Users\Steph\Desktop\BoaVista\test.pdf')
    save(form, filename='merged.pdf')


def get_overlay_canvas() -> io.BytesIO:
    data = io.BytesIO()
    pdf = canvas.Canvas(data)
    pdf.drawString(x=163, y=12, text=str(date))
    pdf.drawString(x=163, y=500, text='Johnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn')
    pdf.
    pdf.save()
    data.seek(0)

    return data


def merge(overlay_canvas: io.BytesIO, template_path: str) -> io.BytesIO:
    template_pdf = pdfrw.PdfReader(template_path)

    overlay_pdf = pdfrw.PdfReader(overlay_canvas)
    for page, data in zip(template_pdf.pages, overlay_pdf.pages):

        overlay = pdfrw.PageMerge().add(data)[0]
        pdfrw.PageMerge(page).add(overlay).render()
    form = io.BytesIO()
    pdfrw.PdfWriter().write(form, template_pdf)
    form.seek(0)

    return form


def save(form: io.BytesIO, filename: str):
    with open(filename, 'wb') as f:
        f.write(form.read())


if __name__ == '__main__':
    run()