case_one_root = [{'node_id': 1, 'parent_id': None},
                 {'node_id': 2, 'parent_id': 1},
                 {'node_id': 3, 'parent_id': 1},
                 {'node_id': 4, 'parent_id': 1},
                 {'node_id': 5, 'parent_id': 2},
                 {'node_id': 6, 'parent_id': 2},
                 {'node_id': 7, 'parent_id': 2},
                 {'node_id': 8, 'parent_id': 5},
                 {'node_id': 9, 'parent_id': 5},
                 {'node_id': 10, 'parent_id': 8}]

case_one_root_result = {
    1: {
        'node_id': 1,
        'parent_id': None,
        'children': {
            2: {
                'node_id': 2,
                'parent_id': 1,
                'children': {
                    5: {
                        'node_id': 5,
                        'parent_id': 2,
                        'children': {
                            8: {
                                'node_id': 8,
                                'parent_id': 5,
                                'children': {
                                    10: {
                                        'node_id': 10,
                                        'parent_id': 8,
                                        'children': {}
                                    }
                                }
                            },
                            9: {
                                'node_id': 9,
                                'parent_id': 5,
                                'children': {}
                            }
                        }
                    },
                    6: {
                        'node_id': 6,
                        'parent_id': 2,
                        'children': {}
                    },
                    7: {
                        'node_id': 7,
                        'parent_id': 2,
                        'children': {}
                    }
                }
            },
            3: {
                'node_id': 3,
                'parent_id': 1,
                'children': {}
            },
            4: {
                'node_id': 4,
                'parent_id': 1,
                'children': {}
            }
        }
    }
}

case_two_roots = [{'node_id': 1, 'parent_id': None},
                  {'node_id': 2, 'parent_id': 1},
                  {'node_id': 3, 'parent_id': 1},
                  {'node_id': 4, 'parent_id': 1},
                  {'node_id': 5, 'parent_id': None},
                  {'node_id': 6, 'parent_id': 5},
                  {'node_id': 7, 'parent_id': 5},
                  {'node_id': 8, 'parent_id': 6},
                  {'node_id': 9, 'parent_id': 6},
                  {'node_id': 10, 'parent_id': 9}]

case_two_roots_result = {
    1: {
        'node_id': 1,
        'parent_id': None,
        'children': {
            2: {
                'node_id': 2,
                'parent_id': 1,
                'children': {}
            },
            3: {
                'node_id': 3,
                'parent_id': 1,
                'children': {}
            },
            4: {
                'node_id': 4,
                'parent_id': 1,
                'children': {}
            }
        }
    },
    5: {
        'node_id': 5,
        'parent_id': None,
        'children': {
            6: {
                'node_id': 6,
                'parent_id': 5,
                'children': {
                    8: {
                        'node_id': 8,
                        'parent_id': 6,
                        'children': {}
                    },
                    9: {
                        'node_id': 9,
                        'parent_id': 6,
                        'children': {
                            10: {
                                'node_id': 10,
                                'parent_id': 9,
                                'children': {}
                            }
                        }
                    }
                }
            },
            7: {
                'node_id': 7,
                'parent_id': 5,
                'children': {}
            }
        }
    }
}
