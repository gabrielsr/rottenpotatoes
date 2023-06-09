from flask_restx import Resource, fields
from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint('api', __name__)
api = Api(blueprint, doc='/doc/')

from ..models import Movie

review_api_model = api.model('MovieReview', {
    'potatoes': fields.Integer(required=True, description='The number of potatoes'),
    'moviegoer_name': fields.String(required=True, description='The name of the reviewer')
})

@api.route('/movies/<int:movie_id>/reviews')
@api.doc(params={'movie_id': 'ID of a movie'})
class Reviews(Resource):
    
    @api.marshal_with(review_api_model, as_list=True)
    def get(self, movie_id):
        return Movie.query.get_or_404(movie_id).reviews


    