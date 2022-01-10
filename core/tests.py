from config.wsgi import *
from core.security.models import *
from django.contrib.auth.models import Permission
from core.user.models import *
from core.homepage.models import *

# dashboard
dashboard = Dashboard()
dashboard.name = 'Sudo TechTechnologyonology'
dashboard.system_name = 'Sudo Technology'
dashboard.icon = 'fas fa-paw'
dashboard.layout = 1
dashboard.card = 'card-primary'
dashboard.navbar = 'navbar-dark navbar-primary'
dashboard.brand_logo = ''
dashboard.sidebar = 'sidebar-dark-primary'
dashboard.save()

# Mainpage
mainpage = Mainpage()
mainpage.name = 'Sudo Technology'
mainpage.proprietor = 'Sudo Technology'
mainpage.desc = 'Te ofrecemos el mejor servicio de tecnologia en el mercado..'
mainpage.with_us = 'Somos una empresa dedicada a la comercialización de equipos tecnologicos inteligentes, desarrollo tecnologico y servicio tecnico de proyectores, computadoras y todo equipo tecnologico.'
mainpage.mission = 'Ofrecer bienestar a cada una de nuestros clientes,Nuestro grupo de trabajo comparte valores y principios éticos de respeto, responsabilidad y compromiso, superándolas expectativas de nuestros clientes y entregando calidad y satisfacción en nuestros servicios.'
mainpage.vision = 'Ser una empresa sólida, líder en prestación de servicios tecnologicos de la mejor calidad y profesionalismo.'
mainpage.about_us = 'Proporcionar una atención de calidad con productos y servicios integrales satisfaciendo las necesidades de nuestros clientes.'
mainpage.phone = '0984717773'
mainpage.mobile = '0984717773'
mainpage.address = 'Niagara, Latacunga - Ecuador'
mainpage.email = 'asesoria@sudo.com'
mainpage.coordinates = '-2.1327665,-79.5912141'
mainpage.about_youtube = 'https://www.youtube.com/watch?v=-To5Xq6JP6M&list=RD-To5Xq6JP6M&start_radio=1'
mainpage.horary = 'Lunes a Viernes de 10:30 AM - 17:00 PM'
mainpage.save()

SocialNetworks(css='twitter', url='https://twitter.com/', icon='fab fa-twitter', state=True).save()
SocialNetworks(css='facebook', url='https://facebook.com/', icon='fab fa-facebook-f', state=True).save()
SocialNetworks(css='instagram', url='https://instagram.com/', icon='fab fa-instagram', state=True).save()
SocialNetworks(css='skype', url='https://skype.com/', icon='fab fa-skype', state=True).save()
SocialNetworks(css='linkedin', url='https://linkedin.com/', icon='fab fa-linkedin-in', state=True).save()

# module type

module = Module()
module.name = 'Cambiar password'
module.url = '/user/update/password/'
module.is_active = True
module.is_vertical = False
module.is_visible = True
module.icon = 'fas fa-key'
module.description = 'Permite cambiar tu password de tu cuenta'
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.name = 'Editar perfil'
module.url = '/user/update/profile/'
module.is_active = True
module.is_vertical = False
module.is_visible = True
module.icon = 'fas fa-user'
module.description = 'Permite cambiar la información de tu cuenta'
module.save()
print('insertado {}'.format(module.name))


type = ModuleType()
type.name = 'Seguridad'
type.icon = 'fas fa-lock'
type.save()
print('insertado {}'.format(type.name))

module = Module()
module.moduletype_id = 1
module.name = 'Tipos de Módulos'
module.url = '/security/module/type/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-door-open'
module.description = 'Permite administrar los tipos de módulos del sistema'
module.save()
for p in Permission.objects.filter(content_type__model=ModuleType._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 1
module.name = 'Módulos'
module.url = '/security/module/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-th-large'
module.description = 'Permite administrar los módulos del sistema'
module.save()
for p in Permission.objects.filter(content_type__model=Module._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 1
module.name = 'Grupos'
module.url = '/security/group/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-users'
module.description = 'Permite administrar los grupos de usuarios del sistema'
module.save()
for p in Permission.objects.filter(content_type__model=Group._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 1
module.name = 'Respaldos'
module.url = '/security/database/backups/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-database'
module.description = 'Permite administrar los respaldos de base de datos'
module.save()
for p in Permission.objects.filter(content_type__model=DatabaseBackups._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 1
module.name = 'Conf. Dashboard'
module.url = '/security/dashboard/update/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-tools'
module.description = 'Permite configurar los datos de la plantilla'
module.save()
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 1
module.name = 'Accesos'
module.url = '/security/access/users/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-user-secret'
module.description = 'Permite administrar los accesos de los usuarios'
module.save()
for p in Permission.objects.filter(content_type__model=AccessUsers._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

type = ModuleType()
type.name = 'Usuarios'
type.icon = 'fas fa-users'
type.save()
print('insertado {}'.format(type.name))

module = Module()
module.moduletype_id = 2
module.name = 'Administradores'
module.url = '/user/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-user'
module.description = 'Permite administrar a los administradores del sistema'
module.save()
for p in Permission.objects.filter(content_type__model=User._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))


type = ModuleType()
type.name = 'Página Web'
type.icon = 'fas fa-house-damage'
type.save()
print('insertado {}'.format(type.name))

module = Module()
module.moduletype_id = 3
module.name = 'Información'
module.url = '/mainpage/update/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-home'
module.description = 'Permite administrar la información de la página principal'
module.save()
for p in Permission.objects.filter(content_type__model=Mainpage._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Noticias'
module.url = '/homepage/news/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'far fa-newspaper'
module.description = 'Permite administrar las noticias del dashboard'
module.save()
for p in Permission.objects.filter(content_type__model=News._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Videos'
module.url = '/homepage/videos/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-photo-video'
module.description = 'Permite administrar las videos del dashboard'
module.save()
for p in Permission.objects.filter(content_type__model=Videos._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Redes Sociales'
module.url = '/homepage/socialnetworks/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'far fa-thumbs-up'
module.description = 'Permite administrar las redes sociales de la página'
module.save()
for p in Permission.objects.filter(content_type__model=SocialNetworks._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Departamentos'
module.url = '/homepage/departments/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-city'
module.description = 'Permite administrar los departamentos de la página'
module.save()
for p in Permission.objects.filter(content_type__model=Departments._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Servicios'
module.url = '/homepage/services/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-atlas'
module.description = 'Permite administrar los servicios de la página'
module.save()
for p in Permission.objects.filter(content_type__model=Services._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Estadísticas'
module.url = '/homepage/statistics/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fab fa-stack-overflow'
module.description = 'Permite administrar las estadísticas de la página'
module.save()
for p in Permission.objects.filter(content_type__model=Statistics._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Preguntas frecuentes'
module.url = '/homepage/freqquestions/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-question-circle'
module.description = 'Permite administrar las preguntas frecuentes de la página'
module.save()
for p in Permission.objects.filter(content_type__model=FreqQuestions._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Testimonios'
module.url = '/homepage/testimonials/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-comment-alt'
module.description = 'Permite administrar los testimonios de la página'
module.save()
for p in Permission.objects.filter(content_type__model=Testimonials._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Galería'
module.url = '/homepage/gallery/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-file-image'
module.description = 'Permite administrar las imágenes de la página'
module.save()
for p in Permission.objects.filter(content_type__model=Gallery._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Doctores'
module.url = '/homepage/team/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-users-cog'
module.description = 'Permite administrar a los doctores de la página'
module.save()
for p in Permission.objects.filter(content_type__model=Team._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Comentarios'
module.url = '/homepage/comments/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-envelope'
module.description = 'Permite administrar los comentarios de la página'
module.save()
for p in Permission.objects.filter(content_type__model=Comments._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))

module = Module()
module.moduletype_id = 3
module.name = 'Cualidades'
module.url = '/homepage/qualities/'
module.is_active = True
module.is_vertical = True
module.is_visible = True
module.icon = 'fas fa-folder-open'
module.description = 'Permite administrar los comentarios de la página'
module.save()
for p in Permission.objects.filter(content_type__model=Qualities._meta.label.split('.')[1].lower()):
    module.permits.add(p)
print('insertado {}'.format(module.name))


# group
group = Group()
group.name = 'Administrador'
group.save()
print('insertado {}'.format(group.name))
notsearch = [
]
for m in Module.objects.filter().exclude(
        url__in=notsearch):
    gm = GroupModule()
    gm.module = m
    gm.group = group
    gm.save()
    for perm in m.permits.all():
        group.permissions.add(perm)
        grouppermission = GroupPermission()
        grouppermission.module_id = m.id
        grouppermission.group_id = group.id
        grouppermission.permission_id = perm.id
        grouppermission.save()

# user
u = User()
u.first_name = 'Techonology'
u.last_name = 'Sudo'
u.username = 'admin'
u.dni = '0984717773'
u.email = 'kevinits@develworld.com'
u.is_active = True
u.is_superuser = True
u.is_staff = True
u.set_password('kevinpaul1997')
u.save()

group = Group.objects.get(pk=1)
u.groups.add(group)
