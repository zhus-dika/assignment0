from tree_utils_02.tree import Tree
from tree_utils_02.node import FileNode
import tempfile
import os



def test_get_tree_dirs_only():
    try:
        tree = Tree()
        with tempfile.NamedTemporaryFile() as fp:
            temp_file = fp.name
            tree.get(temp_file, True)
            assert False
    except AttributeError:
        assert True


def test_get_tree_dirs_only_recurse():
    tree = Tree()
    with tempfile.NamedTemporaryFile() as fp:
        temp_file = fp.name
        assert None == tree.get(temp_file, True, True)


def test_get_tree_childs():
    with tempfile.TemporaryDirectory() as top_level:
        with tempfile.TemporaryDirectory(dir=top_level) as low_level:
            with tempfile.NamedTemporaryFile(dir=top_level) as fp:
                tree = Tree()
                fn = tree.get(top_level, False)
                assert fn.children[0] in [tree.get(low_level, False), tree.get(fp.name, False)] and \
                       fn.children[1] in [tree.get(low_level, False), tree.get(fp.name, False)]


def test_tree_exception():
    try:
        tree = Tree()
        with tempfile.NamedTemporaryFile() as fp:
            temp_file = fp.name
        tree.get(temp_file, False)
        assert False
    except AttributeError:
        assert True


def test_filter_empty_nodes_exception():
    try:
        fn = FileNode(
            name='.',
            is_dir=True,
            children=[])
        tree = Tree()
        tree.filter_empty_nodes(fn)
        assert False
    except ValueError:
        assert True


def test_filter_empty_nodes():
    tree = Tree()
    with tempfile.TemporaryDirectory() as top_level:
        with tempfile.TemporaryDirectory(dir=top_level) as low_level:
            with tempfile.NamedTemporaryFile(dir=low_level) as file:
                fn = tree.get(file.name, dirs_only=False)
                fndir_top = tree.get(top_level, dirs_only=False)
                fndir_low = tree.get(low_level, dirs_only=False)
                tree.filter_empty_nodes(fndir_top, current_path=top_level)
                assert True == os.path.exists(top_level)
                tree.filter_empty_nodes(fndir_low, current_path=low_level)
                assert True == os.path.exists(low_level)
            fndir_low = tree.update_filenode(tree.get(low_level, dirs_only=False))
            tree.filter_empty_nodes(fndir_low, current_path=top_level)
            assert False == os.path.exists(low_level)
