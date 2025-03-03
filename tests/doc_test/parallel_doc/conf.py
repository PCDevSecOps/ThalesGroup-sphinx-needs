extensions = ["sphinx_needs"]

needs_types = [
    {"directive": "story", "title": "User Story", "prefix": "US_", "color": "#BFD8D2", "style": "node"},
    {"directive": "spec", "title": "Specification", "prefix": "SP_", "color": "#FEDCD2", "style": "node"},
    {"directive": "impl", "title": "Implementation", "prefix": "IM_", "color": "#DF744A", "style": "node"},
    {"directive": "test", "title": "Test Case", "prefix": "TC_", "color": "#DCB239", "style": "node"},
]
needs_variants = {"change_author": "assignee == 'Randy Duodu'"}
needs_variant_options = ["status", "author"]
needs_filter_data = {"assignee": "Randy Duodu"}
needs_extra_options = ["my_extra_option", "another_option", "author", "comment"]
