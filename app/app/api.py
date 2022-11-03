from ninja import NinjaAPI
from chatapp.api import router as chatapp_router


api = NinjaAPI(
    version='1.0.0', title='Chat App API', description='Yannix Chat App Server Assignment'
)

api.add_router('/', chatapp_router)
