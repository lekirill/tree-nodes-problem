cache_success_1 = {
    1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1, 'children': {}}}

cache_success_2 = {
    1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1, 'children': {}},
    6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False, 'children': {}}}

cache_success_3 = {1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1,
                       'children': {2: {'node_id': 2, 'value': 'value_2', 'parent_id': 1, 'is_deleted': False,
                                        'children': {
                                            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False,
                                                'children': {}}}}}}}

cache_success_4 = {1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1,
                       'children': {2: {'node_id': 2, 'value': 'value_2', 'parent_id': 1, 'is_deleted': False,
                                        'children': {
                                            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False,
                                                'children': {}}}}}},
                   8: {'node_id': 8, 'value': 'value_2', 'parent_id': 5, 'is_deleted': False, 'children': {
                       10: {'node_id': 10, 'value': 'value_2', 'parent_id': 8, 'is_deleted': False, 'children': {}}}}}

cache_success_5 = {1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1,
                       'children': {2: {'node_id': 2, 'value': 'value_2', 'parent_id': 1, 'is_deleted': False,
                                        'children': {
                                            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False,
                                                'children': {}},
                                            5: {'node_id': 5, 'value': 'value_5', 'parent_id': 2, 'is_deleted': False,
                                                'children': {8: {'node_id': 8, 'value': 'value_2', 'parent_id': 5,
                                                                 'is_deleted': False, 'children': {
                                                        10: {'node_id': 10, 'value': 'value_2', 'parent_id': 8,
                                                             'is_deleted': False, 'children': {}}}}}}}}}}}

cache_for_flat= {1: {'node_id': 1, 'value': 'value_1', 'parent_id': None, 'is_deleted': False, 'level': 1,
                       'children': {2: {'node_id': 2, 'value': 'value_2', 'parent_id': 1, 'is_deleted': False,
                                        'children': {
                                            6: {'node_id': 6, 'value': 'value_6', 'parent_id': 2, 'is_deleted': False,
                                                'children': {}},
                                            5: {'node_id': 5, 'value': 'value_5', 'parent_id': 2, 'is_deleted': False,
                                                'children': {8: {'node_id': 8, 'value': 'value_2', 'parent_id': 5,
                                                                 'is_deleted': False, 'children': {
                                                        10: {'node_id': 10, 'value': 'value_2', 'parent_id': 8,
                                                             'is_deleted': False, 'children': {}}}}}}}}}}}