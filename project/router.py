from rest_framework.routers import Route,DynamicRoute,SimpleRouter

class CustomRouter(SimpleRouter):
    routes =[
        Route(
            url=r'^{prefix}',
        mapping={"get":"list"},
        detail=False,
        initkwrgs={"suffix":"List"}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        ),
        DynamicRoute(
            url=r'^{prefix}/{lookup}/{url_path}$',
            name='{basename}-{url_name}',
            detail=True,
            initkwargs={}
        )
    ]