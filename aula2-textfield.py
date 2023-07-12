import flet as ft



def main(page):

    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Digite seu nome."
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Digite sua senha"
            page.update()

        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}/ Senha: {senha}")
            page.clean()
            page.add(ft.Text(f'Olá {nome}, seja bem vindo!'))
        pass



    entrada_nome = ft.TextField(label='Digite seu nome')
    entrada_senha = ft.TextField(label='Digite sua senha', password=True)
    
    page.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("Confirmar", on_click=login)
    )
    pass

ft.app(target=main)