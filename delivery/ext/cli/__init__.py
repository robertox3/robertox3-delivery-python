import click
from delivery.ext.db import db
from delivery.ext.site import models

def init_app(app):
     
    @app.cli.command()
    def create_db():
        """Este comando inicia o Banco de Dados"""
        db.create_all()

    @app.cli.command()
    def listar_pedidos():
        click.echo("lista_de_produtos")

    @app.cli.command()
    def listar_usuarios():
        click.echo("lista_de_usuarios")
