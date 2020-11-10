from controllers.comments_controllers import pizza_comments, add_comment
from controllers.favpizza_controllers import users_favpizzas, add_pizza
from controllers.friends_controllers import users_friends, add_friend
from controllers.likes_controllers import comment_likes, new_like
from controllers.pizza_controllers import pizza_comments, add_comment
from controllers.pizzaratings_controllers import pizza_rating, new_rating
from controllers.users_controllers import users, new_user, user_login, user_logout



registerable_controllers = [
    pizza_comments,
    add_comment,
    users,
    new_user,
    users_friends,
    add_friend,
    users_favpizzas,
    add_pizza,
    pizza_comments,
    comment_likes,
    new_like,
    pizza_rating,
    new_rating,
    user_login,
    user_logout

]