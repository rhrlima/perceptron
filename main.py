"""
Perceptron classifier made with Python3 and Pygame
Author: Ricardo Henrique Remes de Lima <https://www.github.com/rhrlima>
"""

from dependencies import *

#Parametros
#--------------------------------------------
WIDTH  = 600			#largura da tela
HEIGHT = 600			#altura da tela

FPS = 60				#frames por segundo
POINT_SIZE = 8			#tamanho dos pontos

NUM_POINTS = 100		#numero de pontos
LEARNING_RATE = 0.002	#taxa de aprendizado
#--------------------------------------------

window = None
clock  = None

line_eq = LineEquation(random.uniform(-1, 1), random.uniform(-1, 1))
perc = Perceptron2D(lrate=LEARNING_RATE)

rLineIni = Point(-1, line_eq.getY(-1))
rLineEnd = Point( 1, line_eq.getY( 1))
pLineIni = Point(-1, -1)
pLineEnd = Point( 1,  1)

running = True
t_index = 0

def set_line_equation(m=None, b=None):
	if m == None or b == None:
		m = random.uniform(-1, 1)
		b = random.uniform(-1, 1)
	line_eq.m = m
	line_eq.b = b


def create_dataset(num_points=NUM_POINTS, min=-1, max=1):
	global points
	points = []
	for i in range(num_points):
		x = random.uniform(min, max)
		y = random.uniform(min, max)
		l = line_eq.getY(x)
		points.append(Point(x, y, l))
	rLineIni.y = line_eq.getY(-1)
	rLineEnd.y = line_eq.getY( 1)


def handle_event(event):
	global running
	if event.type == QUIT:
		running = False

	if event.type == MOUSEBUTTONDOWN:
		buttons = pg.mouse.get_pressed()

		if buttons[0] == 1: #right button
			pos = pg.mouse.get_pos()
			px = (2*pos[0]-WIDTH)/WIDTH
			py = -(2*pos[1]-HEIGHT)/HEIGHT
			l = line_eq.getY(px)
			p = Point(px, py, l)
			points.append(p)

		if buttons[2] == 1: #left button
			set_line_equation(random.uniform(-1, 1), random.uniform(-1, 1))
			create_dataset(NUM_POINTS)


def update():
	global t_index

	p = points[t_index]

	inputs = (p.x, p.y)
	target = p.label
	
	guess = perc.classify(inputs)
	if guess == target:
		p.color = GREEN
	else:
		p.color = RED

	perc.train(inputs, target)

	t_index += 1
	if t_index == len(points):
		t_index = 0

	pLineIni.y = perc.guess_line(-1)
	pLineEnd.y = perc.guess_line( 1)


def draw():
	window.fill(BLACK)
	#X axis
	pg.draw.line(window, GRAY, (0, HEIGHT/2), (WIDTH, HEIGHT/2))
	#Y axis
	pg.draw.line(window, GRAY, (WIDTH/2, 0), (WIDTH/2, HEIGHT))
	#real division
	pg.draw.line(window, WHITE,  (x_px(rLineIni.x), y_py(rLineIni.y)), (x_px(rLineEnd.x), y_py(rLineEnd.y)))
	#predicted division
	pg.draw.line(window, BLUE, (x_px(pLineIni.x), y_py(pLineIni.y)), (x_px(pLineEnd.x), y_py(pLineEnd.y)))

	for p in points:
		px = int(x_px(p.x))
		py = int(y_py(p.y))
		if p.label == 1:
			pg.draw.circle(window, p.color, (px, py), POINT_SIZE)
		else:
			pg.draw.rect(window, p.color, pg.Rect(px-POINT_SIZE, py-POINT_SIZE, POINT_SIZE*2, POINT_SIZE*2))

	d1 = '{:.2g}'.format(euclidean(rLineIni, pLineIni))
	d2 = '{:.2g}'.format(euclidean(rLineEnd, pLineEnd))
	pg.display.set_caption("Perceptron2D: P:{0} LR:{1} E(x,y):({2},{3})".format(NUM_POINTS, LEARNING_RATE, d1, d2))


def main_loop():
	while running:
		clock.tick(FPS)
		for event in pg.event.get():
			handle_event(event)
		update()
		draw()
		pg.display.flip()


def euclidean(pa, pb):
	return math.sqrt( (pa.x-pb.x)**2 + (pa.y-pb.y)**2 )


def x_px(x):
	return (x * WIDTH/2) + WIDTH/2


def y_py(y):
	return (y * -HEIGHT/2) + HEIGHT/2


if __name__ == '__main__':

	pg.init()
	window = pg.display.set_mode((WIDTH, HEIGHT), pg.HWSURFACE)
	clock  = pg.time.Clock()

	set_line_equation()
	create_dataset()
	main_loop()