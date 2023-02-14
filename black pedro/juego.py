from baraja import Baraja
from mano import Mano

mibaraja=Baraja()
mano1=Mano()
mibaraja.mezclar()
mibaraja.mostrar()
cartacogida=mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
mano1.mostrar_mano()