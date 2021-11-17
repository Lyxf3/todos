# region				-----External Imports-----
# endregion

# region				-----Internal Imports-----
from .api import urls as front_api
# endregion

urlpatterns = []
urlpatterns += front_api.urlpatterns