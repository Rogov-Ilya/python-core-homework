def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """

    result = {'categories': []}
    for categoryId in mapping['categoryIdsSorted']:
        roles = []
        for roleId in mapping['categories'][categoryId]['roleIds']:
            roles.append({'id': roleId, "text": mapping['roles'][roleId]['name']})
        result['categories'].append({'id': f'category-{categoryId}', "text": mapping['categories'][categoryId]['name'],
                                     'items': roles})

    return result
