from tree_utils_02.size_tree import *
from tree_utils_02.size_node import FileSizeNode
import tempfile
import os


def test_construct_filenode_file():
    size_tree = SizeTree()
    with tempfile.NamedTemporaryFile() as fp:
        temp_file = fp.name
        temp_file_name = os.path.basename(temp_file)
        assert FileSizeNode(
            name=temp_file_name,
            is_dir=False,
            children=[],
            size=os.path.getsize(temp_file)
        ) == size_tree.construct_filenode(temp_file, False)

def test_construct_filenode_dir():
    size_tree = SizeTree()
    with tempfile.TemporaryDirectory() as tmpdir:
        temp_dir_name = os.path.basename(tmpdir)
        assert FileSizeNode(
            name=temp_dir_name,
            is_dir=True,
            children=[],
            size=BLOCK_SIZE
        ) == size_tree.construct_filenode(tmpdir, True)

def test_update_filenode():
    size_tree = SizeTree()
    with tempfile.TemporaryDirectory() as tmpdir:
        fn = size_tree.construct_filenode(tmpdir, True)
        with tempfile.NamedTemporaryFile(dir=tmpdir) as fp:
            fp.write(b'Now the file has more content and size!')
            fp.seek(0)
            fsize = os.path.getsize(fp.name)
            fn_updated = size_tree.update_filenode(size_tree.get(tmpdir, False))
            assert fn.size + 2 * fsize == fn_updated.size
