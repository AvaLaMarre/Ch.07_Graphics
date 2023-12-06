"""
PYCASSO PROJECT (4pts)
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times.
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program.
If you have 5 lines that draw a robot, group them together with blank lines above and below.
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Upload both your code and a screenshot of your art.
"""
import arcade
arcade.open_window(600, 600, "AVA LAMARRE", )
arcade.set_background_color(arcade.color.DARK_PASTEL_BLUE)
arcade.start_render()

"BODY"
arcade.draw_circle_filled(300, 350, 120, (30, 15, 6))
arcade.draw_circle_filled(300, 220, 200, (30, 15, 6))
arcade.draw_triangle_filled(250, 400, 350, 400, 300, 250, (0, 0, 0))

"HEAD"
arcade.draw_triangle_filled(200, 500, 400, 500, 300, 300, (30, 15, 6))
arcade.draw_triangle_filled(250, 400, 350, 400, 300, 300, (138, 99, 76))

"SNOUT"
arcade.draw_rectangle_filled(300, 420, 30, 60, (138, 99, 76))
arcade.draw_rectangle_filled(290, 400, 30, 40, (138, 99, 76), 30)
arcade.draw_rectangle_filled(310, 400, 30, 40, (138, 99, 76), 330)
arcade.draw_circle_filled(300, 450, 15, (138, 99, 76))

arcade.draw_rectangle_filled(300, 330, 40, 40, arcade.color.BLACK)
arcade.draw_circle_filled(300, 290, 30, (30, 15, 6))
arcade.draw_circle_filled(300, 315, 20, (0, 0, 0))

arcade.draw_circle_filled(300, 350, 22, (138, 99, 76))

arcade.draw_circle_filled(300, 352, 10, (0, 0, 0))
arcade.draw_triangle_filled(290, 350, 310, 350, 300, 335, (0, 0, 0))
"Head shape change "
arcade.draw_rectangle_filled(205, 480, 40, 100, arcade.color.DARK_PASTEL_BLUE, 25)
arcade.draw_circle_filled(236, 477.5, 22.5, (30, 15, 6))
arcade.draw_rectangle_filled(395, 480, 40, 100, arcade.color.DARK_PASTEL_BLUE, 335)
arcade.draw_circle_filled(364, 477.5, 22.5, (30, 15, 6))
"EARS"
earY = 510
earXone = 235
earXtwo = 365
arcade.draw_circle_filled(earXone, earY, 20, (30, 15, 6))
arcade.draw_circle_filled(earXtwo, earY, 20, (30, 15, 6))
arcade.draw_circle_filled(earXone, earY, 10, arcade.color.CLASSIC_ROSE)
arcade.draw_circle_filled(earXtwo, earY, 10, arcade.color.CLASSIC_ROSE)
'EYES'
arcade.draw_circle_filled(250, 450, 10, arcade.color.WHITE)
arcade.draw_circle_filled(350, 450, 10, arcade.color.WHITE)
arcade.draw_circle_filled(249, 450, 8, arcade.color.BLACK)
arcade.draw_circle_filled(351, 450, 8, arcade.color.BLACK)
"TABLE"
arcade.draw_rectangle_filled(300, 100, 600, 200, arcade.color.BROWN_NOSE)
tableLine = 200
tableLinetwo = 200
for i in range(5):
    arcade.draw_line(0, tableLine, 600, tableLine, (70, 38, 5), 3)
    tableLine -= 40
    for q in range(7):
        arcade.draw_line(0, tableLinetwo, 600, tableLinetwo, (97, 58, 25))
        tableLinetwo -= 6
"CAKE"
y = 100
for i in range(4):
    arcade.draw_ellipse_filled(300, y, 200, 100, arcade.color.PINK)
    y += 10
    arcade.draw_ellipse_filled(300, y, 200, 100, arcade.color.WHITE)
    y += 10
arcade.draw_ellipse_filled(300, y, 200, 100, arcade.color.PINK)
candleLeftX = 210
candleRightX = 390
candleY = 195
for i in range(5):
    arcade.draw_line(candleLeftX, candleY, candleLeftX, candleY + 30, arcade.color.GOLD, 4)
    candleLeftX += 20
    arcade.draw_line(candleRightX, candleY, candleRightX, candleY + 30, arcade.color.GOLD, 4)
    candleRightX -= 20
    candleY += 7
candleLeftX = 210
candleRightX = 390
candleY = 165
for i in range(5):
    arcade.draw_line(candleLeftX, candleY, candleLeftX, candleY + 30, arcade.color.YELLOW, 4)
    candleLeftX += 20
    arcade.draw_line(candleRightX, candleY, candleRightX, candleY + 30, arcade.color.YELLOW, 4)
    candleRightX -= 20
    candleY -= 7
"HAT"
arcade.draw_triangle_filled(265, 495, 335, 495, 300, 580, arcade.color.GOLD)
arcade.draw_triangle_filled(265, 495, 275, 520, 335, 495, arcade.color.PINK_SHERBET)
arcade.draw_triangle_filled(283, 540, 292, 560, 330, 510, arcade.color.PINK_SHERBET)
"TEXT"
arcade.draw_text("BEAR", 25, 550, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("I", 30, 520, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("R", 25, 490, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("T", 25, 460, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("H", 25, 430, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("D", 25, 400, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("A", 25, 370, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("Y", 25, 340, arcade.color.BLACK, 30, 0, "left", "Times new roman")

arcade.draw_text("RAEB", 470, 550, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("I", 555, 520, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("R", 550, 490, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("T", 550, 460, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("H", 550, 430, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("D", 550, 400, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("A", 550, 370, arcade.color.BLACK, 30, 0, "left", "Times new roman")
arcade.draw_text("Y", 550, 340, arcade.color.BLACK, 30, 0, "left", "Times new roman")

"END"
arcade.finish_render()
arcade.run()
