@main.app_errorhandler(404)
def four_0_four(error)
'''
Function to render the 404 page
'''
return render _template('four_of_four.html'),404