from Plant import *



class User:

    def __init__(self, maap, time, ui):
        self.is_brain_eaten = False
        self.nums_of_sun = 0
        self.time = time
        self.maap = maap
        self.ui = ui

    def place_the_plant(self, plant_type, pos_x, pos_y):  # if succeeded returns True
        new_plant = None
        tile = self.maap.find_tile_by_pos(pos_x, pos_y)
        if tile is not None:
            print("tile:  ", tile.row_num, tile.col_num)
            if tile.is_tile_empty():
                print("tile is empty")  
                if plant_type == PeaShooter.NAME:
                    new_plant = PeaShooter(tile.get_x_center(), tile.get_y_center(), self.maap, 
                                           self.time, tile.get_row_num(), tile.get_col_num(), self.ui)
                      
                elif plant_type == SnowPeaShooter.NAME:
                    new_plant = SnowPeaShooter(tile.get_x_center(), tile.get_y_center(), self.maap, 
                                               self.time, tile.get_row_num(), tile.get_col_num(), self.ui)

                elif plant_type == Sibzamini.NAME:
                    new_plant = Sibzamini(tile.get_x_center(), tile.get_y_center(), self.maap, 
                                          self.time, tile.get_row_num(), tile.get_col_num(), self.ui)

                elif plant_type == Sunflower.NAME:
                    new_plant = Sunflower(tile.get_x_center(), tile.get_y_center(), self.maap, 
                                          self.time, tile.get_row_num(), tile.get_col_num(), self.ui)
                    
                else:
                    print("ERROR:  plant type not valid - 39User.py")

                self.maap.add_plant(new_plant, tile)

        if new_plant is not None:
            return True
        else:
            return False
            

    def increment_nums_of_sun(self):
        self.nums_of_sun += SUN_VALUE

    def dicrease_nums_of_sun(self , plant_price):
        self.nums_of_sun = self.nums_of_sun - plant_price

    def run_game(self, event):
        pass


    def get_nums_of_sun(self):
        return self.nums_of_sun
    
    def lack_of_sun_gray_mode(self):
        if not PeaShooter.is_sun_enough(self.nums_of_sun):
            self.ui.pea_shooter_gray_mode_render()
        if not SnowPeaShooter.is_sun_enough(self.nums_of_sun):
            self.ui.snow_pea_shooter_gray_mode_render()
        if not Sunflower.is_sun_enough(self.nums_of_sun):
            self.ui.sunflower_gray_mode_render()
        if not Sibzamini.is_sun_enough(self.nums_of_sun):
            self.ui.sibzamini_gray_mode_render()

    def cool_down_gray_mode(self):
        if not PeaShooter.is_available():
            self.ui.pea_shooter_gray_mode_render()
        if not SnowPeaShooter.is_available():
            self.ui.snow_pea_shooter_gray_mode_render()
        if not Sunflower.is_available():
            self.ui.sunflower_gray_mode_render()
        if not Sibzamini.is_available():
            self.ui.sibzamini_gray_mode_render()
