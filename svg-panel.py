import svgwrite
from svgwrite.extensions import Inkscape

# units are usually in inches, and are rounded to the nearest 0.001"
# x and y locations are typically centers
# x=0, y=0: top left

def i2p(i):
  # kicad dpi default is 96
  # svg dpi default seems to be 90
  return round(96*i,3)

def i2s(i):
  round(i,3)
  return "{:.3f}in".format(i)

def label_box(x, y, w, h):
  left = x-w/2
  right = x+w/2
  top = y-h/2
  bottom = y+h/2
  offset = w/15
  points = []
  # convert inches to points since "in" doesn't seem to work
  points.append((i2p(left-offset), i2p(bottom)))
  points.append((i2p(left), i2p(top)))
  points.append((i2p(right), i2p(top)))
  points.append((i2p(right-offset), i2p(bottom)))
  tb = dwg.polygon(points)
  return tb

def label_text(x,y,n,th):
  xs = i2s(x)
  ys = i2s(y)
  ths = i2s(th)
  txt = dwg.text(n, insert=(xs,ys), font_family="Consolas", font_weight="bold", font_size=ths, text_anchor="middle", dominant_baseline="central", fill="white")
  return txt

def lbl(x,y,w,h,n,th):
  tb = label_box(x,y,w,h)
  mask.add(tb)
  txt = label_text(x - w/30,y,n,th)
  silk.add(txt)
  #mask.add(txt)

width = 9.8
height = 3.0
dwg = svgwrite.Drawing('panel.svg', profile='full', size=(i2s(width),i2s(height)), debug=True)
ink = Inkscape(dwg)
mask = ink.layer(label='mask', locked=True)
silk = ink.layer(label='silk', locked=True)
dwg.add(mask)
dwg.add(silk)

x  = 1.1    # first column
y  = 0.35   # top row
dx = 1.0    # horizontal spacing
w  = 0.9    # label width
h  = 0.4    # label height
th = 0.275  # text height
thp = i2p(th)

lbl(x,y,w,h,"MAIN",th)
x = x+dx
lbl(x,y,w,h,"PUMP",th)
x = x+dx
lbl(x,y,w,h,"AVIO",th)
x = x+dx
lbl(x,y,w,h,"AV B",th)
x = x+dx
lbl(x,y,w,h,"ACC",th)
x = x+dx
lbl(x,y,w,h,"NAV",th)
x = x+dx
lbl(x,y,w,h,"STRB",th)
x = x+dx
lbl(x,y,w,h,"TAXI",th)
x = x+dx+0.2
lbl(x,y,w,h,"LAND",th)

dwg.save()

