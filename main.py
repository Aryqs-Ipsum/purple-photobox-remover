from PIL import Image
import colorsys

def progressBar(current, total, barLength = 20):
    percent = float(current) * 100 / total
    arrow   = '-' * int(percent/100 * barLength - 1) + '>'
    spaces  = ' ' * (barLength - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

def replacePixel(x, y, pxdata, hue, tolerance):
    px = pxdata[x, y]
    hsv = colorsys.rgb_to_hsv(px[0], px[1], px[2])
    pxhue = hsv[0]
    if pxhue >= hue - hue * tolerance and pxhue <= hue + hue * tolerance:
        pxdata[x, y] = (0, 0, 0, 255 - hsv[2])

def main():
    filename = input('Image location : ')
    tolerance = int(input('Tolerance (in %, 10 by default) : ') or 10) / 100

    hue = 308 / 360

    img = Image.open('input/' + filename)
    img = img.convert("RGBA")

    pxdata = img.load()

    [width, height] = img.size
    for x in range(width):
        progressBar(x, width)
        for y in range(height):
            replacePixel(x, y, pxdata, hue, tolerance)

    img.save('output/' + str(tolerance) + filename + '.png', 'PNG')

main()