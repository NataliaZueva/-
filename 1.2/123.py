from drawSvg import SVG
mySVG = SVG()

mySVG.write('test.svg')

mySVG.addChildElement('rect', {'x':20, 'y':40, 'width':80, 'height':50, 'fill': 'blue'})
mySVG.addChildElement('text', {'x':22, 'y':12,}, "Test text")


