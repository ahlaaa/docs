# -*- coding: utf-8 -*-

# 字体库
import reportlab.lib.fonts
# canvas画图的类库
from reportlab.pdfgen.canvas import Canvas
# 用于定位的inch库，inch将作为我们的高度宽度的单位
from reportlab.lib.units import inch
from reportlab.platypus import Table, SimpleDocTemplate, Paragraph
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter


def pdf_head(canvas, headtext):
    # setFont是字体设置的函数，第一个参数是类型，第二个是大小
    canvas.setFont("Helvetica-Bold", 11.5)
    # 向一张pdf页面上写string
    canvas.drawString(1 * inch, 10.5 * inch, headtext)
    # 画一个矩形，并填充为黑色
    canvas.rect(1 * inch, 10.3 * inch, 6.5 * inch, 0.12 * inch, fill=1)
    # 画一条直线
    canvas.line(1 * inch, 10 * inch, 7.5 * inch, 10 * inch)


if __name__ == "__main__":
    import os
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    from reportlab.platypus import Table as pdfTable

    import os

    os.path.exists('./report.pdf') and os.remove('./report.pdf')
    filename = 'report.pdf'
    p = canvas.Canvas(filename)
    print(getattr(p, '_fontname'))
    style = [
        ('FONTNAME', (0, 0), (-1, -1), getattr(p, '_fontname')),  # 字体
        # ('BACKGROUND', (0, 0), (-1, 0), '#d5dae6'),  # 设置第一行背景颜色
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # 对齐
        ('VALIGN', (-1, 0), (-2, 0), 'MIDDLE'),  # 对齐
        # ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),  # 设置表格框线为grey色，线宽为0.5
    ]
    table_data = [['a', 'b', 'c'], ['dddddddddddd', 'eeeeee', 'f']]
    top_row = pdfTable(table_data, style=style)
    w, h = top_row.wrapOn(p, 0, 0)
    width, height = getattr(p, '_pagesize')
    print(0.75 * inch, 0.5 * inch, w, h)
    top_row.drawOn(p, (width - w) / 2, height - inch)
    p.showPage()
    p.save()
