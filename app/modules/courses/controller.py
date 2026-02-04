from flask_restx import Namespace, Resource
from flask_jwt_extended import jwt_required

from .security import authorizations
from .service import CourseService
from .schema import course_model, course_input_model

api = Namespace("courses", description="Courses operations", authorizations=authorizations)


@api.route("")
class CourseList(Resource):

    @api.marshal_list_with(course_model(api))
    @api.doc(security=[{'BearerAuth': []}])
    @jwt_required()
    def get(self):
        """Listar todos os cursos"""
        return CourseService.find_all()

    @api.expect(course_input_model(api))
    @api.marshal_with(course_model(api), code=201)
    @api.doc(security=[{'BearerAuth': []}])
    @jwt_required()
    def post(self):
        """Criar novo curso"""
        return CourseService.create(api.payload), 201


@api.route("/<string:course_id>")
class CourseResource(Resource):

    @api.marshal_with(course_model(api))
    @api.doc(security=[{'BearerAuth': []}])
    @jwt_required()
    def put(self, course_id):
        """Atualizar curso"""
        course = CourseService.update(course_id, api.payload)
        if not course:
            api.abort(404, "Curso não encontrado")
        return course

    @jwt_required()
    @api.doc(security=[{'BearerAuth': []}])
    def delete(self, course_id):
        """Remover curso"""
        if not CourseService.delete(course_id):
            api.abort(404, "Curso não encontrado")
        return {"message": "Curso removido com sucesso"}, 200
