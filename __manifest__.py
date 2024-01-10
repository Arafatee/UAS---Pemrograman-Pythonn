{
    'name'      : 'Undangan',
    'version'   : '15.0-1.0.0',
    'summary'   : 'Module Create Undangan',
    'description' : """
    Membantu anda dalam pembuatan undangan anda
    """,

    'website'   : 'arafatskr.my.id',
    'category'  : 'create & tools',
    'author'    : 'Galih Nur Arafat',
    'maintenence': 'arafat.cloud',
    'license'   : 'AGPL-3',
    'depends'   : [
        'base',
        'mail',
    ],
    'data'      : [
        'view/undangan_view.xml',
        'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/undangan_card.xml',
        'reports/rismu_card.xml',
        'reports/rismu_report.xml',
        'view/rismu_view.xml',
  
    ],
    'images'    : 'static/description/icon.png',
    'application'   : True,


}