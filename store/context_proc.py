from .models.cordinate import Cordinate

def cor_x_y(request):
	db1 = Cordinate.objects.all()[0]
	context = {
		'db1': db1
	}
	return context