from flask import Flask
from flask_principal import Principal, Permission, RoleNeed

app = Flask(__name__)
Principal(app)

# Definimos los roles y permisos

permissions = {
    "admin": ['create', 'read', 'update', 'delete'],
    "editor": ['read', 'update'],
    "user": ['read']
}

roles_permissions = {
    "admin": ['create', 'read', 'update', 'delete'],
    "user": ['read']
}

admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

# Verificamos los permisos
def check_permissions(role, action):
    if action in roles_permissions.get(role, []):
        return True
    return False


@app.route('/admin', methods=['GET'])
@admin_permission.require(http_exception=403)
def admin_panel():
    return "Admin Panel"

@app.route('/user', methods=['GET'])
def user_panel():
    return "User Panel"

if __name__ == '__main__':
    app.run(debug=True)