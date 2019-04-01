#Zegar analogowy z pomocą Turtle'a
import time
import turtle


window = turtle.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)
window.title("Simple Analog Clock")
window.tracer(0)

#Tworzenie "pola manewrowego"
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h, m, s, pen):

	#rysowanie tarczy zegara
	pen.up()
	pen.goto(0, 210)
	pen.setheading(180)
	pen.color("#73e509")
	pen.pendown()
	pen.circle(210)

	#Rysowanie wskazówek zegara
	pen.penup()
	pen.goto(0,0)
	pen.setheading(90)

	#wskazówki godzin i rozmieszczenie ich co 30 stopni, długość 20px
	for _ in range(12):
		pen.fd(190)
		pen.pendown()
		pen.fd(20)
		pen.penup()
		pen.goto(0,0)
		pen.rt(30)

	#Rysowanie wskazówki godzinowej
	pen.penup()
	pen.goto(0,0)
	pen.color("#d10606")
	pen.setheading(90)
	angle = (h / 12) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(100)

	#Rysowanie wskazówki minutowej
	pen.penup()
	pen.goto(0,0)
	pen.color("#2686e0")
	pen.setheading(90)
	angle = (m / 60) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(175)

	#Rysowanie wskazówki sekundowej
	pen.penup()
	pen.goto(0,0)
	pen.color("#f2e63e")
	pen.setheading(90)
	angle = (s / 60) * 360
	pen.rt(angle)
	pen.pendown()
	pen.fd(120)

	#Ściąganie dokładnej daty w formie godzin, minut i sekund
while True:
	h = int(time.strftime("%I"))
	m = int(time.strftime("%M"))
	s = int(time.strftime("%S"))

	#Cykl odświeżania, który imituje działanie prawdziwego zegarka
	draw_clock(h, m, s, pen)
	window.update()
	time.sleep(1)
	pen.clear()

	#Zapętlenie kodu
window.mainloop()