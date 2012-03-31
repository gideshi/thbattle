import pyglet
import os

from client.ui.resource import ResLoader

with ResLoader(__file__) as args:
    locals().update(args)
    card_attack = tx('attack.tga')
    tag_attacked = anim('tag_attacked.png', [100]*3, True)
    card_graze = tx('graze.tga')
    card_heal = tx('heal.tga')
    card_demolition = tx('card_demolition.tga')
    card_reject = tx('card_reject.tga')
    card_sealarray = tx('card_sealarray.tga')
    tag_sealarray = anim('tag_sealarray.png', [83]*36, True)

    card_nazrinrod= tx('card_nazrinrod.tga')
    card_opticalcloak = tx('card_opticalcloak.tga')
    card_opticalcloak_small = tx('card_opticalcloak_small.tga')
    card_greenufo = tx('card_greenufo.tga')
    card_greenufo_small = tx('card_greenufo_small.tga')
    card_redufo = tx('card_redufo.tga')
    card_redufo_small = tx('card_redufo_small.tga')
    card_zuidai = tx('card_zuidai.tga')
    tag_zuidai = anim('tag_zuidai.png', [100]*3, True)
    card_yukaridimension = tx('card_yukaridimension.tga')
    card_duel = tx('card_duel.tga')
    card_worshiperscarnival = tx('card_worshiperscarnival.tga')
    card_mapcannon = tx('card_mapcannon.tga')
    card_hakurouken = tx('card_hakurouken.tga')
    card_hakurouken_small = tx('card_hakurouken_small.tga')
    card_reactor = tx('card_reactor.tga')
    card_reactor_small = tx('card_reactor_small.tga')
    card_umbrella = tx('card_umbrella.tga')
    card_umbrella_small = tx('card_umbrella_small.tga')
    card_roukanken = tx('card_roukanken.tga')
    card_roukanken_small = tx('card_roukanken_small.tga')
    card_gungnir = tx('card_gungnir.tga')
    card_gungnir_small = tx('card_gungnir_small.tga')
    card_laevatein = tx('card_laevatein.tga')
    card_laevatein_small = tx('card_laevatein_small.tga')
    card_thoridal = tx('card_thoridal.tga')
    card_thoridal_small = tx('card_thoridal_small.tga')
    card_repentancestick = tx('card_repentancestick.tga')
    card_repentancestick_small = tx('card_repentancestick_small.tga')
    card_wine = tx('card_wine.tga')
    tag_wine = anim('tag_wine.png', [100]*3, True)
    card_feast = tx('card_feast.tga')
    card_harvest = tx('card_harvest.tga')
    card_maidencostume = tx('card_maidencostume.tga')
    card_maidencostume_small = tx('card_maidencostume_small.tga')

    parsee_port = tx('parsee_port.png')
    youmu_port = tx('youmu_port.png')
    ldevil_port = tx('ldevil_port.png')


    for k in args.keys(): del k
    del args
