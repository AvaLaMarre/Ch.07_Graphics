import arcade

'''
1. TEST PICTURE  (10pts)
------------------------
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
Upload your code and a screenshot of your picture.
BLACK,,, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and.
'''
arcade.open_window(500, 400, "Test Picture", True)
arcade.set_background_color(arcade.color.ALMOND)
arcade.start_render()

x = 0
y = 0
while x < 500:
    arcade.draw_line(x, 0, x, 400, arcade.color.BLACK)
    x += 20
while y < 400:
    arcade.draw_line(0, y, 500, y, arcade.color.BLACK)
    y += 20
arcade.draw_arc_filled(400, 320, 120, 120, arcade.color.YELLOW, 30, 325)

arcade.draw_rectangle_filled(50, 370, 60, 20, arcade.color.PHLOX)

arcade.draw_text("I love you. I know.", 20, 160, arcade.color.BLUSH, 20)

arcade.finish_render()

arcade.run()
'''
2. FLAG CREATION  (10pts)
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
Can you use <20 lines of code?
CHALLENGE: Can  make the flag parametrically? This means if change the hoist to 520px the flag will resize accordingly.
Upload your code and a screenshot of your flag.
'''
y = 260
x = y * 1.9
arcade.open_window(x, y, "The Stars and Stripes", True)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
a = y * (1/13) - 10
b = y / 13
for i in range(7):
    arcade.draw_rectangle_filled(x/2, a, x, b, (191, 10, 48), 0)
    a = a + (2*(y/13))
c = y*(7/13)
d = y * 0.76
arcade.draw_rectangle_filled(y-d, y, d, c, (0, 40, 104), 0)
h = y * 0.063
e = y * 0.054
for i in range(1):
    arcade.draw_text("*",h,e, arcade.color.WHITE, 20)
arcade.finish_render()
arcade.run()
