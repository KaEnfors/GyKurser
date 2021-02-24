import arcade, os
from player.character import Character
from enemy.enemies import Muskroom, Muscrab

class MuskFormer(arcade.Window):
    """

    """
    player : Character
    physics = {
        'gravity' : 100
    }
    key_map = {
        'UP' : False,
        'DOWN' : False,
        'LEFT' : False,
        'RIGHT' : False
    }
    enemies = []

    def run(self):
        print("Run game")

        path = os.path.dirname(__file__)
        self.player = Character(physics=self.physics, filename=path+'/player/player_sprite.png', scale=0.4, center_x=500, center_y=500)
        self.player.set_keys(keymap=self.key_map)
        self.player.texture_left = arcade.load_texture(file_name=path+'/player/player_sprite.png', flipped_horizontally=True)
        self.player.texture_right = arcade.load_texture(file_name=path+'/player/player_sprite.png')

        for i in range(10):
            newenemy = Muskroom(physics=self.physics, filename=path+'/enemy/muskroom_sprite.png', scale=0.2, center_x=200+i*30, center_y=400)
            self.enemies.append(newenemy)

        self.thecrab = Muscrab(physics=self.physics, filename=path+'/enemy/muscrab_sprite.gif', scale=0.2, center_x=70, center_y=400)
        self.thecrab.textures = []
        self.thecrab.textures.append(arcade.load_texture(file_name=path+'/enemy/muscrab_sprite.gif'))
        self.thecrab.textures.append(arcade.load_texture(file_name=path+'/enemy/muscrab_sprite.gif', flipped_vertically=True))
#        self.thecrab.textures.append(arcade.load_texture(file_name=path+'/enemy/muskroom_sprite.png'))

        arcade.run()
        

    def on_key_press(self, key, modifiers):
        print("You pressed:", key)

        if arcade.key.W == key:
            self.key_map['UP'] = True
        if arcade.key.S == key:
            self.key_map['DOWN'] = True
        if arcade.key.A == key:
            self.key_map['LEFT'] = True
        if arcade.key.D == key:
            self.key_map['RIGHT'] = True





    def on_key_release(self, key, modifiers):
        print("You released:", key)
        if arcade.key.W == key:
            self.key_map['UP'] = False
        if arcade.key.S == key:
            self.key_map['DOWN'] = False
        if arcade.key.A == key:
            self.key_map['LEFT'] = False
        if arcade.key.D == key:
            self.key_map['RIGHT'] = False


    

    def on_update(self, deltatime):
        #print("Update!")

        self.player.on_update(delta=deltatime)
#        self.thecrab.on_update(deltatime)
#        self.thecrab.update_animation(deltatime)
#        for enemy in self.enemies:
#            enemy.on_update(delta=deltatime)

#        self.physics['gravity'] = 0
#        print(self.key_map)

    def on_draw(self):
        #print("Draw!")
        arcade.start_render()
        self.player.draw()

        self.thecrab.draw()
        
        for enemy in self.enemies:
            enemy.draw()


if __name__ == "__main__":
    MuskFormer(fullscreen=False, title="Muskformer").run()