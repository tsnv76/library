import graphene
from graphene_django import DjangoObjectType
from .models import Author, Book


# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value='world')



class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)

    def resolve_all_authors(root, info):
        return Author.objects.all()

    all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        return Book.objects.all()

    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))

    def resolve_author_by_id(root, info, id):
        try:
            return Author.objects.get(id=id)
        except Author.DoesNotExist:
            return None

    author_by_name = graphene.List(AuthorType, first_name=graphene.String(required=False))

    def resolve_author_by_name(root, info, first_name=None):
        authors = Author.objects.all()
        if first_name:
            authors = authors.filter(first_name=first_name)
        return authors


class AuthorCreateMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday_year = graphene.Int(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday_year):
        author = Author(first_name=first_name, last_name=last_name, birthday_year=birthday_year)
        author.save()
        return AuthorCreateMutation(author)


class AuthorUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        birthday_year = graphene.Int(required=False)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id, first_name=None, last_name=None, birthday_year=None):
        author = Author.objects.get(id=id)
        if birthday_year:
            author.birthday_year = birthday_year
        if first_name:
            author.first_name = first_name
        if last_name:
            author.last_name = last_name
        if first_name or last_name or birthday_year:
            author.save()
        return AuthorUpdateMutation(author)


class Mutations(graphene.ObjectType):
    create_author = AuthorCreateMutation.Field()
    update_author = AuthorUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
