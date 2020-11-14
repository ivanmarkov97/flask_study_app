from flask import Blueprint

purchase = Blueprint('purchase_bp', __name__, template_folder='templates')


@purchase.route('/purchase')
def purchase_main():
	return 'purchase page'
