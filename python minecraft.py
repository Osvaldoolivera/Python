from mcpi.minecraft import Minecraft
from mcpi import block	  

mc = Minecraft.create()

mc.postToChat("Hello world")
x, y, z = mc.player.getTilePos()                                                  
#x, y, z = mc.player.getPos()

mc.postToChat("LEAVES")
mc.setBlock(x+1, y, z, 18)
mc.postToChat("WOOD")
mc.setBlock(x, y+1, z, 17)
mc.postToChat("COAL_ORE")
mc.setBlock(x, y+2, z+2, 2)
mc.setBlock(x+2, y+3, z+1, 30)
mc.setBlock(x+2, y+4, z+2, 41)
mc.setBlock(x+3, y+6, z+1, 43)
mc.setBlock(x+4, y+9,z+1, 35)
mc.setBlock(x+5, y+11, z+1, 37)
mc.setBlock(x+8, y+11, z+2, 54)
mc.setBlock(x+11, y, z+20, 56)
mc.setBlock(x+12, y, z+19, 1)
mc.setBlock(x+13, y, z+18, 7)
mc.setBlock(x+14, y, z+17, 83)
mc.setBlock(x+16, y, z+15, 82)
mc.setBlock(x+17, y, z+14, 81)
mc.setBlock(x+2, y, z+13, 85)
mc.setBlock(x+4, y, z+11, 89)
mc.setBlock(x+5, y, z+5, 10)
mc.setBlock(x+8, y, z, 11)
mc.setBlock(x+9, y, z+9, 8)
mc.setBlock(x+10, y, z+7, 60)
mc.setBlock(x+2, y, z+6, 62)
mc.setBlock(x+13, y, z+4, 2)
mc.player.setPos(0,10  ,0)
#COAL_ORE             16
#WOOD                 17
#LEAVES               18
