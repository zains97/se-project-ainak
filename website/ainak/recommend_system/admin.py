from django.contrib import admin

# Register your models here.
from .models import Home
from .models import Contact
from .models import User
from .models import Comment
from .models import Contact_broker
from .models import Wish_list
from .models import Click_item
from .models import Search
from .models import Rating
from .models import Buy
from .models import Admin

admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Contact_broker)
admin.site.register(Wish_list)
admin.site.register(Click_item)
admin.site.register(Search)
admin.site.register(Rating)
admin.site.register(Buy)
admin.site.register(Admin)