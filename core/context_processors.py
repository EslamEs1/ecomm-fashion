from datetime import date

def current_year(request):
    year = date.today().year
    
    return {
        'current_year': year
    }
