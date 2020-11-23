from controllers.pizzas_controller import pizzas
from controllers.auth_controller  import auth
from controllers.pizza_images_controller import pizza_images
from controllers.favfriends_controller import fav_friends
from controllers.favpizza_controller import fav_pizza

registerable_controllers = [
    auth,
    pizzas,
    pizza_images,
    fav_friends,
    fav_pizza
]