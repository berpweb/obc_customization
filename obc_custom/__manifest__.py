{
    'name': "OBC Custom",

    'summary': """
        This module is used to customize the point of sale""",
    'description': """
        This module is used to customize the point of sale""",
    'version': '10.0.1.0.0',
    'application': True,
    'installable': True,
    'depends': ['product',
                'pos_combo',
                'point_of_sale'],
    'data': [
        "security/pos_security_view.xml",
        "views/main_sub_menu.xml",
        "views/point_of_sale_view.xml",
        "views/pos_order_view.xml",
        "views/pos_category_view.xml",
        "views/product_template_view.xml",
        "views/res_users_view.xml",
        "views/obc_search_view.xml",
    ],
    'demo': [],
    'qweb': [],
}
