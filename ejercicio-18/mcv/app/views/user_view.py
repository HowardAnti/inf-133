def render_usuario_list(usuarios):
    # Representa una lista de animales como una lista de diccionarios
    return [
        {
            "id": usuario.id,
            "username": usuario.username,
            "roles": usuario.roles
        }
        for usuario in usuarios
    ]


def render_usuario_detail(usuario):
    # Representa los detalles de un animal como un diccionario
    return {
        "id": usuario.id,
        "username": usuario.username,
        "roles": usuario.roles
    }