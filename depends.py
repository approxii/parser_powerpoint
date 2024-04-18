from core.services.powerpoint import PowerPointService as Service

#need to fix
async def get_service() -> Service:
    return Service()
