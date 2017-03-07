{
    'name': "OBC Install",
    'description': """ point of sale""",

    'summary': """
        This module is used to customize the POS""",

    'version': '10.0.1.0.0',
    'category': 'pos',
    'application': True,
    'installable': True,
    'depends': [
        'point_of_sale',
        'stock',
        'account',
        'stock_account',
        'pos_debranding',
        'to_pos_shared_floor',
        'obc_custom',
        'pos_multi_currency',
        'pos_multi_session',
        'pos_multi_session_restaurant',
        'pos_combo',
        'theme_kit',
                ],
    'data': [],
    'demo': [],
    'qweb': [],
}
