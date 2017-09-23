
class StoneException(Exception):
    def __init__(self, msg, ast_tree):
        err_msg = msg
        if ast_tree is not None:
            err_msgs = '{0} ({1})'.format(msg,ast_tree.location())

        super(self, msg)
