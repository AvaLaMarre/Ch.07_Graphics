import arcade
arcade.open_window(600, 600, "213759")
arcade.set_background_color(arcade.color.AMAZON)
arcade.start_render()
x = 200
y = 200
for i in range(2):
    arcade.draw_line(x, 0 ,x, 600, arcade.color.BLACK)
    arcade.draw_line(0, y, 600, y, arcade.color.BLACK)
    x += 200
    y += 200
"TOP LEFT SQUARE"
arcade.draw_rectangle_filled(100, 500, 50, 50, arcade.color.NEON_CARROT)
arcade.draw_rectangle_outline(100, 500, 50, 50, arcade.color.BLACK, 2)
"TOP MIDDLE SQUARE"
arcade.draw_circle_filled(300, 500, 50, arcade.color.BRIGHT_TURQUOISE)
"TOP RIGHT SQUARE"
arcade.draw_arc_filled(500, 500, 50, 50, arcade.color.YELLOW, 200, 500)
"MIDDLE LEFT SQUARE"
arcade.draw_polygon_filled(((0, 300), (100, 400), (200, 300), (100, 200)), arcade.color.BARBIE_PINK)
"MIDDLE MIDDLE SQUARE"

"MIDDLE RIGHT SQUARE"
arcade.draw_rectangle_filled(500, 300, 200, 200, arcade.color.WHITE)
y = 390
for i in range(5):
    arcade.draw_rectangle_filled(500, y, 200, 20, arcade.color.RED)
    y -= 40
arcade.draw_rectangle_filled(450, 350, 100, 100, arcade.color.NAVY_BLUE)
"BOTTOM LEFT SQUARE"
x = 20
for i in range(5):
    arcade.draw_circle_filled(x, 100, 20, arcade.color.BLUEBERRY)
    x += 40
" BOTTOM MIDDLE SQUARE"
x = 210
y = 190
for i in range(19):
    x = 210
    for i in range(19):
        arcade.draw_point(x, y, arcade.color.NEON_GREEN, 2)
        x += 10
    y -= 10
"BOTTOM RIGHT SQUARE"
arcade.draw_text("Ava LaMarre", 455,100, arcade.color.BLACK,12)
arcade.finish_render()
arcade.run()
