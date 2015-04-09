"""
The module contains a collection of helper routines for composing deployment scripts for Azure Web Apps.
"""


from subprocess import check_call


_node_path = None
_python_path = None


def _get_node_path():
    global _node_path

    if not _node_path:
        #TODO: Add support for path discovery by external Azure script
        _node_path = "node"

    return _node_path


def _get_python_path():
    global _python_path

    if not _python_path:
        #TODO: Add support for path discovery by external Azure script
        _python_path = "python"

    return _python_path


def _call(command, args):
    command_args = [command]
    command_args.extend(args)

    return check_call(command_args)


def call_node(*args):
    """
    Calls the node.js with given list of arguments.

    Returns:
        The exit code.

    """
    node_path = _get_node_path()
    _call(node_path, args)


def call_python(*args):
    """
    Calls the Python with given list of arguments.

    Returns:
        The exit code.

    """
    python_path = _get_python_path()
    _call(python_path, args)
