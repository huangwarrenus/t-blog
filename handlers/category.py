from base import BaseHandler
from models import category
from tornado.web import authenticated


class IndexHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render("category.html", categories=category.get_categories())

    @authenticated
    def post(self):
        category.add(category.Category(self.get_argument("name")))
        self.redirect("/admin/categories")


class EditHandler(BaseHandler):
    @authenticated
    def get(self, category_id):
        self.render("category_edit.html", category=category.get_category_by_id(int(category_id)))
    @authenticated
    def post(self, category_id):
        category.update(category_id, self.get_argument("name"))
        self.redirect("/admin/categories")


class DeleteHandler(BaseHandler):
    @authenticated
    def get(self, id):
        self.render("category_delete.html", category=category.get_category_by_id(int(id)))

    @authenticated
    def delete(self):
        category.delete_by_id(int(self.get_argument("id")))
        self.redirect("/admin/categories")
