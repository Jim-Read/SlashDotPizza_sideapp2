from controllers.pizzas_controller import pizzas
from controllers.auth_controller  import auth
from controllers.pizza_images_controller import pizza_images
from controllers.favfriends_controller import fav_friends
from controllers.favpizza_controller import fav_pizza
from controllers.comments_controller import comments
from controllers.likes_controller import likes
from controllers.pizzarating_controller import pizzaratings
#from controllers.user_images_controller import user_images


registerable_controllers = [
    auth,
    pizzas,
    pizza_images,
    #user_images,
    fav_friends,
    fav_pizza,
    comments,
    likes,
    pizzaratings
]