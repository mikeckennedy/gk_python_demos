from pyramid.view import view_config

# Model View Controller
# template is the 'view'
#
# @view_config(route_name='home', renderer='templates/index.pt')
# def my_view(request):  # Controller
#     # processing here
#     # dict is the model
#     return {'project': 'Something cool for the web', 'more': "Tested" }
#
# def not_run():
#     pass

def not_found_there(request):
    # do real response here.
    print("See, not found! {}".format(request.url))

