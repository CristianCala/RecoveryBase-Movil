import pymysql
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen


from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.datatables import MDDataTable


Window.size = (400,500)

class RecoveryInit(MDApp):

	title: 'RecoveryBase'

	def build(self):
		pantalla = Builder.load_file('vista_Logo.kv')

		return pantalla

	def cerrar(self):
		MDApp.get_running_app().stop()
		Window.close()

	def menu(self):
		print("Prueba")

	def data_table(self):
		print("Crear tabla")   


	# para llamar funciones cada 5s
	# Clock.schedule_interval(saludo, 5)
	# para llamar solo en 5s
	# Clock.schedule_once(cerrar, 10)

class StartupScreen(Screen):
	pass

class MenuScreen(Screen):
	pass


class Tab(FloatLayout, MDTabsBase):
	pass

# class RecoveryBase(MDApp):
# 	def build(self):

# 		return Builder.load_file('vista.kv')

# 	def menu(self):
# 		print("Buenasss")

# 	def data_table(self):
# 		print("Crear tabla")        


if __name__ == '__main__':
	RecoveryInit().run()
