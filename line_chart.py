import pandas as pd
from bokeh.plotting import figure, show, output_file 
from bokeh.models import ColumnDataSource 

# Membaca data dari file
data = pd.read_csv('soal_chart_bokeh.txt', delimiter='\t')

# Membuat ColumnDataSource dari data
source = ColumnDataSource(data)

# Membuat figure
p = figure(title="Testing Jaringan", x_axis_label='Date Time', y_axis_label='Speed (Mbps)', x_axis_type='datetime')

# Menambahkan garis ke figure
p.line(x='Date Time', y='Speed', source=source, line_width=2)

# Menyimpan output ke file HTML
output_file("line_chart.html")

# Menampilkan grafik
show(p)
