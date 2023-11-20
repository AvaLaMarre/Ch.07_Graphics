import arcade
arcade.open_window(600, 600, "Where the Title Goes", True)
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()
#WHERE DRAWING GOES
arcade.draw_circle_filled(50,50,20, arcade.color.RED)
arcade.draw_rectangle_filled(100, 100,50,50, arcade.color.AERO_BLUE)

arcade.finish_render()

arcade.run()
