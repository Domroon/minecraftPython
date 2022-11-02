from mcpi.minecraft import Minecraft
from mcpi import block


PLAYER_HEIGHT = 2
WORLD_CENTER = (0, 0, 0)


def set_all_blocks(mc):
    x, y, z = mc.player.getTilePos()
    for block_id in range(block.NETHER_REACTOR_CORE.id):
        mc.setBlock(x+block_id, y, z, block_id, 0)


def generate_flat(mc, width, length, block_id, height):
    x, y, z = mc.player.getTilePos()
    for x_offset in range(width):
        for z_offset in range(length):
            mc.setBlock(x+x_offset, y+height, z+z_offset, block_id, 0)


def generate_cube(mc, width, length, height, block_id):
    x, y, z = mc.player.getTilePos()
    x = x - width/4
    z = z - length/4
    for height_offset in range(height):
        for x_offset in range(width):
            for z_offset in range(length):
                mc.setBlock(x+x_offset, y+height_offset, z+z_offset, block_id, 0)


def generate_player_on_flat(mc):
    width = 10
    length = 10
    height = 100
    mc.player.setPos(0, 0, 0)
    generate_flat(mc, width, length, block.DIRT, height)
    mc.player.setPos(width/2, height + PLAYER_HEIGHT + 1, length/2)
    print(mc.player.getPos())


def generate_block(mc, block_id):
    x, y, z = mc.player.getTilePos()
    mc.setBlock(x + 2, y, z, block_id, 0)


def generate_player_ground(mc, width, length, block_id):
    x, y, z = mc.player.getTilePos()
    x = x - width/4
    z = z - length/4
    for x_offset in range(width):
        for z_offset in range(length):
            mc.setBlock(x+x_offset, y - 1, z+z_offset, block_id, 0)


def generate_wall(mc, length, height, block_id, direction):
    x, y, z = mc.player.getTilePos()
    if direction == 'x':
        for y_offset in range(height):
            for x_offset in range(length):
                mc.setBlock(x + x_offset, y + y_offset, z, block_id, 0)
    if direction == 'z':
        for y_offset in range(height):
            for z_offset in range(length):
                mc.setBlock(x, y + y_offset, z+ z_offset, block_id, 0)


def main():
    mc = Minecraft.create('85.214.205.229')
    print("1 - Generate flat Level")
    print("2 - Go to height")
    print("3 - Generate block near player")
    print("4 - Generate Cube around player")
    print("5 - Generate flat around under player")
    print("6 - Generate wall")
    
    user_input = input("Eingabe: ")
    if user_input == '1':
        width = int(input("width: "))
        length = int(input("length: "))
        height = int(input("height: "))
        generate_flat(mc, width, length, block.DIRT, height)
    if user_input == '2':
        pos = mc.player.getPos()
        height = input("height: ")
        mc.player.setPos(pos.x, height, pos.z)
    if user_input == '3':
        block_id = input("block id: ")
        generate_block(mc, int(block_id))
    if user_input == '4':
        width = int(input("width: "))
        length = int(input("length: "))
        height = int(input("height: "))
        block_id = int(input("block id: "))
        generate_cube(mc, width, length, height, block_id)
    if user_input == '5':
        width = int(input("width: "))
        length = int(input("length: "))
        block_id = int(input("block id: "))
        generate_player_ground(mc, width, length, block_id)
    if user_input == '6':
        length = int(input("length: "))
        height = int(input("height: "))
        block_id = int(input("block id: "))
        direction = input("direction (x or z): ")
        generate_wall(mc, length, height, block_id, direction)
    

if __name__ == '__main__':
    main()