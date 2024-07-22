""" Run in DrawBot to generate random colours. Set your desired saturation and luminosity values with the sliders. """

from colorsys import hls_to_rgb
size(1000, 500)

Variable([
    dict(name="Saturation_1", ui="Slider",
            args=dict(

                value=50,
                minValue=0,
                maxValue=100)),
    
    dict(name="Luminosity_1", ui="Slider",
        args=dict(

            value=50,
            minValue=0,
            maxValue=100)),
       
   dict(name="Saturation_2", ui="Slider",
            args=dict(

                value=50,
                minValue=0,
                maxValue=100)),
    
    dict(name="Luminosity_2", ui="Slider",
        args=dict(

            value=50,
            minValue=0,
            maxValue=100)),
    ],
       globals())

hue = randint(0,360)/360
saturation = Saturation_1/100
luminosity = Luminosity_1/100

clr = hls_to_rgb(hue, luminosity, saturation)


hue_2 = randint(0,360)/360
saturation_2 = Saturation_2/100
luminosity_2 = Luminosity_2/100

clr2 = hls_to_rgb(hue_2, luminosity_2, saturation_2)

stripeNumb = 10 # editable number of stripes
gap = 10
w = (width()-gap)/2 / (stripeNumb)
x = w

oSize = 300 # editable size of circle

fill(*clr2)
rect(0, 0, width(), height())
    
for i in range(stripeNumb//2):
    fill(*clr)
    rect(x, 0, w, height())
    x+= w*2
    
fill(1)
rect(width()/2 - gap/2, 0, gap, height())
        
fill(*clr)
xPos = width()/2 + (width()/2 + gap/2)/2 - oSize/2
oval(xPos, height()/2 - oSize/2, oSize, oSize)


print("RGB Colour 1:  ", round(clr[0]*255), "/", round(clr[1]*255), "/", round(clr[2]*255) )

print("RGB Colour 2:  ", round(clr2[0]*255), "/", round(clr2[1]*255), "/", round(clr2[2]*255) )



